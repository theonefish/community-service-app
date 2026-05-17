from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CouponOut(BaseModel):
    """优惠券响应"""
    id: int
    type: str
    name: str
    desc: str = ""
    condition: str = ""
    discount_amount: Optional[float] = None
    discount_rate: Optional[float] = None
    service_type: str = ""
    status: str = "active"
    tag: str = ""
    expired_at: Optional[datetime] = None

    model_config = {"from_attributes": True}
