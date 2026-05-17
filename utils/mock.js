/**
 * Mock 数据层
 * 开发环境下返回本地硬编码数据，无需后端即可运行
 * 切换到生产环境时，只需将 USE_MOCK 设为 false，数据自动从后端获取
 */

// ==================== 首页数据 ====================

/** 轮播图 */
export const mockBanners = [
	{
		id: 1,
		tag: '最新动态',
		title: '春季社区绿化升级工程正式启动',
		desc: '共同打造更宜居、更美丽的绿色生态家园。',
		image: '/static/banner/banner1.jpg',
		bgColor: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
		path: '/pages/notice/notice'
	},
	{
		id: 2,
		tag: '社区活动',
		title: '周末亲子运动会报名开始',
		desc: '增进邻里感情，共享欢乐时光。',
		image: '/static/banner/banner2.jpg',
		bgColor: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
		path: '/pages/activity/activity'
	},
	{
		id: 3,
		tag: '通知公告',
		title: '电梯维护保养通知',
		desc: '本周三进行电梯例行保养，请留意。',
		image: '/static/banner/banner3.jpg',
		bgColor: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
		path: '/pages/notice/notice'
	}
]

/** 功能菜单 */
export const mockMenus = [
	{ id: 1, name: '社区公告', icon: '📢', bgColor: '#e8f4f8', path: '/pages/notice/notice' },
	{ id: 2, name: '报修申请', icon: '🔧', bgColor: '#e8f4f8', path: '/pages/repair-apply/repair-apply' },
	{ id: 3, name: '缴费中心', icon: '💳', bgColor: '#e8f4f8', path: '/pages/payment/payment' },
	{ id: 4, name: '社区活动', icon: '🎉', bgColor: '#e8f4f8', path: '/pages/activity/activity' },
	{ id: 5, name: '快递代收', icon: '🚚', bgColor: '#e8f4f8', path: '/pages/express/express' },
	{ id: 6, name: '邻里交流', icon: '💬', bgColor: '#e8f4f8', path: '/pages/help/help' },
	{ id: 7, name: '物业管家', icon: '🎧', bgColor: '#e8f4f8', path: '/pages/service/service' },
	{ id: 8, name: '志愿服务', icon: '🤝', bgColor: '#e8f4f8', path: '/pages/volunteer/volunteer' }
]

/** 服务推荐 */
export const mockServices = [
	{ id: 1, name: '深度保洁', desc: '专业团队上门服务', icon: '🧹', bgColor: '#e8e0f0' },
	{ id: 2, name: '家庭医生', desc: '在线问诊及健康档案', icon: '⚕️', bgColor: '#e0e8f0' }
]

// ==================== 公告数据 ====================

export const mockNotices = [
	{
		id: 1,
		tag: '通知',
		tagClass: 'tag-notice',
		date: '2025/10/21',
		title: '停水通知：A区水管网例行检修',
		desc: '接自来水公司通知，因例行管网维护检修，本社区住宅楼将于本周三下午14:00至18:00暂停供水，请大家提前做好储水准备。',
		link: '阅读更多',
		image: '/static/notice/water.jpg',
		category: 'important'
	},
	{
		id: 2,
		tag: '活动',
		tagClass: 'tag-activity',
		date: '2025/10/18',
		title: '秋季社区文化节圆满落幕',
		desc: '感谢各位居民的积极参与！本次社区文化节吸引了超过500个家庭参与，各类文艺汇演和互动游戏活动均获得圆满成功，期待来年再聚。',
		link: '查看照片',
		image: '/static/notice/event.jpg',
		imageOverlay: true,
		category: 'activity'
	},
	{
		id: 3,
		tag: '通知',
		tagClass: 'tag-notice',
		date: '2025/10/15',
		title: '关于启用全新智能门禁系统的说明',
		desc: '为了进一步提升小区的安全管理水平，物业服务中心已全面完成人脸识别智能门禁系统升级，请各位业主及时前往物业办公室进行人脸信息录入，以便正常使用。',
		link: '阅读详细说明',
		category: 'important'
	},
	{
		id: 4,
		tag: '活动',
		tagClass: 'tag-activity',
		date: '2025/10/10',
		title: '垃圾分类积分兑换活动即将开始',
		desc: '本社区垃圾分类积分兑换活动将于本周五在小区中心广场举行，欢迎广大居民参与兑换各类生活用品。',
		link: '查看详情',
		image: '/static/notice/recycle.jpg',
		category: 'activity'
	}
]

// ==================== 物业服务数据 ====================

export const mockPropertyServices = [
	{ id: 1, name: '报修申请', icon: '🔧', bgColor: '#e8f4f8', path: '/pages/repair-apply/repair-apply' },
	{ id: 2, name: '缴费中心', icon: '💳', bgColor: '#e8f4f8', path: '/pages/payment/payment' },
	{ id: 3, name: '投诉建议', icon: '📝', bgColor: '#e8f4f8', path: '/pages/feedback/feedback' },
	{ id: 4, name: '公共空间预约', icon: '🏢', bgColor: '#e8f4f8', path: '/pages/booking/booking' }
]

export const mockPropertyNotices = [
	{
		id: 1,
		title: '停水通知：关于3栋高区水箱清洗的公告',
		desc: '尊敬的业主：为保证高区居民用水质量，物业服务中心计划于本周四（10月24日...',
		time: '2小时前',
		icon: '💧',
		bgColor: '#fce8e8'
	},
	{
		id: 2,
		title: '电梯例行维保通知',
		desc: '本周五将对全区客梯进行月度例行维护保养，具体保养时间段已在各单元大堂电...',
		time: '昨天 10:30',
		icon: '🏢',
		bgColor: '#e8f4f8'
	}
]

// ==================== 缴费数据 ====================

export const mockPendingBills = [
	{
		id: 1,
		name: '物业管理费',
		date: '2023年10月',
		amount: '850.00',
		detail: '住宅面积120㎡, 单价7.08元/㎡',
		icon: '🏢',
		bgColor: '#e8f4f8'
	},
	{
		id: 2,
		name: '停车费',
		date: '2023年10月',
		amount: '300.00',
		detail: '车位号 B2-105, 包月费用',
		icon: '🚗',
		bgColor: '#e8e0f0'
	},
	{
		id: 3,
		name: '水电公摊费',
		date: '2023年9月结算',
		amount: '130.50',
		detail: '公摊水费: ¥45.20    公摊电费: ¥85.30',
		icon: '⚡',
		bgColor: '#f0f0e8'
	}
]

export const mockHistoryBills = [
	{
		id: 1,
		name: '2023年9月综合账单',
		time: '2023-09-05 14:20',
		amount: '1,250.00',
		status: '已支付'
	},
	{
		id: 2,
		name: '2023年8月综合账单',
		time: '2023-08-02 09:15',
		amount: '1,250.00',
		status: '已支付'
	}
]

// ==================== 积分数据 ====================

export const mockPointsInfo = {
	balance: 12850,
	unit: '积分'
}

export const mockPointsHistory = [
	{
		id: 1,
		title: '社区公益活动奖励',
		date: '2023年10月24日',
		desc: '垃圾分类宣传',
		value: 500,
		icon: '🌱',
		bgColor: '#e8f4f8'
	},
	{
		id: 2,
		title: '物业费缴纳成功',
		date: '2023年10月20日',
		desc: '线上自动缴费',
		value: 200,
		icon: '🏠',
		bgColor: '#e8f4f8'
	},
	{
		id: 3,
		title: '兑换超市代金券',
		date: '2023年10月15日',
		desc: '50元无门槛',
		value: -1000,
		icon: '🎫',
		bgColor: '#fce8e8'
	}
]

// ==================== 活动数据 ====================

export const mockActivities = [
	{
		id: 1,
		title: '晨间公园瑜伽',
		date: '4月16日 08:00 - 09:00',
		location: '中央草坪',
		image: '/static/activity/yoga.jpg',
		category: 'health',
		isFull: false
	},
	{
		id: 2,
		title: '社区环保讲座：城市阳台种植',
		date: '4月20日 19:30 - 20:30',
		location: '图书馆多功能厅',
		image: '/static/activity/lecture.jpg',
		category: 'art',
		status: '限报30人/已报28人',
		isFull: false
	},
	{
		id: 3,
		title: '儿童绘本阅读与手作分享会',
		date: '4月25日 10:00 - 11:30',
		location: '社区活动中心儿童区',
		image: '/static/activity/reading.jpg',
		category: 'family',
		status: '限报15组家庭',
		isFull: true
	}
]

// ==================== 志愿服务数据 ====================

export const mockVolunteerProjects = [
	{
		id: 1,
		title: '周末中央公园清洁行动',
		desc: '协助社区维护中央公园的环境卫生。工作内容包括清理散落的垃圾、修剪低矮灌木以及向游客宣传环保知识。无需经验，提供必需工具和饮用水。',
		date: '本周六 09:00-12:00',
		registered: 12,
		total: 20,
		category: 'environment',
		tag: '环境保护',
		status: 'recruiting',
		image: '/static/volunteer/park.jpg',
		type: 'featured'
	},
	{
		id: 2,
		title: '独居老人定期探访',
		desc: '每周定期探访社区内的独居老人，陪伴聊天、代购生活用品、协助使用智能设备。',
		date: '每周二/四 14:00-16:00',
		registered: 8,
		total: 15,
		category: 'elderly',
		tag: '助老关怀',
		status: 'recruiting',
		type: 'compact'
	}
]

// ==================== 快递数据 ====================

export const mockPackages = [
	{
		id: 1,
		name: '顺丰速运包裹',
		time: '2025/10/22 09:30',
		tracking: 'SF1234567890',
		tag: '待领取',
		tagClass: 'tag-pending'
	},
	{
		id: 2,
		name: '京东快递包裹',
		time: '2025/10/21 16:45',
		tracking: 'JD9876543210',
		tag: '即将过期',
		tagClass: 'tag-expiring'
	}
]

// ==================== 用户数据 ====================

export const mockUserInfo = {
	id: 1,
	nickname: '张先生',
	avatar: '/static/avatar/default.png',
	phone: '138****8888',
	room: '3栋1201室',
	propertyName: '光耀智慧社区',
	memberLevel: 'VIP会员',
	points: 12850
}

// ==================== 帮助中心数据 ====================

export const mockHelpCategories = [
	{ id: 1, name: '账户相关', icon: '👤', count: 8 },
	{ id: 2, name: '物业服务', icon: '🏠', count: 12 },
	{ id: 3, name: '缴费问题', icon: '💳', count: 6 },
	{ id: 4, name: '报修指南', icon: '🔧', count: 5 }
]

export const mockHotQuestions = [
	{ id: 1, title: '如何修改绑定的手机号码？', category: '账户相关' },
	{ id: 2, title: '物业费包含哪些项目？', category: '缴费问题' },
	{ id: 3, title: '报修后多久能上门维修？', category: '报修指南' },
	{ id: 4, title: '如何申请停车位？', category: '物业服务' }
]

// ==================== 预约数据 ====================

export const mockSpaces = [
	{
		id: 1,
		name: '多功能会议室',
		desc: '可容纳20人，配备投影仪和白板',
		icon: '🏢',
		image: '/static/booking/meeting.jpg',
		tags: ['投影仪', '白板', 'WiFi']
	},
	{
		id: 2,
		name: '健身房',
		desc: '配备跑步机、哑铃等基础器械',
		icon: '🏋️',
		image: '/static/booking/gym.jpg',
		tags: ['跑步机', '哑铃', '更衣室']
	},
	{
		id: 3,
		name: '网球场',
		desc: '标准室外网球场，需自备球拍',
		icon: '🎾',
		image: '/static/booking/tennis.jpg',
		tags: ['室外', '标准场地', '夜间照明']
	}
]

// ==================== 统一导出 ====================

export default {
	banners: mockBanners,
	menus: mockMenus,
	services: mockServices,
	notices: mockNotices,
	propertyServices: mockPropertyServices,
	propertyNotices: mockPropertyNotices,
	pendingBills: mockPendingBills,
	historyBills: mockHistoryBills,
	pointsInfo: mockPointsInfo,
	pointsHistory: mockPointsHistory,
	activities: mockActivities,
	volunteerProjects: mockVolunteerProjects,
	packages: mockPackages,
	userInfo: mockUserInfo,
	helpCategories: mockHelpCategories,
	hotQuestions: mockHotQuestions,
	spaces: mockSpaces
}