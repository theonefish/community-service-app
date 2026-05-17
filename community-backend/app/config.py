from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """应用配置"""

    # 应用
    APP_NAME: str = "智慧社区服务"
    APP_ENV: str = "development"
    DEBUG: bool = True

    # 安全
    SECRET_KEY: str = "dev-secret-key-do-not-use-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"

    # 数据库
    DATABASE_URL: str = "mysql+aiomysql://root:password@localhost:3306/community_db"
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # 文件上传
    UPLOAD_DIR: str = "./uploads"
    MAX_UPLOAD_SIZE_MB: int = 5
    ALLOWED_EXTENSIONS: str = "jpg,jpeg,png,webp"

    # 微信小程序
    WECHAT_APPID: str = ""
    WECHAT_SECRET: str = ""

    model_config = {"env_file": ".env", "case_sensitive": True}


settings = Settings()
