from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SpaceOut(BaseModel):
    """公共空间响应"""
    id: int
    name: str
    desc: str = ""
    price: str = ""
    capacity: str = ""
    icon: str = ""
    image: str = ""

    model_config = {"from_attributes": True}


class BookingCreateRequest(BaseModel):
    """创建预约请求"""
    space_id: int
    book_date: str = Field(..., description="预约日期 YYYY-MM-DD")
    time_slot: str = Field(..., max_length=30, description="时段 如08:00-09:00")


class BookingOut(BaseModel):
    """预约记录响应"""
    id: int
    space_id: int
    space_name: str = ""
    book_date: str
    time_slot: str
    status: str = "confirmed"
    points_cost: int = 0
    created_at: datetime

    model_config = {"from_attributes": True}
