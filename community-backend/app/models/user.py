from datetime import datetime

from sqlalchemy import BigInteger, String, Boolean, Integer, DateTime, Text, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    uid: Mapped[str] = mapped_column(String(20), unique=True, nullable=False, comment="用户唯一标识")
    name: Mapped[str] = mapped_column(String(50), default="", comment="用户名")
    avatar: Mapped[str] = mapped_column(String(500), default="", comment="头像URL")
    phone: Mapped[str] = mapped_column(String(20), default="", comment="手机号")
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False, comment="密码哈希")
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否已实名认证")
    bio_enabled: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否开启生物识别")
    status: Mapped[int] = mapped_column(Integer, default=1, comment="状态 1正常 0禁用")
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True, comment="软删除时间")

    tags: Mapped[list["UserTag"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    addresses: Mapped[list["Address"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class UserTag(Base):
    __tablename__ = "user_tags"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    icon: Mapped[str] = mapped_column(String(100), default="")
    text: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    user: Mapped["User"] = relationship(back_populates="tags")


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False, comment="收件人姓名")
    phone: Mapped[str] = mapped_column(String(20), nullable=False, comment="收件人电话")
    province: Mapped[str] = mapped_column(String(50), default="")
    city: Mapped[str] = mapped_column(String(50), default="")
    district: Mapped[str] = mapped_column(String(50), default="")
    detail: Mapped[str] = mapped_column(String(200), nullable=False, comment="详细地址")
    is_default: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    user: Mapped["User"] = relationship(back_populates="addresses")
