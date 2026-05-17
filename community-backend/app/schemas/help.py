from pydantic import BaseModel


class HelpCategoryOut(BaseModel):
    """帮助分类响应"""
    id: int
    name: str
    desc: str = ""
    icon: str = ""
    bg_color: str = ""
    path: str = ""

    model_config = {"from_attributes": True}


class FAQOut(BaseModel):
    """常见问题响应"""
    id: int
    question: str
    answer: str
    category: str = ""
    is_hot: bool = False

    model_config = {"from_attributes": True}
