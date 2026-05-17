from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ActivityOut(BaseModel):
    """社区活动响应"""
    id: int
    title: str
    desc: str = ""
    category: str
    date_time: str = ""
    location: str = ""
    image: str = ""
    max_participants: int = 0
    current_participants: int = 0
    is_full: bool = False
    is_featured: bool = False
    tag: str = ""
    status: str = "open"

    model_config = {"from_attributes": True}
