from datetime import datetime

from sqlalchemy import BigInteger, String, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    desc: Mapped[str] = mapped_column(String(1000), default="")
    category: Mapped[str] = mapped_column(String(30), nullable=False, comment="art/health/family/other")
    date_time: Mapped[str] = mapped_column(String(100), default="")
    location: Mapped[str] = mapped_column(String(200), default="")
    image: Mapped[str] = mapped_column(String(500), default="")
    max_participants: Mapped[int] = mapped_column(Integer, default=0, comment="0=不限")
    current_participants: Mapped[int] = mapped_column(Integer, default=0)
    is_full: Mapped[bool] = mapped_column(Boolean, default=False)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False)
    tag: Mapped[str] = mapped_column(String(50), default="")
    status: Mapped[str] = mapped_column(String(20), default="open", comment="open/closed/ended")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)


class ActivityRegister(Base):
    __tablename__ = "activity_registers"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    activity_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("activities.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
