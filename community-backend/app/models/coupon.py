from datetime import datetime, date

from sqlalchemy import BigInteger, String, Integer, DateTime, ForeignKey, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class CouponTemplate(Base):
    __tablename__ = "coupon_templates"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String(20), nullable=False, comment="money/service/discount")
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    desc: Mapped[str] = mapped_column(String(500), default="")
    condition: Mapped[str] = mapped_column(String(100), default="")
    discount_amount: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    discount_rate: Mapped[float | None] = mapped_column(Numeric(3, 2), nullable=True)
    service_type: Mapped[str] = mapped_column(String(50), default="")
    total_count: Mapped[int] = mapped_column(Integer, default=0, comment="0=不限")
    used_count: Mapped[int] = mapped_column(Integer, default=0)
    start_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    end_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)


class UserCoupon(Base):
    __tablename__ = "user_coupons"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    template_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("coupon_templates.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="active", comment="active/used/expired")
    tag: Mapped[str] = mapped_column(String(50), default="")
    used_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    expired_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
