from fastapi import APIRouter

from app.api.v1 import (
    auth, user, property, notice, repair, feedback,
    bill, points, coupon, space, package, volunteer,
    activity, help_center, home, upload,
)

api_router = APIRouter()

# 认证
api_router.include_router(auth.router)

# 用户
api_router.include_router(user.router)

# 房产
api_router.include_router(property.router)

# 首页
api_router.include_router(home.router)

# 公告
api_router.include_router(notice.router)

# 报修
api_router.include_router(repair.router)

# 投诉建议
api_router.include_router(feedback.router)

# 缴费
api_router.include_router(bill.router)

# 积分
api_router.include_router(points.router)

# 优惠券
api_router.include_router(coupon.router)

# 公共空间预约
api_router.include_router(space.router)

# 快递包裹
api_router.include_router(package.router)

# 志愿服务
api_router.include_router(volunteer.router)

# 社区活动
api_router.include_router(activity.router)

# 帮助中心
api_router.include_router(help_center.router)

# 文件上传
api_router.include_router(upload.router)
