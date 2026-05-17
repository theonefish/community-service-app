from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.space import Space, Booking
from app.schemas.space import SpaceOut, BookingCreateRequest, BookingOut
from app.schemas import resp_ok

router = APIRouter(tags=["公共空间预约"])


@router.get("/spaces", summary="获取公共空间列表")
async def get_spaces(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Space).where(Space.is_active == True))  # noqa: E712
    spaces = result.scalars().all()

    data = [SpaceOut.model_validate(s).model_dump() for s in spaces]
    return resp_ok(data=data)


@router.get("/spaces/{space_id}/timeslots", summary="获取指定日期的可用时段")
async def get_timeslots(
    space_id: int,
    date_str: str = Query(..., alias="date", description="日期 YYYY-MM-DD"),
    db: AsyncSession = Depends(get_db),
):
    # 查询该空间该日已预约的时段
    book_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    result = await db.execute(
        select(Booking.time_slot).where(
            Booking.space_id == space_id,
            Booking.book_date == book_date,
            Booking.status == "confirmed",
        )
    )
    booked_slots = set(result.scalars().all())

    # 默认时段列表
    all_slots = []
    for hour in range(8, 22):
        slot = f"{hour:02d}:00-{hour + 1:02d}:00"
        all_slots.append({
            "label": slot,
            "is_available": slot not in booked_slots,
        })

    return resp_ok(data=all_slots)


@router.post("/bookings", summary="创建预约")
async def create_booking(
    body: BookingCreateRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    book_date = datetime.strptime(body.book_date, "%Y-%m-%d").date()

    # 检查时段是否已被预约
    result = await db.execute(
        select(Booking).where(
            Booking.space_id == body.space_id,
            Booking.book_date == book_date,
            Booking.time_slot == body.time_slot,
            Booking.status == "confirmed",
        )
    )
    if result.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="该时段已被预约")

    booking = Booking(
        user_id=user.id,
        space_id=body.space_id,
        book_date=book_date,
        time_slot=body.time_slot,
    )
    db.add(booking)
    await db.flush()

    # 获取空间名称
    space_result = await db.execute(select(Space).where(Space.id == body.space_id))
    space = space_result.scalar_one_or_none()

    data = BookingOut(
        id=booking.id,
        space_id=booking.space_id,
        space_name=space.name if space else "",
        book_date=body.book_date,
        time_slot=booking.time_slot,
        status=booking.status,
        points_cost=booking.points_cost,
        created_at=booking.created_at,
    )

    return resp_ok(data=data.model_dump(), message="预约成功")


@router.delete("/bookings/{booking_id}", summary="取消预约")
async def cancel_booking(
    booking_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Booking).where(Booking.id == booking_id, Booking.user_id == user.id))
    booking = result.scalar_one_or_none()

    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="预约不存在")

    if booking.status != "confirmed":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="预约不可取消")

    booking.status = "cancelled"
    return resp_ok(message="取消成功")


@router.get("/bookings", summary="获取我的预约列表")
async def get_my_bookings(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Booking).where(Booking.user_id == user.id).order_by(Booking.book_date.desc())
    )
    bookings = result.scalars().all()

    data = []
    for b in bookings:
        space_result = await db.execute(select(Space).where(Space.id == b.space_id))
        space = space_result.scalar_one_or_none()

        data.append(BookingOut(
            id=b.id,
            space_id=b.space_id,
            space_name=space.name if space else "",
            book_date=str(b.book_date),
            time_slot=b.time_slot,
            status=b.status,
            points_cost=b.points_cost,
            created_at=b.created_at,
        ).model_dump())

    return resp_ok(data=data)
