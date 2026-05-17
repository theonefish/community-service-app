"""初始化数据脚本

运行方式: python -m scripts.init_data
"""
import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import select
from app.database import async_session, engine, Base
from app.models import *
from app.utils.security import hash_password


async def init():
    # 创建所有表
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        # 检查是否已有数据
        result = await session.execute(select(User).limit(1))
        if result.scalar_one_or_none():
            print("数据已存在，跳过初始化")
            return

        # 创建测试用户
        user = User(
            uid="88294105",
            name="测试用户",
            phone="13800009920",
            password_hash=hash_password("123456"),
            is_verified=True,
        )
        session.add(user)
        await session.flush()

        # 用户标签
        tags = [
            UserTag(user_id=user.id, icon="verified", text="实名用户"),
            UserTag(user_id=user.id, icon="star", text="金牌邻里"),
        ]
        session.add_all(tags)

        # 积分账户
        account = PointsAccount(user_id=user.id, balance=200, total_earned=500, total_spent=300)
        session.add(account)

        # 社区楼栋
        buildings = [
            CommunityBuilding(area="A区", building="1栋", sort=1),
            CommunityBuilding(area="A区", building="2栋", sort=2),
            CommunityBuilding(area="B区", building="1栋", sort=3),
            CommunityBuilding(area="C区", building="1栋", sort=4),
        ]
        session.add_all(buildings)

        # 房产
        prop = Property(
            user_id=user.id,
            community_name="观澜锦苑",
            building="3栋",
            room="1204室",
            owner_name="张先生",
            owner_role="owner",
            property_fee_status="paid",
            property_fee_until="2024-12",
            parking_space="B2-108",
            parking_status="normal",
            is_current=True,
        )
        session.add(prop)
        await session.flush()

        # 轮播图
        banners = [
            Banner(tag="最新动态", title="社区新风貌", desc="观澜锦苑社区焕然一新", image="/static/banner1.jpg", bg_color="linear-gradient(135deg, #2c7a7b, #38b2ac)", sort=1),
            Banner(tag="社区活动", title="邻里运动会", desc="一起来参加我们的社区运动会", image="/static/banner2.jpg", bg_color="linear-gradient(135deg, #6b46c1, #9f7aea)", sort=2),
        ]
        session.add_all(banners)

        # 功能菜单
        menus = [
            Menu(name="物业报修", icon="repair", bg_color="#2c7a7b", path="/pages/repair/repair", sort=1),
            Menu(name="投诉建议", icon="feedback", bg_color="#e53e3e", path="/pages/feedback/feedback", sort=2),
            Menu(name="缴费中心", icon="payment", bg_color="#dd6b20", path="/pages/payment/payment", sort=3),
            Menu(name="社区公告", icon="notice", bg_color="#3182ce", path="/pages/notice/notice", sort=4),
            Menu(name="快递包裹", icon="express", bg_color="#38a169", path="/pages/express/express", sort=5),
            Menu(name="公共空间", icon="booking", bg_color="#805ad5", path="/pages/booking/booking", sort=6),
            Menu(name="社区活动", icon="activity", bg_color="#d53f8c", path="/pages/activity/activity", sort=7),
            Menu(name="志愿服务", icon="volunteer", bg_color="#d69e2e", path="/pages/volunteer/volunteer", sort=8),
        ]
        session.add_all(menus)

        # 公告
        notices = [
            Notice(title="关于社区电梯维护的通知", desc="3栋电梯将于本周六进行年度检修", content="详细内容...", tag="通知", category="important", is_published=True, published_at=datetime.now(), sort=1),
            Notice(title="社区春季运动会即将举办", desc="欢迎各位业主积极参加", content="详细内容...", tag="活动", category="activity", is_published=True, published_at=datetime.now(), sort=2),
        ]
        session.add_all(notices)

        # 公共空间
        spaces = [
            Space(name="健身中心", desc="社区健身中心，配备专业器械", price="免费使用", capacity="限10人", icon="fitness"),
            Space(name="共享会议室", desc="社区共享会议室，需提前预约", price="20点/小时", capacity="限8人", icon="meeting"),
            Space(name="网球场", desc="标准网球场，需预约使用", price="10点/小时", capacity="限4人", icon="tennis"),
        ]
        session.add_all(spaces)

        # 志愿项目
        volunteer_projects = [
            VolunteerProject(title="关爱老人送温暖", desc="为社区独居老人提供生活帮助", category="elderly", status="recruiting", date_time="每周六上午", location="社区活动中心", current_count=5, max_count=20, duration="2小时/次"),
            VolunteerProject(title="社区环境清洁日", desc="每月一次社区环境清洁志愿活动", category="environment", status="recruiting", date_time="每月第一个周日", location="社区各区域", current_count=12, max_count=30, duration="3小时/次"),
        ]
        session.add_all(volunteer_projects)

        # 社区活动
        activities = [
            Activity(title="春季邻里运动会", desc="社区年度运动会，包含多种趣味竞赛", category="health", date_time="2024年4月20日 9:00-17:00", location="社区运动场", max_participants=30, current_participants=28, is_full=False, tag="本周末"),
            Activity(title="亲子绘画工坊", desc="家庭亲子绘画体验活动", category="family", date_time="2024年4月21日 14:00-16:00", location="社区活动中心", max_participants=20, current_participants=20, is_full=True, tag="已满"),
        ]
        session.add_all(activities)

        # 帮助分类
        help_cats = [
            HelpCategory(name="物业报修", desc="房屋维修相关问题", icon="repair", bg_color="#2c7a7b", path="/pages/repair/repair", sort=1),
            HelpCategory(name="停车服务", desc="停车位相关问题", icon="parking", bg_color="#dd6b20", path="", sort=2),
            HelpCategory(name="社区活动", desc="活动报名相关问题", icon="activity", bg_color="#d53f8c", path="/pages/activity/activity", sort=3),
            HelpCategory(name="App 使用", desc="应用操作相关问题", icon="app", bg_color="#3182ce", path="", sort=4),
        ]
        session.add_all(help_cats)

        # FAQ
        faqs = [
            FAQ(question="如何提交报修申请？", answer="进入物业报修页面，选择报修类型，填写问题描述后提交即可。", category="物业报修", is_hot=True, sort=1),
            FAQ(question="报修后多久能处理？", answer="我们会在24小时内安排维修人员与您联系。", category="物业报修", is_hot=True, sort=2),
            FAQ(question="如何预约公共空间？", answer="进入公共空间预约页面，选择空间、日期和时段后确认预约。", category="App 使用", is_hot=True, sort=3),
            FAQ(question="积分有什么用？", answer="积分可用于预约公共空间、兑换优惠券等。", category="App 使用", sort=4),
        ]
        session.add_all(faqs)

        # 快递室信息
        session.add(ExpressRoomInfo(weekday_hours="08:00-21:00", weekend_hours="09:00-18:00"))

        # 物业通知
        property_notices = [
            PropertyNotice(title="3栋电梯年度检修", desc="本周六8:00-18:00", icon="wrench", bg_color="#dd6b20", sort=1),
            PropertyNotice(title="物业费缴纳提醒", desc="请及时缴纳本月物业费", icon="bill", bg_color="#3182ce", sort=2),
        ]
        session.add_all(property_notices)

        await session.commit()

    print("初始化数据完成！")
    print("测试用户: 13800009920 / 123456")


if __name__ == "__main__":
    from datetime import datetime
    asyncio.run(init())
