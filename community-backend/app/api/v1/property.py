from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.property import Property, CommunityBuilding
from app.schemas.property import PropertyOut, PropertyCreateRequest, BuildingOut
from app.schemas import resp_ok

router = APIRouter(tags=["房产"])


@router.get("/user/properties", summary="获取当前用户关联房产列表")
async def get_user_properties(user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Property).where(Property.user_id == user.id))
    properties = result.scalars().all()

    data = [PropertyOut.model_validate(p).model_dump() for p in properties]
    return resp_ok(data=data)


@router.post("/user/properties", summary="绑定房产")
async def bind_property(
    body: PropertyCreateRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    prop = Property(
        user_id=user.id,
        community_name=body.community_name,
        building=body.building,
        room=body.room,
        owner_name=body.owner_name,
        owner_role=body.owner_role,
    )
    db.add(prop)
    await db.flush()

    return resp_ok(data=PropertyOut.model_validate(prop).model_dump(), message="绑定成功")


@router.put("/user/properties/{property_id}/current", summary="切换当前选中房产")
async def switch_current_property(
    property_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # 取消当前选中
    result = await db.execute(
        select(Property).where(Property.user_id == user.id, Property.is_current == True)  # noqa: E712
    )
    for p in result.scalars().all():
        p.is_current = False

    # 设置新选中
    result = await db.execute(select(Property).where(Property.id == property_id, Property.user_id == user.id))
    prop = result.scalar_one_or_none()
    if not prop:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="房产不存在")

    prop.is_current = True
    return resp_ok(message="切换成功")


@router.delete("/user/properties/{property_id}", summary="解绑房产")
async def unbind_property(
    property_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Property).where(Property.id == property_id, Property.user_id == user.id))
    prop = result.scalar_one_or_none()
    if not prop:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="房产不存在")

    await db.delete(prop)
    return resp_ok(message="解绑成功")


@router.get("/community/buildings", summary="获取社区楼栋地址列表")
async def get_community_buildings(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CommunityBuilding).where(CommunityBuilding.is_active == True).order_by(CommunityBuilding.sort))  # noqa: E712
    buildings = result.scalars().all()

    data = [BuildingOut.model_validate(b).model_dump() for b in buildings]
    return resp_ok(data=data)


@router.get("/property/{property_id}/fee-status", summary="获取房产物业费状态")
async def get_property_fee_status(
    property_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Property).where(Property.id == property_id, Property.user_id == user.id))
    prop = result.scalar_one_or_none()
    if not prop:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="房产不存在")

    return resp_ok(data={
        "property_fee_status": prop.property_fee_status,
        "property_fee_until": prop.property_fee_until,
    })


@router.get("/property/{property_id}/parking-status", summary="获取房产停车位状态")
async def get_property_parking_status(
    property_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Property).where(Property.id == property_id, Property.user_id == user.id))
    prop = result.scalar_one_or_none()
    if not prop:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="房产不存在")

    return resp_ok(data={
        "parking_space": prop.parking_space,
        "parking_status": prop.parking_status,
    })


@router.get("/property/contact", summary="获取物业联系电话")
async def get_property_contact():
    return resp_ok(data={"phone": "4001234567"})
