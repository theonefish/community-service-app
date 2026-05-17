from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NoticeOut(BaseModel):
    """公告响应"""
    id: int
    title: str
    desc: str = ""
    content: str = ""
    tag: str = ""
    tag_class: str = ""
    category: str = "all"
    image: str = ""
    image_overlay: bool = False
    link_text: str = ""
    published_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


class PropertyNoticeOut(BaseModel):
    """物业通知响应"""
    id: int
    title: str
    desc: str = ""
    icon: str = ""
    bg_color: str = ""

    model_config = {"from_attributes": True}
