from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.banner import Banner, Menu, Merchant
from app.schemas import resp_ok

router = APIRouter(tags=["首页"])


@router.get("/banners", summary="获取轮播图列表")
async def get_banners(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Banner).where(Banner.is_visible == True).order_by(Banner.sort)  # noqa: E712
    )
    banners = result.scalars().all()

    data = [{
        "id": b.id, "tag": b.tag, "title": b.title, "desc": b.desc,
        "image": b.image, "bg_color": b.bg_color, "path": b.path,
    } for b in banners]
    return resp_ok(data=data)


@router.get("/menus", summary="获取功能菜单列表")
async def get_menus(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Menu).where(Menu.is_visible == True).order_by(Menu.sort)  # noqa: E712
    )
    menus = result.scalars().all()

    data = [{
        "id": m.id, "name": m.name, "icon": m.icon, "bg_color": m.bg_color, "path": m.path,
    } for m in menus]
    return resp_ok(data=data)


@router.get("/merchants", summary="获取推荐商家列表")
async def get_merchants(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Merchant).where(Merchant.is_visible == True).order_by(Merchant.sort)  # noqa: E712
    )
    merchants = result.scalars().all()

    data = [{
        "id": m.id, "name": m.name, "desc": m.desc, "logo": m.logo,
        "badge": m.badge, "distance": m.distance, "is_featured": m.is_featured,
    } for m in merchants]
    return resp_ok(data=data)


@router.get("/services/recommended", summary="获取推荐服务列表")
async def get_recommended_services():
    # 暂返回空列表，后续可从数据库读取
    return resp_ok(data=[])
