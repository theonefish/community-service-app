from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserTagOut(BaseModel):
    id: int
    icon: str = ""
    text: str

    model_config = {"from_attributes": True}


class UserOut(BaseModel):
    """用户信息响应"""
    id: int
    uid: str
    name: str = ""
    avatar: str = ""
    phone: str = ""
    is_verified: bool = False
    bio_enabled: bool = False
    tags: list[UserTagOut] = []
    points_balance: int = 0
    coupon_count: int = 0

    model_config = {"from_attributes": True}


class UserUpdateRequest(BaseModel):
    """更新用户信息请求"""
    name: Optional[str] = Field(None, max_length=50)
    avatar: Optional[str] = Field(None, max_length=500)


class PasswordChangeRequest(BaseModel):
    """修改密码请求"""
    old_password: str = Field(..., min_length=6, max_length=50)
    new_password: str = Field(..., min_length=6, max_length=50)


class BioAuthRequest(BaseModel):
    """生物识别开关请求"""
    bio_enabled: bool
