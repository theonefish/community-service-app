from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class VolunteerProjectOut(BaseModel):
    """志愿项目响应"""
    id: int
    title: str
    desc: str = ""
    category: str
    status: str = "recruiting"
    date_time: str = ""
    location: str = ""
    current_count: int = 0
    max_count: int = 0
    requirements: str = ""
    duration: str = ""
    image: str = ""
    icon: str = ""
    is_featured: bool = False

    model_config = {"from_attributes": True}
