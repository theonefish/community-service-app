from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.repair import RepairOrder
from app.schemas.repair import RepairCreateRequest, RepairOut
from app.schemas import resp_ok
from app.utils.pagination import paginate

router = APIRouter(prefix="/repairs", tags=["报修"])


@router.post("", summary="提交报修工单")
async def create_repair(
    body: RepairCreateRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    order = RepairOrder(
        user_id=user.id,
        property_id=body.property_id,
        type=body.type,
        source=body.source,
        address=body.address,
        detail_address=body.detail_address,
        description=body.description,
        images=body.images,
        scheduled_time=body.scheduled_time,
        contact_name=body.contact_name,
        contact_phone=body.contact_phone,
    )
    db.add(order)
    await db.flush()

    return resp_ok(data=RepairOut.model_validate(order).model_dump(), message="提交成功")


@router.get("", summary="获取我的报修列表")
async def get_repairs(
    status_filter: str = Query("", alias="status", description="状态筛选"),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    query = select(RepairOrder).where(RepairOrder.user_id == user.id).order_by(RepairOrder.created_at.desc())

    if status_filter:
        query = query.where(RepairOrder.status == status_filter)

    result = await paginate(query, db, page, page_size)
    result["items"] = [RepairOut.model_validate(r).model_dump() for r in result["items"]]

    return resp_ok(data=result)


@router.get("/{repair_id}", summary="获取报修详情")
async def get_repair_detail(
    repair_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(RepairOrder).where(RepairOrder.id == repair_id, RepairOrder.user_id == user.id))
    order = result.scalar_one_or_none()

    if not order:
        return resp_ok(code=404, message="报修工单不存在", data=None)

    return resp_ok(data=RepairOut.model_validate(order).model_dump())


@router.put("/{repair_id}/cancel", summary="取消报修工单")
async def cancel_repair(
    repair_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(RepairOrder).where(RepairOrder.id == repair_id, RepairOrder.user_id == user.id))
    order = result.scalar_one_or_none()

    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="报修工单不存在")

    if order.status not in ("pending", "assigned"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="当前状态不可取消")

    order.status = "cancelled"
    return resp_ok(message="取消成功")
