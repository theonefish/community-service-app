from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PointsBalanceOut(BaseModel):
    """积分余额响应"""
    balance: int = 0
    total_earned: int = 0
    total_spent: int = 0

    model_config = {"from_attributes": True}


class PointsRecordOut(BaseModel):
    """积分明细响应"""
    id: int
    title: str
    desc: str = ""
    value: int
    icon: str = ""
    bg_color: str = ""
    created_at: datetime

    model_config = {"from_attributes": True}
