from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.activity import Activity, ActivityRegister
from app.schemas.activity import ActivityOut
from app.schemas import resp_ok
from app.utils.pagination import paginate

router = APIRouter(prefix="/activities", tags=["社区活动"])


@router.get("", summary="获取活动列表")
async def get_activities(
    category: str = Query("", description="分类筛选"),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    query = select(Activity).where(Activity.status == "open").order_by(Activity.created_at.desc())

    if category:
        query = query.where(Activity.category == category)

    result = await paginate(query, db, page, page_size)
    result["items"] = [ActivityOut.model_validate(a).model_dump() for a in result["items"]]

    return resp_ok(data=result)


@router.get("/{activity_id}", summary="获取活动详情")
async def get_activity_detail(activity_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Activity).where(Activity.id == activity_id))
    activity = result.scalar_one_or_none()

    if not activity:
        return resp_ok(code=404, message="活动不存在", data=None)

    return resp_ok(data=ActivityOut.model_validate(activity).model_dump())


@router.post("/{activity_id}/join", summary="报名参加活动")
async def join_activity(
    activity_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Activity).where(Activity.id == activity_id))
    activity = result.scalar_one_or_none()

    if not activity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="活动不存在")

    if activity.is_full:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="活动名额已满")

    # 检查是否已报名
    existing = await db.execute(
        select(ActivityRegister).where(ActivityRegister.user_id == user.id, ActivityRegister.activity_id == activity_id)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="已报名该活动")

    register = ActivityRegister(user_id=user.id, activity_id=activity_id)
    db.add(register)

    activity.current_participants = (activity.current_participants or 0) + 1
    if activity.max_participants > 0 and activity.current_participants >= activity.max_participants:
        activity.is_full = True

    return resp_ok(message="报名成功")
