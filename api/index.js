/**
 * API 接口服务层
 * 统一管理所有后端接口调用，支持 mock/真实接口无缝切换
 *
 * 使用方式：
 *   import { homeApi, noticeApi, paymentApi } from '@/api/index.js'
 *   const banners = await homeApi.getBanners()
 *
 * 切换环境：
 *   修改 utils/request.js 中的 USE_MOCK 和 CURRENT_ENV
 */

import { get, post, put, del, USE_MOCK } from '../utils/request.js'
import {
	mockBanners, mockMenus, mockServices,
	mockNotices,
	mockPropertyServices, mockPropertyNotices,
	mockPendingBills, mockHistoryBills,
	mockPointsInfo, mockPointsHistory,
	mockActivities,
	mockVolunteerProjects,
	mockPackages,
	mockUserInfo,
	mockHelpCategories, mockHotQuestions,
	mockSpaces
} from '../utils/mock.js'

// 模拟网络延迟（让 mock 数据更有真实请求的感觉）
function delay(ms = 300) {
	return new Promise(resolve => setTimeout(resolve, ms))
}

// ==================== 首页 API ====================

export const homeApi = {
	/** 获取轮播图列表 */
	async getBanners() {
		if (USE_MOCK) { await delay(); return mockBanners }
		return get('/home/banners')
	},

	/** 获取功能菜单 */
	async getMenus() {
		if (USE_MOCK) { await delay(); return mockMenus }
		return get('/home/menus')
	},

	/** 获取服务推荐 */
	async getServices() {
		if (USE_MOCK) { await delay(); return mockServices }
		return get('/home/services')
	},

	/** 获取首页全部数据（合并请求减少请求次数） */
	async getHomeData() {
		if (USE_MOCK) {
			await delay()
			return {
				banners: mockBanners,
				menus: mockMenus,
				services: mockServices
			}
		}
		return get('/home/all')
	}
}

// ==================== 公告 API ====================

export const noticeApi = {
	/** 获取公告列表，category: all/important/activity */
	async getList(category = 'all') {
		if (USE_MOCK) {
			await delay()
			if (category === 'all') return mockNotices
			return mockNotices.filter(item => item.category === category)
		}
		return get('/notices', { category })
	},

	/** 获取公告详情 */
	async getDetail(id) {
		if (USE_MOCK) {
			await delay()
			return mockNotices.find(item => item.id === id) || null
		}
		return get(`/notices/${id}`)
	}
}

// ==================== 物业服务 API ====================

export const serviceApi = {
	/** 获取便捷服务列表 */
	async getServices() {
		if (USE_MOCK) { await delay(); return mockPropertyServices }
		return get('/property/services')
	},

	/** 获取物业通知 */
	async getNotices() {
		if (USE_MOCK) { await delay(); return mockPropertyNotices }
		return get('/property/notices')
	},

	/** 获取物业服务页全部数据 */
	async getServiceData() {
		if (USE_MOCK) {
			await delay()
			return {
				services: mockPropertyServices,
				notices: mockPropertyNotices
			}
		}
		return get('/property/all')
	}
}

// ==================== 缴费 API ====================

export const paymentApi = {
	/** 获取待缴账单 */
	async getPendingBills() {
		if (USE_MOCK) { await delay(); return mockPendingBills }
		return get('/payment/pending')
	},

	/** 获取历史账单 */
	async getHistoryBills() {
		if (USE_MOCK) { await delay(); return mockHistoryBills }
		return get('/payment/history')
	},

	/** 缴费支付 */
	async pay(billIds) {
		if (USE_MOCK) { await delay(500); return { success: true } }
		return post('/payment/pay', { billIds })
	}
}

// ==================== 积分 API ====================

export const pointsApi = {
	/** 获取积分信息 */
	async getPointsInfo() {
		if (USE_MOCK) { await delay(); return mockPointsInfo }
		return get('/points/info')
	},

	/** 获取积分明细 */
	async getHistory() {
		if (USE_MOCK) { await delay(); return mockPointsHistory }
		return get('/points/history')
	},

	/** 积分兑换 */
	async exchange(data) {
		if (USE_MOCK) { await delay(500); return { success: true, message: '兑换成功' } }
		return post('/points/exchange', data)
	}
}

// ==================== 社区活动 API ====================

export const activityApi = {
	/** 获取活动列表 */
	async getList(category = 'all') {
		if (USE_MOCK) {
			await delay()
			if (category === 'all') return mockActivities
			return mockActivities.filter(item => item.category === category)
		}
		return get('/activities', { category })
	},

	/** 报名活动 */
	async join(activityId) {
		if (USE_MOCK) { await delay(); return { success: true, message: '报名成功' } }
		return post('/activities/join', { activityId })
	}
}

// ==================== 志愿服务 API ====================

export const volunteerApi = {
	/** 获取志愿项目列表 */
	async getList(category = 'all') {
		if (USE_MOCK) {
			await delay()
			if (category === 'all') return mockVolunteerProjects
			return mockVolunteerProjects.filter(item => item.category === category)
		}
		return get('/volunteer/projects', { category })
	},

	/** 报名志愿项目 */
	async join(projectId) {
		if (USE_MOCK) { await delay(); return { success: true, message: '报名成功' } }
		return post('/volunteer/join', { projectId })
	}
}

// ==================== 快递 API ====================

export const expressApi = {
	/** 获取待领取包裹 */
	async getPending() {
		if (USE_MOCK) { await delay(); return mockPackages }
		return get('/express/pending')
	},

	/** 获取取件码 */
	async getPickupCode(packageId) {
		if (USE_MOCK) {
			await delay()
			return { code: String(Math.floor(100000 + Math.random() * 900000)) }
		}
		return post('/express/pickup-code', { packageId })
	}
}

// ==================== 用户 API ====================

export const userApi = {
	/** 获取用户信息 */
	async getProfile() {
		if (USE_MOCK) { await delay(); return mockUserInfo }
		return get('/user/profile')
	},

	/** 更新用户信息 */
	async updateProfile(data) {
		if (USE_MOCK) { await delay(); return { success: true } }
		return put('/user/profile', data)
	},

	/** 用户登录 */
	async login(data) {
		if (USE_MOCK) { await delay(); return { token: 'mock_token_xxx', user: mockUserInfo } }
		return post('/user/login', data)
	}
}

// ==================== 帮助中心 API ====================

export const helpApi = {
	/** 获取帮助分类 */
	async getCategories() {
		if (USE_MOCK) { await delay(); return mockHelpCategories }
		return get('/help/categories')
	},

	/** 获取热门问题 */
	async getHotQuestions() {
		if (USE_MOCK) { await delay(); return mockHotQuestions }
		return get('/help/hot-questions')
	}
}

// ==================== 预约 API ====================

export const bookingApi = {
	/** 获取可预约空间 */
	async getSpaces() {
		if (USE_MOCK) { await delay(); return mockSpaces }
		return get('/booking/spaces')
	},

	/** 提交预约 */
	async submit(data) {
		if (USE_MOCK) { await delay(500); return { success: true, message: '预约成功' } }
		return post('/booking/submit', data)
	}
}

// ==================== 报修 API ====================

export const repairApi = {
	/** 获取报修记录 */
	async getList() {
		if (USE_MOCK) { await delay(); return [] }
		return get('/repair/list')
	},

	/** 提交报修 */
	async submit(data) {
		if (USE_MOCK) { await delay(500); return { success: true, message: '提交成功' } }
		return post('/repair/submit', data)
	}
}

// ==================== 投诉建议 API ====================

export const feedbackApi = {
	/** 提交投诉建议 */
	async submit(data) {
		if (USE_MOCK) { await delay(500); return { success: true, message: '提交成功' } }
		return post('/feedback/submit', data)
	}
}

// 统一导出所有 API 模块
export default {
	home: homeApi,
	notice: noticeApi,
	service: serviceApi,
	payment: paymentApi,
	points: pointsApi,
	activity: activityApi,
	volunteer: volunteerApi,
	express: expressApi,
	user: userApi,
	help: helpApi,
	booking: bookingApi,
	repair: repairApi,
	feedback: feedbackApi
}