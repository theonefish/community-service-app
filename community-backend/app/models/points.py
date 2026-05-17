from datetime import datetime

from sqlalchemy import BigInteger, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class PointsAccount(Base):
    __tablename__ = "points_accounts"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), unique=True, nullable=False)
    balance: Mapped[int] = mapped_column(Integer, default=0, comment="积分余额")
    total_earned: Mapped[int] = mapped_column(Integer, default=0, comment="累计获得")
    total_spent: Mapped[int] = mapped_column(Integer, default=0, comment="累计消耗")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)


class PointsRecord(Base):
    __tablename__ = "points_records"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    desc: Mapped[str] = mapped_column(String(500), default="")
    value: Mapped[int] = mapped_column(Integer, nullable=False, comment="正为获取,负为消耗")
    icon: Mapped[str] = mapped_column(String(100), default="")
    bg_color: Mapped[str] = mapped_column(String(30), default="")
    source_type: Mapped[str] = mapped_column(String(50), default="", comment="来源类型")
    source_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True, comment="来源关联ID")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
