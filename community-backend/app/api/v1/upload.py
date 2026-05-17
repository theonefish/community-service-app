import os
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status

from app.dependencies import get_current_user
from app.models.user import User
from app.schemas import resp_ok
from app.utils.upload import validate_file, save_upload_file
from app.config import settings

router = APIRouter(prefix="/upload", tags=["文件上传"])


@router.post("/images", summary="上传图片")
async def upload_images(
    files: list[UploadFile] = File(...),
    user: User = Depends(get_current_user),
):
    if len(files) > 9:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="最多上传9张图片")

    urls = []
    for file in files:
        if not file.filename:
            continue

        is_valid, msg = validate_file(file.filename, 0)  # size 校验在 save 时处理
        if not is_valid:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)

        url = await save_upload_file(file)
        urls.append(url)

    return resp_ok(data=urls)
