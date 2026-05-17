from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PropertyOut(BaseModel):
    """房产信息响应"""
    id: int
    community_name: str
    building: str
    room: str
    owner_name: str = ""
    owner_role: str = "owner"
    property_fee_status: str = "unpaid"
    property_fee_until: str = ""
    parking_space: str = ""
    parking_status: str = "normal"
    image: str = ""
    is_current: bool = False

    model_config = {"from_attributes": True}


class PropertyCreateRequest(BaseModel):
    """绑定房产请求"""
    community_name: str = Field(..., max_length=100)
    building: str = Field(..., max_length=50)
    room: str = Field(..., max_length=50)
    owner_name: str = Field("", max_length=50)
    owner_role: str = "owner"


class BuildingOut(BaseModel):
    """楼栋信息响应"""
    id: int
    area: str
    building: str

    model_config = {"from_attributes": True}
