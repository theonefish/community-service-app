"""创建管理员脚本

运行方式: python -m scripts.create_admin
"""
import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import select
from app.database import async_session
from app.models.user import User
from app.utils.security import hash_password


async def create_admin():
    phone = input("请输入管理员手机号: ").strip()
    password = input("请输入密码: ").strip()
    name = input("请输入用户名 (回车使用默认): ").strip() or "管理员"

    async with async_session() as session:
        result = await session.execute(select(User).where(User.phone == phone))
        if result.scalar_one_or_none():
            print("该手机号已存在！")
            return

        import random
        uid = str(random.randint(10000000, 99999999))

        admin = User(
            uid=uid,
            name=name,
            phone=phone,
            password_hash=hash_password(password),
            is_verified=True,
        )
        session.add(admin)
        await session.commit()

        print(f"管理员创建成功！UID: {uid}")


if __name__ == "__main__":
    asyncio.run(create_admin())
