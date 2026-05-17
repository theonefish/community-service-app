from datetime import datetime

from sqlalchemy import BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Package(Base):
    __tablename__ = "packages"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False, comment="快递公司名")
    tracking: Mapped[str] = mapped_column(String(100), default="")
    tag: Mapped[str] = mapped_column(String(50), default="", comment="存放位置标签")
    tag_class: Mapped[str] = mapped_column(String(30), default="")
    pickup_code: Mapped[str] = mapped_column(String(30), default="")
    qr_code: Mapped[str] = mapped_column(String(500), default="")
    status: Mapped[str] = mapped_column(String(20), default="pending", comment="pending/picked_up")
    arrived_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    picked_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)


class ExpressRoomInfo(Base):
    __tablename__ = "express_room_info"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    weekday_hours: Mapped[str] = mapped_column(String(100), default="")
    weekend_hours: Mapped[str] = mapped_column(String(100), default="")
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
