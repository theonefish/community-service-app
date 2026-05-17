<template>
	<view class="container">
		<!-- 顶部自定义导航栏 -->
		<view class="custom-nav">
			<view class="nav-left">
				<view class="grid-icon">
					<view class="grid-cell"></view>
					<view class="grid-cell"></view>
					<view class="grid-cell"></view>
					<view class="grid-cell"></view>
				</view>
			</view>
			<view class="nav-title">社区服务</view>
			<view class="nav-right" @click="goNotice">
				<view class="bell-icon">
					<view class="bell-body"></view>
					<view class="bell-clapper"></view>
					<view class="bell-dot"></view>
				</view>
			</view>
		</view>

		<!-- 轮播图区域 -->
		<view class="banner-section">
			<swiper class="banner-swiper" :indicator-dots="true" :autoplay="true" :interval="3000" :duration="500"
				indicator-color="rgba(255,255,255,0.5)" indicator-active-color="#ffffff">
				<swiper-item v-for="(item, index) in bannerList" :key="index" @click="onBannerClick(item)">
					<view class="banner-item" :style="{ background: item.bgColor }">
						<image class="banner-img" :src="item.image" mode="aspectFill"></image>
						<view class="banner-content">
							<view class="banner-tag">{{ item.tag }}</view>
							<view class="banner-title">{{ item.title }}</view>
							<view class="banner-desc">{{ item.desc }}</view>
						</view>
					</view>
				</swiper-item>
			</swiper>
		</view>

		<!-- 功能菜单区域 -->
		<view class="menu-section">
			<view class="menu-grid">
				<view class="menu-item" v-for="(item, index) in menuList" :key="index" @click="onMenuClick(item)">
					<view class="menu-icon" :style="{ backgroundColor: item.bgColor }">
						<text class="menu-iconfont">{{ item.icon }}</text>
					</view>
					<text class="menu-name">{{ item.name }}</text>
				</view>
			</view>
		</view>

		<!-- 社区推荐区域 -->
		<view class="recommend-section">
			<view class="section-header">
				<text class="section-title">社区推荐</text>
				<view class="section-more" @click="onMoreClick">
					<text> 查看全部 </text>
					<text class="arrow"></text>
				</view>
			</view>

			<!-- 推荐商家卡片 -->
			<view class="merchant-card">
				<view class="merchant-left">
					<view class="merchant-badge">精选商家</view>
					<view class="merchant-logo">
						<text class="logo-text">LOCAL</text>
						<text class="logo-sub">Service</text>
					</view>
				</view>
				<view class="merchant-right">
					<view class="merchant-name">隐溪禅意推拿馆</view>
					<view class="merchant-desc">新店入驻专属福利，业主凭认证截图立享首单五折优惠，舒缓疲劳好去处。</view>
					<view class="merchant-distance">
						<text class="location-icon">📍</text>
						<text>距您 300m</text>
					</view>
				</view>
			</view>

			<!-- 服务卡片列表 -->
			<view class="service-grid">
				<view class="service-card" v-for="(item, index) in serviceList" :key="index">
					<view class="service-icon" :style="{ backgroundColor: item.bgColor }">
						<text class="service-iconfont">{{ item.icon }}</text>
					</view>
					<view class="service-name">{{ item.name }}</view>
					<view class="service-desc">{{ item.desc }}</view>
				</view>
			</view>
		</view>
	</view>
	
	<!-- 自定义液态玻璃 tabBar -->
	<CustomTabBar :current="0" />
</template>

<script>
	import { homeApi } from '@/api/index.js'

	export default {
		data() {
			return {
				// 轮播图数据（从 API 获取）
				bannerList: [],
				// 功能菜单数据（从 API 获取）
				menuList: [],
				// 服务推荐数据（从 API 获取）
				serviceList: [],
				// 加载状态
				loading: true
			}
		},
		async onLoad() {
			await this.fetchHomeData()
		},
		methods: {
			// 从 API 获取首页数据
			async fetchHomeData() {
				try {
					this.loading = true
					const data = await homeApi.getHomeData()
					this.bannerList = data.banners || []
					this.menuList = data.menus || []
					this.serviceList = data.services || []
				} catch (err) {
					console.error('获取首页数据失败:', err)
				} finally {
					this.loading = false
				}
			},
			// 菜单点击事件 - 跳转到对应功能页面
			onMenuClick(item) {
				uni.navigateTo({
					url: item.path
				})
			},
			// 铃铛图标点击 - 跳转到社区公告页查看通知
			goNotice() {
				uni.navigateTo({
					url: '/pages/notice/notice'
				})
			},
			// 轮播图点击 - 根据banner的path跳转到对应页面
			onBannerClick(item) {
				uni.navigateTo({
					url: item.path
				})
			},
			// 查看全部 - 跳转到社区公告页
			onMoreClick() {
				uni.navigateTo({
					url: '/pages/notice/notice'
				})
			}
		}
	}
</script>

<style>
	/* 页面容器 */
	.container {
		background-color: #f5f7fa;
		min-height: 100vh;
		padding-bottom: 140rpx;
	}

	/* 自定义导航栏 */
	.custom-nav {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 20rpx 30rpx;
		background-color: #ffffff;
	}

	.nav-left {
		width: 60rpx;
	}

	/* 网格图标 */
	.grid-icon {
		display: grid;
		grid-template-columns: 1fr 1fr;
		grid-template-rows: 1fr 1fr;
		gap: 4rpx;
		width: 40rpx;
		height: 40rpx;
	}

	.grid-cell {
		background-color: #2c7a7b;
		border-radius: 2rpx;
	}

	.nav-title {
		font-size: 36rpx;
		font-weight: bold;
		color: #2c7a7b;
	}

	.nav-right {
		width: 60rpx;
		display: flex;
		justify-content: flex-end;
	}

	/* 铃铛图标 */
	.bell-icon {
		position: relative;
		width: 40rpx;
		height: 40rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.bell-body {
		width: 28rpx;
		height: 28rpx;
		border: 4rpx solid #2c7a7b;
		border-radius: 14rpx 14rpx 0 0;
		border-bottom: none;
		position: relative;
	}

	.bell-clapper {
		width: 8rpx;
		height: 8rpx;
		background-color: #2c7a7b;
		border-radius: 50%;
		margin-top: -2rpx;
	}

	.bell-dot {
		position: absolute;
		top: 0;
		right: 2rpx;
		width: 12rpx;
		height: 12rpx;
		background-color: #ff4444;
		border-radius: 50%;
	}

	/* 轮播图区域 */
	.banner-section {
		padding: 20rpx 30rpx;
	}

	.banner-swiper {
		height: 320rpx;
		border-radius: 20rpx;
		overflow: hidden;
	}

	.banner-item {
		position: relative;
		width: 100%;
		height: 100%;
		border-radius: 20rpx;
		overflow: hidden;
		background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
	}

	.banner-img {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		opacity: 0.3;
	}

	.banner-content {
		position: absolute;
		bottom: 0;
		left: 0;
		padding: 30rpx;
		z-index: 1;
	}

	.banner-tag {
		display: inline-block;
		background-color: rgba(44, 122, 123, 0.9);
		color: #ffffff;
		font-size: 22rpx;
		padding: 6rpx 16rpx;
		border-radius: 20rpx;
		margin-bottom: 16rpx;
	}

	.banner-title {
		color: #ffffff;
		font-size: 36rpx;
		font-weight: bold;
		margin-bottom: 10rpx;
	}

	.banner-desc {
		color: rgba(255, 255, 255, 0.9);
		font-size: 26rpx;
	}

	/* 功能菜单区域 */
	.menu-section {
		background-color: #ffffff;
		margin: 0 30rpx;
		border-radius: 20rpx;
		padding: 30rpx;
	}

	.menu-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 30rpx 20rpx;
	}

	.menu-item {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.menu-icon {
		width: 90rpx;
		height: 90rpx;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 16rpx;
	}

	.menu-iconfont {
		font-size: 44rpx;
	}

	.menu-name {
		font-size: 26rpx;
		color: #333333;
	}

	/* 社区推荐区域 */
	.recommend-section {
		margin: 20rpx 30rpx 0;
	}

	.section-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 20rpx;
	}

	.section-title {
		font-size: 34rpx;
		font-weight: bold;
		color: #333333;
	}

	.section-more {
		display: flex;
		align-items: center;
		color: #2c7a7b;
		font-size: 26rpx;
	}

	.arrow {
		margin-left: 8rpx;
		font-size: 28rpx;
	}

	/* 商家卡片 */
	.merchant-card {
		display: flex;
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 24rpx;
		margin-bottom: 20rpx;
	}

	.merchant-left {
		width: 180rpx;
		height: 180rpx;
		background-color: #1a1a2e;
		border-radius: 16rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		position: relative;
		margin-right: 24rpx;
		flex-shrink: 0;
	}

	.merchant-badge {
		position: absolute;
		top: 12rpx;
		left: 12rpx;
		background-color: #2c7a7b;
		color: #ffffff;
		font-size: 18rpx;
		padding: 4rpx 10rpx;
		border-radius: 8rpx;
	}

	.merchant-logo {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.logo-text {
		color: #ffffff;
		font-size: 32rpx;
		font-weight: bold;
		letter-spacing: 2rpx;
	}

	.logo-sub {
		color: #888888;
		font-size: 20rpx;
		margin-top: 8rpx;
		font-style: italic;
	}

	.merchant-right {
		flex: 1;
		display: flex;
		flex-direction: column;
		justify-content: center;
	}

	.merchant-name {
		font-size: 32rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 12rpx;
	}

	.merchant-desc {
		font-size: 24rpx;
		color: #666666;
		line-height: 1.6;
		margin-bottom: 16rpx;
	}

	.merchant-distance {
		display: flex;
		align-items: center;
		font-size: 24rpx;
		color: #2c7a7b;
	}

	.location-icon {
		margin-right: 6rpx;
	}

	/* 服务卡片网格 */
	.service-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 20rpx;
	}

	.service-card {
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 30rpx;
		display: flex;
		flex-direction: column;
	}

	.service-icon {
		width: 80rpx;
		height: 80rpx;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 16rpx;
	}

	.service-iconfont {
		font-size: 40rpx;
	}

	.service-name {
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 8rpx;
	}

	.service-desc {
		font-size: 24rpx;
		color: #999999;
	}
</style>
