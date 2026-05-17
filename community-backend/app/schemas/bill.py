from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class BillOut(BaseModel):
    """账单响应"""
    id: int
    name: str
    type: str
    bill_date: str
    amount: float
    detail: str = ""
    status: str = "pending"
    icon: str = ""
    bg_color: str = ""
    paid_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


class BillPayRequest(BaseModel):
    """缴费请求"""
    bill_ids: list[int] = Field(..., description="账单ID列表")
