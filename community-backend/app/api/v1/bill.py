from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.bill import Bill
from app.schemas.bill import BillOut, BillPayRequest
from app.schemas import resp_ok
from app.utils.pagination import paginate

router = APIRouter(prefix="/bills", tags=["缴费"])


@router.get("/pending", summary="获取待缴账单列表")
async def get_pending_bills(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Bill)
        .where(Bill.user_id == user.id, Bill.status == "pending")
        .order_by(Bill.bill_date.desc())
    )
    bills = result.scalars().all()

    data = [BillOut.model_validate(b).model_dump() for b in bills]
    return resp_ok(data=data)


@router.get("/history", summary="获取历史账单列表")
async def get_history_bills(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    query = select(Bill).where(Bill.user_id == user.id, Bill.status == "paid").order_by(Bill.paid_at.desc())
    result = await paginate(query, db, page, page_size)
    result["items"] = [BillOut.model_validate(b).model_dump() for b in result["items"]]

    return resp_ok(data=result)


@router.get("/total-pending", summary="获取待缴总金额")
async def get_total_pending(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(func.sum(Bill.amount)).where(Bill.user_id == user.id, Bill.status == "pending")
    )
    total = float(result.scalar() or 0)

    return resp_ok(data={"total": total})


@router.post("/pay", summary="批量缴费")
async def pay_bills(
    body: BillPayRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Bill).where(Bill.id.in_(body.bill_ids), Bill.user_id == user.id, Bill.status == "pending")
    )
    bills = result.scalars().all()

    if not bills:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="无待缴账单")

    now = datetime.now()
    for bill in bills:
        bill.status = "paid"
        bill.paid_at = now
        bill.payment_no = f"PAY{now.strftime('%Y%m%d%H%M%S')}{bill.id:06d}"

    return resp_ok(message="缴费成功")


@router.post("/{bill_id}/pay", summary="单笔缴费")
async def pay_single_bill(
    bill_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Bill).where(Bill.id == bill_id, Bill.user_id == user.id))
    bill = result.scalar_one_or_none()

    if not bill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="账单不存在")

    if bill.status == "paid":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="账单已支付")

    now = datetime.now()
    bill.status = "paid"
    bill.paid_at = now
    bill.payment_no = f"PAY{now.strftime('%Y%m%d%H%M%S')}{bill.id:06d}"

    return resp_ok(message="缴费成功")
