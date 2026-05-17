/**
 * HTTP 请求工具封装（增强版）
 * 统一处理：token 鉴权、请求/响应拦截、错误处理、loading 状态、环境切换
 */

// 环境配置：开发环境用 mock，生产环境用真实接口
const ENV = {
	DEV: 'dev',
	PROD: 'prod'
}

const CURRENT_ENV = ENV.DEV // 切换环境：ENV.DEV 或 ENV.PROD

// 后端接口基础地址
const API_BASE = {
	[ENV.DEV]: 'http://localhost:3000/api',  // 本地开发后端
	[ENV.PROD]: 'https://api.community.com/api' // 生产环境
}

const BASE_URL = API_BASE[CURRENT_ENV]

// 是否启用 mock 模式（开发时返回本地硬编码数据，不请求后端）
const USE_MOCK = true

/**
 * 获取本地存储的 token
 */
function getToken() {
	try {
		return uni.getStorageSync('token') || ''
	} catch (e) {
		return ''
	}
}

/**
 * 保存 token
 */
function setToken(token) {
	try {
		uni.setStorageSync('token', token)
	} catch (e) {}
}

/**
 * 清除 token（退出登录时调用）
 */
function clearToken() {
	try {
		uni.removeStorageSync('token')
	} catch (e) {}
}

/**
 * 核心请求方法
 * @param {string} url - 接口路径（相对路径，如 /user/profile）
 * @param {object} options - 请求配置
 * @param {string} options.method - 请求方法 GET/POST/PUT/DELETE
 * @param {object} options.data - 请求参数
 * @param {boolean} options.showLoading - 是否显示加载中
 * @param {string} options.loadingText - 加载提示文字
 * @param {boolean} options.showError - 是否显示错误提示
 * @param {boolean} options.skipAuth - 是否跳过 token 校验
 */
function request(url, options = {}) {
	const {
		method = 'GET',
		data = {},
		showLoading = false,
		loadingText = '加载中...',
		showError = true,
		skipAuth = false
	} = options

	return new Promise((resolve, reject) => {
		if (showLoading) {
			uni.showLoading({ title: loadingText, mask: true })
		}

		// 构建请求头
		const header = {
			'Content-Type': 'application/json'
		}

		// 非免鉴权接口，自动带上 token
		if (!skipAuth) {
			const token = getToken()
			if (token) {
				header['Authorization'] = `Bearer ${token}`
			}
		}

		uni.request({
			url: url.startsWith('http') ? url : BASE_URL + url,
			method,
			data,
			header,
			success: (res) => {
				const { statusCode, data: resData } = res

				// 根据后端约定的返回格式处理
				// 假设后端返回格式：{ code: 0, data: {...}, message: 'ok' }
				if (statusCode === 200) {
					if (resData.code === 0) {
						resolve(resData.data)
					} else if (resData.code === 401) {
						// token 过期，清除并跳转登录
						clearToken()
						uni.showToast({ title: '登录已过期，请重新登录', icon: 'none' })
						// 跳转到登录页（如果有的话）
						// uni.reLaunch({ url: '/pages/login/login' })
						reject(new Error('登录已过期'))
					} else {
						handleError(resData.message || '请求失败', showError)
						reject(resData)
					}
				} else if (statusCode === 401) {
					clearToken()
					uni.showToast({ title: '登录已过期，请重新登录', icon: 'none' })
					reject(new Error('登录已过期'))
				} else {
					handleError(resData?.message || `请求失败(${statusCode})`, showError)
					reject(res)
				}
			},
			fail: (err) => {
				handleError('网络异常，请检查网络连接', showError)
				reject(err)
			},
			complete: () => {
				if (showLoading) {
					uni.hideLoading()
				}
			}
		})
	})
}

/**
 * 统一错误提示
 */
function handleError(msg, show) {
	if (show) {
		uni.showToast({ title: msg, icon: 'none', duration: 2500 })
	}
}

// 快捷方法
export const get = (url, data, opts) => request(url, { ...opts, method: 'GET', data })
export const post = (url, data, opts) => request(url, { ...opts, method: 'POST', data })
export const put = (url, data, opts) => request(url, { ...opts, method: 'PUT', data })
export const del = (url, data, opts) => request(url, { ...opts, method: 'DELETE', data })

export { getToken, setToken, clearToken, USE_MOCK, CURRENT_ENV, ENV }

export default { get, post, put, del, getToken, setToken, clearToken }