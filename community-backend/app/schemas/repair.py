from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class RepairCreateRequest(BaseModel):
    """提交报修请求"""
    type: str = Field(..., description="报修类型: water/appliance/door/wall/pipe/plumbing/electrical/general/other")
    source: str = Field("repair", description="来源: repair/repair_apply/repair_submit")
    address: str = Field("", max_length=200)
    detail_address: str = Field("", max_length=200)
    description: str = Field(..., max_length=500)
    images: list[str] = Field(default_factory=list)
    scheduled_time: str = Field("", max_length=30)
    contact_name: str = Field("", max_length=50)
    contact_phone: str = Field("", max_length=20)
    property_id: Optional[int] = None


class RepairOut(BaseModel):
    """报修工单响应"""
    id: int
    type: str
    source: str = "repair"
    address: str = ""
    detail_address: str = ""
    description: str
    images: list[str] = []
    scheduled_time: str = ""
    contact_name: str = ""
    contact_phone: str = ""
    status: str = "pending"
    worker_name: str = ""
    worker_phone: str = ""
    created_at: datetime
    completed_at: Optional[datetime] = None

    model_config = {"from_attributes": True}
