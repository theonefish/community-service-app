from datetime import datetime

from sqlalchemy import BigInteger, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Bill(Base):
    __tablename__ = "bills"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    property_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("properties.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[str] = mapped_column(String(30), nullable=False, comment="property_fee/parking_fee/utility_fee/other")
    bill_date: Mapped[str] = mapped_column(String(20), nullable=False, comment="账单周期")
    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    detail: Mapped[str] = mapped_column(String(500), default="")
    status: Mapped[str] = mapped_column(String(20), default="pending", comment="pending/paid/overdue")
    icon: Mapped[str] = mapped_column(String(100), default="")
    bg_color: Mapped[str] = mapped_column(String(30), default="")
    paid_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    payment_no: Mapped[str] = mapped_column(String(64), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
