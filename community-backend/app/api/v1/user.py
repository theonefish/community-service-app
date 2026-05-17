from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User, UserTag
from app.models.points import PointsAccount
from app.models.coupon import UserCoupon
from app.schemas.user import UserOut, UserUpdateRequest, PasswordChangeRequest, BioAuthRequest
from app.schemas import resp_ok
from app.utils.security import verify_password, hash_password

router = APIRouter(prefix="/user", tags=["用户"])


@router.get("/profile", summary="获取用户信息")
async def get_profile(user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    # 积分余额
    result = await db.execute(select(PointsAccount).where(PointsAccount.user_id == user.id))
    points_account = result.scalar_one_or_none()
    points_balance = points_account.balance if points_account else 0

    # 优惠券数
    result = await db.execute(
        select(func.count()).select_from(UserCoupon).where(UserCoupon.user_id == user.id, UserCoupon.status == "active")
    )
    coupon_count = result.scalar() or 0

    # 手机号脱敏
    phone = user.phone
    if len(phone) == 11:
        phone = f"{phone[:3]}****{phone[-4:]}"

    user_data = UserOut(
        id=user.id,
        uid=user.uid,
        name=user.name,
        avatar=user.avatar,
        phone=phone,
        is_verified=user.is_verified,
        bio_enabled=user.bio_enabled,
        tags=[UserTagOut(id=t.id, icon=t.icon, text=t.text) for t in user.tags],
        points_balance=points_balance,
        coupon_count=coupon_count,
    )

    return resp_ok(data=user_data.model_dump())


@router.put("/profile", summary="更新用户信息")
async def update_profile(
    body: UserUpdateRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if body.name is not None:
        user.name = body.name
    if body.avatar is not None:
        user.avatar = body.avatar

    return resp_ok(message="更新成功")


@router.put("/password", summary="修改密码")
async def change_password(
    body: PasswordChangeRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if not verify_password(body.old_password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="原密码错误")

    user.password_hash = hash_password(body.new_password)
    return resp_ok(message="密码修改成功")


@router.put("/bio-auth", summary="开关生物识别")
async def toggle_bio_auth(
    body: BioAuthRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    user.bio_enabled = body.bio_enabled
    return resp_ok(message="设置成功")


# 导入 UserTagOut 避免循环依赖
from app.schemas.user import UserTagOut  # noqa: E402
