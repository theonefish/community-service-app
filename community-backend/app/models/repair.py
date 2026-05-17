from datetime import datetime

from sqlalchemy import BigInteger, String, DateTime, ForeignKey, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class RepairOrder(Base):
    __tablename__ = "repair_orders"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    property_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("properties.id"), nullable=True)
    type: Mapped[str] = mapped_column(String(30), nullable=False, comment="报修类型")
    source: Mapped[str] = mapped_column(String(30), default="repair", comment="来源页面")
    address: Mapped[str] = mapped_column(String(200), default="")
    detail_address: Mapped[str] = mapped_column(String(200), default="")
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    images: Mapped[dict | None] = mapped_column(JSON, nullable=True, comment="图片URL列表")
    scheduled_time: Mapped[str] = mapped_column(String(30), default="")
    contact_name: Mapped[str] = mapped_column(String(50), default="")
    contact_phone: Mapped[str] = mapped_column(String(20), default="")
    status: Mapped[str] = mapped_column(String(20), default="pending", comment="pending/assigned/processing/completed/cancelled")
    worker_name: Mapped[str] = mapped_column(String(50), default="")
    worker_phone: Mapped[str] = mapped_column(String(20), default="")
    completed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
