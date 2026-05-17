from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.points import PointsAccount, PointsRecord
from app.schemas.points import PointsBalanceOut, PointsRecordOut
from app.schemas import resp_ok
from app.utils.pagination import paginate

router = APIRouter(prefix="/points", tags=["积分"])


@router.get("/balance", summary="获取积分余额")
async def get_points_balance(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(PointsAccount).where(PointsAccount.user_id == user.id))
    account = result.scalar_one_or_none()

    if not account:
        return resp_ok(data={"balance": 0, "total_earned": 0, "total_spent": 0})

    return resp_ok(data=PointsBalanceOut.model_validate(account).model_dump())


@router.get("/records", summary="获取积分明细列表")
async def get_points_records(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    query = select(PointsRecord).where(PointsRecord.user_id == user.id).order_by(PointsRecord.created_at.desc())
    result = await paginate(query, db, page, page_size)
    result["items"] = [PointsRecordOut.model_validate(r).model_dump() for r in result["items"]]

    return resp_ok(data=result)


@router.get("/rules", summary="获取积分规则说明")
async def get_points_rules():
    rules = [
        {"title": "缴费获取积分", "desc": "消费金额 × 1 积分/元"},
        {"title": "志愿活动参与", "desc": "10 积分/次"},
        {"title": "社区活动参与", "desc": "5 积分/次"},
        {"title": "新用户注册", "desc": "50 积分"},
        {"title": "公共空间预约", "desc": "根据空间定价扣除"},
    ]
    return resp_ok(data=rules)
