from datetime import datetime

from sqlalchemy import BigInteger, String, Boolean, Integer, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Notice(Base):
    __tablename__ = "notices"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    desc: Mapped[str] = mapped_column(String(500), default="")
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    tag: Mapped[str] = mapped_column(String(30), default="")
    tag_class: Mapped[str] = mapped_column(String(30), default="")
    category: Mapped[str] = mapped_column(String(20), default="all", comment="important/activity/all")
    image: Mapped[str] = mapped_column(String(500), default="")
    image_overlay: Mapped[bool] = mapped_column(Boolean, default=False)
    link_text: Mapped[str] = mapped_column(String(50), default="")
    is_published: Mapped[bool] = mapped_column(Boolean, default=False)
    published_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    sort: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)


class PropertyNotice(Base):
    __tablename__ = "property_notices"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    desc: Mapped[str] = mapped_column(String(500), default="")
    icon: Mapped[str] = mapped_column(String(100), default="")
    bg_color: Mapped[str] = mapped_column(String(30), default="")
    sort: Mapped[int] = mapped_column(Integer, default=0)
    is_visible: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
