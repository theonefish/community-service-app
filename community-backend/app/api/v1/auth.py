from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, RefreshTokenRequest
from app.schemas import resp_ok
from app.utils.security import (
    verify_password, hash_password,
    create_access_token, create_refresh_token, decode_token,
)

router = APIRouter(prefix="/auth", tags=["认证"])


@router.post("/login", summary="用户登录")
async def login(body: LoginRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.phone == body.phone, User.deleted_at.is_(None)))
    user = result.scalar_one_or_none()

    if not user or not verify_password(body.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="手机号或密码错误")

    if user.status != 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="用户已被禁用")

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return resp_ok(data=TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    ).model_dump())


@router.post("/register", summary="用户注册")
async def register(body: RegisterRequest, db: AsyncSession = Depends(get_db)):
    # 检查手机号是否已注册
    result = await db.execute(select(User).where(User.phone == body.phone))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="该手机号已注册")

    # 生成 uid
    import random
    uid = str(random.randint(10000000, 99999999))

    user = User(
        uid=uid,
        name=body.name or f"用户{uid[-4:]}",
        phone=body.phone,
        password_hash=hash_password(body.password),
    )
    db.add(user)
    await db.flush()

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return resp_ok(data=TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    ).model_dump())


@router.post("/refresh", summary="刷新 Token")
async def refresh_token(body: RefreshTokenRequest, db: AsyncSession = Depends(get_db)):
    payload = decode_token(body.refresh_token)

    if payload is None or payload.get("type") != "refresh":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="无效的刷新令牌")

    user_id = int(payload.get("sub", 0))
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user or user.status != 1:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="用户不存在或已禁用")

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)

    return resp_ok(data=TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    ).model_dump())


@router.post("/logout", summary="退出登录")
async def logout():
    # TODO: 将 Token 加入 Redis 黑名单
    return resp_ok(message="退出成功")
