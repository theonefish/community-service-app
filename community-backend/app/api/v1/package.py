from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.package import Package, ExpressRoomInfo
from app.schemas.package import PackageOut
from app.schemas import resp_ok

router = APIRouter(tags=["快递包裹"])


@router.get("/packages", summary="获取包裹列表")
async def get_packages(
    status_filter: str = Query("pending", alias="status", description="pending/picked_up"),
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Package).where(Package.user_id == user.id, Package.status == status_filter)
        .order_by(Package.arrived_at.desc())
    )
    packages = result.scalars().all()

    data = [PackageOut.model_validate(p).model_dump() for p in packages]
    return resp_ok(data=data)


@router.get("/packages/{package_id}/pickup-code", summary="获取取件码")
async def get_pickup_code(
    package_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Package).where(Package.id == package_id, Package.user_id == user.id))
    pkg = result.scalar_one_or_none()

    if not pkg:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="包裹不存在")

    return resp_ok(data={"pickup_code": pkg.pickup_code, "qr_code": pkg.qr_code})


@router.post("/packages/{package_id}/pickup", summary="确认取件")
async def confirm_pickup(
    package_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Package).where(Package.id == package_id, Package.user_id == user.id))
    pkg = result.scalar_one_or_none()

    if not pkg:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="包裹不存在")

    if pkg.status == "picked_up":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="包裹已取件")

    pkg.status = "picked_up"
    pkg.picked_at = datetime.now()
    return resp_ok(message="取件成功")


@router.get("/express-room/info", summary="获取快递室开放时间")
async def get_express_room_info(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ExpressRoomInfo).limit(1))
    info = result.scalar_one_or_none()

    if not info:
        return resp_ok(data={"weekday_hours": "08:00-21:00", "weekend_hours": "09:00-18:00"})

    return resp_ok(data={"weekday_hours": info.weekday_hours, "weekend_hours": info.weekend_hours})
