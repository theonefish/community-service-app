<template>
	<view class="tab-bar-wrap" v-if="showTabBar">
		<view class="tab-bar" :style="{ paddingBottom: safeAreaBottom + 'px' }">
			<!-- 液态玻璃背景层 -->
			<view class="glass-bg"></view>
			<view class="glass-blur"></view>
			
			<!-- 顶部高光线条 -->
			<view class="glass-highlight"></view>
			
			<!-- tab 项 -->
			<view 
				class="tab-item" 
				v-for="(item, index) in tabList" 
				:key="index"
				@click="switchTab(item, index)"
			>
				<view class="tab-icon-wrap">
					<image 
						class="tab-icon" 
						:src="currentIndex === index ? item.selectedIconPath : item.iconPath" 
						mode="aspectFit"
					/>
				</view>
				<text class="tab-text" :class="{ active: currentIndex === index }">
					{{ item.text }}
				</text>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	name: 'CustomTabBar',
	props: {
		current: {
			type: Number,
			default: 0
		}
	},
	data() {
		return {
			currentIndex: 0,
			safeAreaBottom: 0,
			tabList: [
				{
					pagePath: '/pages/index/index',
					text: '首页',
					iconPath: '/static/tabbar/home.png',
					selectedIconPath: '/static/tabbar/home-active.png'
				},
				{
					pagePath: '/pages/service/service',
					text: '物业服务',
					iconPath: '/static/tabbar/service.png',
					selectedIconPath: '/static/tabbar/service-active.png'
				},
				{
					pagePath: '/pages/profile/profile',
					text: '个人中心',
					iconPath: '/static/tabbar/user.png',
					selectedIconPath: '/static/tabbar/user-active.png'
				}
			]
		}
	},
	computed: {
		showTabBar() {
			// 只在 tab 页面显示
			const tabPages = ['/pages/index/index', '/pages/service/service', '/pages/profile/profile']
			const currentPage = getCurrentPages()[getCurrentPages().length - 1]
			if (!currentPage) return false
			const route = '/' + currentPage.route
			return tabPages.includes(route)
		}
	},
	watch: {
		current: {
			immediate: true,
			handler(val) {
				this.currentIndex = val
			}
		}
	},
	created() {
		// 获取安全区域底部高度
		const systemInfo = uni.getSystemInfoSync()
		this.safeAreaBottom = systemInfo.safeAreaInsets?.bottom || 0
	},
	methods: {
		switchTab(item, index) {
			if (this.currentIndex === index) return
			
			this.currentIndex = index
			uni.switchTab({
				url: item.pagePath
			})
		}
	}
}
</script>

<style scoped>
/* 底部导航栏外层 - 固定在底部 */
.tab-bar-wrap {
	position: fixed;
	bottom: 0;
	left: 0;
	right: 0;
	z-index: 999;
	padding: 0 20rpx 20rpx;
}

/* 底部导航栏容器 */
.tab-bar {
	position: relative;
	height: 100rpx;
	display: flex;
	flex-direction: row;
	justify-content: space-around;
	align-items: center;
	border-radius: 40rpx;
	overflow: hidden;
}

/* 液态玻璃背景层 - 提高透明度 */
.glass-bg {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background: rgba(255, 255, 255, 0.55);
	border-radius: 40rpx;
	z-index: -2;
}

/* 模糊层 - 降低模糊度 */
.glass-blur {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	backdrop-filter: blur(15px) saturate(180%);
	-webkit-backdrop-filter: blur(15px) saturate(180%);
	border-radius: 40rpx;
	z-index: -1;
}

/* 顶部高光线条 - 强烈玻璃反光 */
.glass-highlight {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	height: 3px;
	background: linear-gradient(
		90deg,
		transparent 0%,
		rgba(255, 255, 255, 0.9) 20%,
		rgba(255, 255, 255, 1) 50%,
		rgba(255, 255, 255, 0.9) 80%,
		transparent 100%
	);
	border-radius: 2px;
	z-index: 1;
}

/* 底部内阴影 - 增加玻璃厚度感 */
.tab-bar::after {
	content: '';
	position: absolute;
	bottom: 0;
	left: 0;
	right: 0;
	height: 50%;
	background: linear-gradient(
		to top,
		rgba(0, 0, 0, 0.08) 0%,
		transparent 100%
	);
	border-radius: 0 0 40rpx 40rpx;
	z-index: -1;
	pointer-events: none;
}

/* 外边框 - 玻璃边缘发光 */
.tab-bar::before {
	content: '';
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	border-radius: 40rpx;
	border: 2px solid rgba(255, 255, 255, 0.6);
	box-shadow: 
		0 0 20rpx rgba(255, 255, 255, 0.4),
		0 0 40rpx rgba(255, 255, 255, 0.2),
		inset 0 0 20rpx rgba(255, 255, 255, 0.3);
	z-index: 0;
	pointer-events: none;
}

/* tab 项 */
.tab-item {
	flex: 1;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	height: 100%;
	position: relative;
	z-index: 2;
}

/* 图标容器 */
.tab-icon-wrap {
	width: 60rpx;
	height: 60rpx;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-bottom: 6rpx;
}

.tab-icon {
	width: 52rpx;
	height: 52rpx;
}

/* 文字 */
.tab-text {
	font-size: 20rpx;
	color: rgba(120, 120, 120, 0.8);
	transition: all 0.3s ease;
}

.tab-text.active {
	color: #2c7a7b;
	font-weight: 600;
}

/* 选中态图标放大效果 */
.tab-item:active .tab-icon-wrap {
	transform: scale(0.9);
}
</style>