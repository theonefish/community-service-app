<script>
	export default {
		onLaunch: function() {
			// 应用初始化逻辑
			this.initApp()
		},
		onShow: function() {
			// 应用从后台回到前台
		},
		onHide: function() {
			// 应用进入后台
		},
		methods: {
			initApp() {
				// #ifdef MP-WEIXIN
				// 获取系统信息并缓存
				try {
					const sysInfo = uni.getSystemInfoSync()
					uni.setStorageSync('systemInfo', sysInfo)
				} catch(e) {}
				// #endif
			}
		}
	}
</script>

<style>
	/* 每个页面公共 CSS */
	page {
		background-color: #f5f5f5;
		font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, 'PingFang SC', 'Microsoft YaHei', sans-serif;
	}

	/* 全局按钮统一样式 */
	.primary-btn {
		background: linear-gradient(135deg, #2c7a7b, #38a169);
		color: #fff;
		border: none;
		border-radius: 24px;
		padding: 12px 0;
		font-size: 16px;
		font-weight: 600;
		text-align: center;
		transition: opacity 0.2s;
	}

	.primary-btn:active {
		opacity: 0.85;
	}

	/* 卡片统一样式 */
	.card {
		background: #fff;
		border-radius: 12px;
		padding: 16px;
		margin: 12px 16px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
	}

	/* 分隔线 */
	.divider {
		height: 1px;
		background: #f0f0f0;
		margin: 12px 0;
	}

	/* 空状态容器（页内使用） */
	.page-container {
		min-height: 100vh;
	}
</style>
