from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreateRequest, FeedbackOut
from app.schemas import resp_ok
from app.utils.pagination import paginate

router = APIRouter(prefix="/feedback", tags=["投诉建议"])


@router.post("", summary="提交投诉建议")
async def create_feedback(
    body: FeedbackCreateRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    fb = Feedback(
        user_id=user.id,
        type=body.type,
        description=body.description,
        images=body.images,
        is_anonymous=body.is_anonymous,
        contact_name=body.contact_name,
        contact_phone=body.contact_phone,
        room_number=body.room_number,
    )
    db.add(fb)
    await db.flush()

    return resp_ok(data=FeedbackOut.model_validate(fb).model_dump(), message="提交成功")


@router.get("", summary="获取我的反馈列表")
async def get_feedback_list(
    status_filter: str = Query("", alias="status", description="状态筛选"),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    query = select(Feedback).where(Feedback.user_id == user.id).order_by(Feedback.created_at.desc())

    if status_filter:
        query = query.where(Feedback.status == status_filter)

    result = await paginate(query, db, page, page_size)
    result["items"] = [FeedbackOut.model_validate(f).model_dump() for f in result["items"]]

    return resp_ok(data=result)


@router.get("/{feedback_id}", summary="获取反馈详情")
async def get_feedback_detail(
    feedback_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Feedback).where(Feedback.id == feedback_id, Feedback.user_id == user.id))
    fb = result.scalar_one_or_none()

    if not fb:
        return resp_ok(code=404, message="反馈不存在", data=None)

    return resp_ok(data=FeedbackOut.model_validate(fb).model_dump())
