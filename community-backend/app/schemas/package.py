from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PackageOut(BaseModel):
    """快递包裹响应"""
    id: int
    name: str
    tracking: str = ""
    tag: str = ""
    tag_class: str = ""
    pickup_code: str = ""
    status: str = "pending"
    arrived_at: Optional[datetime] = None

    model_config = {"from_attributes": True}
