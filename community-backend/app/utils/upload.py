import os
import uuid
from datetime import datetime

from fastapi import UploadFile

from app.config import settings


def get_allowed_extensions() -> set[str]:
    return set(settings.ALLOWED_EXTENSIONS.split(","))


def validate_file(filename: str, file_size: int) -> tuple[bool, str]:
    """校验上传文件"""
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in get_allowed_extensions():
        return False, f"不支持的文件类型，仅允许 {settings.ALLOWED_EXTENSIONS}"

    max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    if file_size > max_bytes:
        return False, f"文件大小不能超过 {settings.MAX_UPLOAD_SIZE_MB}MB"

    return True, ""


async def save_upload_file(file: UploadFile) -> str:
    """保存上传文件，返回相对路径"""
    ext = file.filename.rsplit(".", 1)[-1].lower() if file.filename and "." in file.filename else "jpg"
    now = datetime.now()
    dir_path = os.path.join(
        settings.UPLOAD_DIR, "images", str(now.year), f"{now.month:02d}"
    )
    os.makedirs(dir_path, exist_ok=True)

    filename = f"{uuid.uuid4().hex}.{ext}"
    file_path = os.path.join(dir_path, filename)

    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    # 返回相对 URL 路径
    return f"/uploads/images/{now.year}/{now.month:02d}/{filename}"
