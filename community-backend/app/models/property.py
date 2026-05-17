from datetime import datetime

from sqlalchemy import BigInteger, String, Boolean, Integer, DateTime, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Property(Base):
    __tablename__ = "properties"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    community_name: Mapped[str] = mapped_column(String(100), nullable=False, comment="小区名称")
    building: Mapped[str] = mapped_column(String(50), nullable=False, comment="栋号")
    room: Mapped[str] = mapped_column(String(50), nullable=False, comment="房号")
    owner_name: Mapped[str] = mapped_column(String(50), default="", comment="业主姓名")
    owner_role: Mapped[str] = mapped_column(String(20), default="owner", comment="身份 owner/tenant")
    property_fee_status: Mapped[str] = mapped_column(String(20), default="unpaid", comment="物业费状态")
    property_fee_until: Mapped[str] = mapped_column(String(20), default="", comment="物业费缴至日期")
    parking_space: Mapped[str] = mapped_column(String(50), default="", comment="车位号")
    parking_status: Mapped[str] = mapped_column(String(20), default="normal", comment="停车状态")
    image: Mapped[str] = mapped_column(String(500), default="", comment="房产图片")
    is_current: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否当前选中房产")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)


class CommunityBuilding(Base):
    __tablename__ = "community_buildings"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    area: Mapped[str] = mapped_column(String(50), nullable=False, comment="区域")
    building: Mapped[str] = mapped_column(String(50), nullable=False, comment="栋号")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    sort: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
