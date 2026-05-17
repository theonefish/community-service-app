from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.coupon import CouponTemplate, UserCoupon
from app.schemas.coupon import CouponOut
from app.schemas import resp_ok

router = APIRouter(prefix="/coupons", tags=["优惠券"])


@router.get("", summary="获取优惠券列表")
async def get_coupons(
    status_filter: str = Query("active", alias="status", description="active/expired"),
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(UserCoupon).where(UserCoupon.user_id == user.id, UserCoupon.status == status_filter)
        .order_by(UserCoupon.created_at.desc())
    )
    coupons = result.scalars().all()

    data = []
    for c in coupons:
        # 获取模板信息
        tpl_result = await db.execute(select(CouponTemplate).where(CouponTemplate.id == c.template_id))
        tpl = tpl_result.scalar_one_or_none()
        if tpl:
            data.append(CouponOut(
                id=c.id,
                type=tpl.type,
                name=tpl.name,
                desc=tpl.desc,
                condition=tpl.condition,
                discount_amount=float(tpl.discount_amount) if tpl.discount_amount else None,
                discount_rate=float(tpl.discount_rate) if tpl.discount_rate else None,
                service_type=tpl.service_type,
                status=c.status,
                tag=c.tag,
                expired_at=c.expired_at,
            ).model_dump())

    return resp_ok(data=data)


@router.get("/available", summary="获取可领取的优惠券模板列表")
async def get_available_coupons(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(CouponTemplate).where(CouponTemplate.is_active == True)  # noqa: E712
        .order_by(CouponTemplate.created_at.desc())
    )
    templates = result.scalars().all()

    data = [CouponOut(
        id=t.id,
        type=t.type,
        name=t.name,
        desc=t.desc,
        condition=t.condition,
        discount_amount=float(t.discount_amount) if t.discount_amount else None,
        discount_rate=float(t.discount_rate) if t.discount_rate else None,
        service_type=t.service_type,
        status="available",
    ).model_dump() for t in templates]

    return resp_ok(data=data)


@router.post("/{coupon_id}/claim", summary="领取优惠券")
async def claim_coupon(
    coupon_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(CouponTemplate).where(CouponTemplate.id == coupon_id, CouponTemplate.is_active == True))  # noqa: E712
    tpl = result.scalar_one_or_none()

    if not tpl:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="优惠券不存在")

    uc = UserCoupon(user_id=user.id, template_id=tpl.id, expired_at=tpl.end_date)
    db.add(uc)

    tpl.used_count = (tpl.used_count or 0) + 1
    return resp_ok(message="领取成功")


@router.post("/{coupon_id}/use", summary="使用优惠券")
async def use_coupon(
    coupon_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(UserCoupon).where(UserCoupon.id == coupon_id, UserCoupon.user_id == user.id))
    coupon = result.scalar_one_or_none()

    if not coupon:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="优惠券不存在")

    if coupon.status != "active":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="优惠券不可使用")

    coupon.status = "used"
    coupon.used_at = datetime.now()
    return resp_ok(message="使用成功")
