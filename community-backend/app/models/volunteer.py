from datetime import datetime

from sqlalchemy import BigInteger, String, Boolean, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class VolunteerProject(Base):
    __tablename__ = "volunteer_projects"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    desc: Mapped[str] = mapped_column(String(1000), default="")
    category: Mapped[str] = mapped_column(String(30), nullable=False, comment="elderly/environment/education/other")
    status: Mapped[str] = mapped_column(String(20), default="recruiting", comment="recruiting/full/ended")
    date_time: Mapped[str] = mapped_column(String(100), default="")
    location: Mapped[str] = mapped_column(String(200), default="")
    current_count: Mapped[int] = mapped_column(Integer, default=0)
    max_count: Mapped[int] = mapped_column(Integer, default=0, comment="0=不限")
    requirements: Mapped[str] = mapped_column(String(500), default="")
    duration: Mapped[str] = mapped_column(String(50), default="")
    image: Mapped[str] = mapped_column(String(500), default="")
    icon: Mapped[str] = mapped_column(String(100), default="")
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)


class VolunteerRecord(Base):
    __tablename__ = "volunteer_records"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    project_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("volunteer_projects.id"), nullable=False)
    hours: Mapped[float] = mapped_column(default=0.0, comment="志愿时长")
    joined_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
