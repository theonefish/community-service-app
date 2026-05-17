from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.notice import Notice, PropertyNotice
from app.schemas.notice import NoticeOut, PropertyNoticeOut
from app.schemas import resp_ok
from app.utils.pagination import paginate

router = APIRouter(prefix="/notices", tags=["公告"])


@router.get("", summary="获取公告列表")
async def get_notices(
    category: str = Query("all", description="分类: important/activity/all"),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    query = select(Notice).where(Notice.is_published == True).order_by(Notice.sort, Notice.published_at.desc())  # noqa: E712

    if category != "all":
        query = query.where(Notice.category == category)

    result = await paginate(query, db, page, page_size)
    result["items"] = [NoticeOut.model_validate(n).model_dump() for n in result["items"]]

    return resp_ok(data=result)


@router.get("/property", summary="获取物业通知列表")
async def get_property_notices(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(PropertyNotice)
        .where(PropertyNotice.is_visible == True)  # noqa: E712
        .order_by(PropertyNotice.sort)
    )
    notices = result.scalars().all()

    data = [PropertyNoticeOut.model_validate(n).model_dump() for n in notices]
    return resp_ok(data=data)


@router.get("/{notice_id}", summary="获取公告详情")
async def get_notice_detail(notice_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Notice).where(Notice.id == notice_id, Notice.is_published == True))  # noqa: E712
    notice = result.scalar_one_or_none()

    if not notice:
        return resp_ok(code=404, message="公告不存在", data=None)

    return resp_ok(data=NoticeOut.model_validate(notice).model_dump())
