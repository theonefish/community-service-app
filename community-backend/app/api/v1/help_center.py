from fastapi import APIRouter, Depends, Query
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.help import HelpCategory, FAQ
from app.schemas.help import HelpCategoryOut, FAQOut
from app.schemas import resp_ok

router = APIRouter(prefix="/help", tags=["帮助中心"])


@router.get("/categories", summary="获取帮助分类列表")
async def get_help_categories(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(HelpCategory).where(HelpCategory.is_visible == True).order_by(HelpCategory.sort)  # noqa: E712
    )
    categories = result.scalars().all()

    data = [HelpCategoryOut.model_validate(c).model_dump() for c in categories]
    return resp_ok(data=data)


@router.get("/faq", summary="搜索/获取常见问题")
async def get_faq(
    keyword: str = Query("", description="搜索关键词"),
    category: str = Query("", description="分类筛选"),
    db: AsyncSession = Depends(get_db),
):
    query = select(FAQ).where(FAQ.is_visible == True).order_by(FAQ.sort)  # noqa: E712

    if keyword:
        query = query.where(or_(FAQ.question.contains(keyword), FAQ.answer.contains(keyword)))

    if category:
        query = query.where(FAQ.category == category)

    result = await db.execute(query)
    faqs = result.scalars().all()

    data = [FAQOut.model_validate(f).model_dump() for f in faqs]
    return resp_ok(data=data)


@router.get("/faq/hot", summary="获取热门问题")
async def get_hot_faq(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(FAQ).where(FAQ.is_hot == True, FAQ.is_visible == True).order_by(FAQ.sort)  # noqa: E712
    )
    faqs = result.scalars().all()

    data = [FAQOut.model_validate(f).model_dump() for f in faqs]
    return resp_ok(data=data)


@router.get("/contact", summary="获取客服联系方式")
async def get_contact():
    return resp_ok(data={"phone": "4001234567", "online_service": True})
