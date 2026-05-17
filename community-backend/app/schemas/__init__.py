from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ResponseBase(BaseModel):
    """统一响应模型"""
    code: int = 200
    message: str = "success"
    data: Optional[dict | list | None] = None


class ResponseOK(ResponseBase):
    """成功响应（无数据）"""
    pass


def resp_ok(data=None, message: str = "success", code: int = 200) -> dict:
    return {"code": code, "message": message, "data": data}


class PageParams(BaseModel):
    """分页参数"""
    page: int = 1
    page_size: int = 10


class PageResult(BaseModel):
    """分页结果"""
    items: list
    total: int
    page: int
    page_size: int
    pages: int


def make_page_result(items: list, total: int, page: int, page_size: int) -> dict:
    """构建分页响应数据"""
    pages = (total + page_size - 1) // page_size if page_size > 0 else 0
    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size,
        "pages": pages,
    }
