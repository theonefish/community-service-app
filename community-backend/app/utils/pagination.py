from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession


async def paginate(query, db: AsyncSession, page: int = 1, page_size: int = 10):
    """通用分页工具"""
    # 总数
    count_query = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_query)).scalar() or 0

    # 分页数据
    offset = (page - 1) * page_size
    items_query = query.offset(offset).limit(page_size)
    result = await db.execute(items_query)
    items = result.scalars().all()

    pages = (total + page_size - 1) // page_size if page_size > 0 else 0

    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size,
        "pages": pages,
    }
