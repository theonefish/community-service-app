from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class FeedbackCreateRequest(BaseModel):
    """提交投诉建议请求"""
    type: str = Field(..., description="类型: noise/hygiene/security/attitude/facility/other")
    description: str = Field(..., max_length=1000)
    images: list[str] = Field(default_factory=list)
    is_anonymous: bool = False
    contact_name: str = Field("", max_length=50)
    contact_phone: str = Field("", max_length=20)
    room_number: str = Field("", max_length=50)


class FeedbackOut(BaseModel):
    """投诉建议响应"""
    id: int
    type: str
    description: str
    images: list[str] = []
    is_anonymous: bool = False
    contact_name: str = ""
    contact_phone: str = ""
    room_number: str = ""
    status: str = "pending"
    reply: str = ""
    replied_at: Optional[datetime] = None
    created_at: datetime

    model_config = {"from_attributes": True}
