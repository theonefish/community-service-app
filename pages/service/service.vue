<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="custom-nav">
			<view class="nav-left">
				<view class="grid-icon">
					<view class="grid-cell"></view>
					<view class="grid-cell"></view>
					<view class="grid-cell"></view>
					<view class="grid-cell"></view>
				</view>
			</view>
			<view class="nav-title">物业服务</view>
			<view class="nav-right" @click="goNotice">
				<view class="bell-icon">
					<view class="bell-body"></view>
					<view class="bell-clapper"></view>
					<view class="bell-dot"></view>
				</view>
			</view>
		</view>

		<!-- 联系物业卡片 -->
		<view class="contact-card">
			<view class="contact-left">
				<view class="contact-title">需要帮助？</view>
				<view class="contact-desc">您的专属管家全天候为您服务</view>
			</view>
			<view class="contact-btn" @click="callProperty">
				<text class="phone-icon">📞</text>
				<text class="btn-text">联系物业</text>
			</view>
		</view>

		<!-- 便捷服务 -->
		<view class="section">
			<view class="section-title">便捷服务</view>
			<view class="service-grid">
				<view class="service-item" v-for="(item, index) in serviceList" :key="index" @click="onServiceClick(item)">
					<view class="service-icon-wrap" :style="{ backgroundColor: item.bgColor }">
						<text class="service-iconfont">{{ item.icon }}</text>
					</view>
					<text class="service-name">{{ item.name }}</text>
				</view>
			</view>
		</view>

		<!-- 我的房产 -->
		<view class="section">
			<view class="property-card">
				<view class="property-header">
					<text class="property-title">我的房产</text>
					<view class="switch-link" @click="switchProperty">
						<text>切换房产</text>
					</view>
				</view>
				<view class="property-info">
					<image class="property-img" src="/static/property/house.png" mode="aspectFill"></image>
					<view class="property-detail">
						<view class="property-name">观澜锦苑 3栋 1204室</view>
						<view class="property-owner">张三（业主）</view>
					</view>
				</view>
				<view class="property-status">
					<view class="status-item" @click="goPayment">
						<view class="status-label">
							<text class="status-icon">📋</text>
							<text>物业费状态</text>
						</view>
						<view class="status-value">
							<text class="status-text paid">已缴清</text>
							<text class="status-date">至 2024-12</text>
						</view>
					</view>
					<view class="status-item" @click="goPayment">
						<view class="status-label">
							<text class="status-icon">🚗</text>
							<text>停车位</text>
						</view>
						<view class="status-value">
							<text class="parking-num">B2-108</text>
							<text class="parking-tag">正常</text>
						</view>
					</view>
				</view>
			</view>
		</view>

		<!-- 物业通知 -->
		<view class="section">
			<view class="section-header">
				<text class="section-title">物业通知</text>
				<view class="section-more" @click="viewAllNotice">
					<text>查看全部</text>
				</view>
			</view>
			<view class="notice-list">
				<view class="notice-item" v-for="(item, index) in noticeList" :key="index" @click="onNoticeClick(item)">
					<view class="notice-icon-wrap" :style="{ backgroundColor: item.bgColor }">
						<text class="notice-iconfont">{{ item.icon }}</text>
					</view>
					<view class="notice-content">
						<view class="notice-title">{{ item.title }}</view>
						<view class="notice-desc">{{ item.desc }}</view>
						<view class="notice-time">{{ item.time }}</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 便捷服务列表
				serviceList: [
					{ name: '报修申请', icon: '🔧', bgColor: '#e8f4f8', path: '/pages/repair-apply/repair-apply' },
					{ name: '缴费中心', icon: '💳', bgColor: '#e8f4f8', path: '/pages/payment/payment' },
					{ name: '投诉建议', icon: '📝', bgColor: '#e8f4f8', path: '/pages/feedback/feedback' },
					{ name: '公共空间预约', icon: '🏢', bgColor: '#e8f4f8', path: '/pages/booking/booking' }
				],
				// 物业通知列表
				noticeList: [
					{
						title: '停水通知：关于3栋高区水箱清洗的公告',
						desc: '尊敬的业主：为保证高区居民用水质量，物业服务中心计划于本周四（10月24日...',
						time: '2小时前',
						icon: '💧',
						bgColor: '#fce8e8'
					},
					{
						title: '电梯例行维保通知',
						desc: '本周五将对全区客梯进行月度例行维护保养，具体保养时间段已在各单元大堂电...',
						time: '昨天 10:30',
						icon: '🏢',
						bgColor: '#e8f4f8'
					}
				]
			}
		},
		methods: {
			// 联系物业
			callProperty() {
				uni.makePhoneCall({
					phoneNumber: '4001234567',
					fail: () => {
						uni.showToast({
							title: '拨打失败',
							icon: 'none'
						})
					}
				})
			},
			// 铃铛图标 - 跳转到社区公告页
			goNotice() {
				uni.navigateTo({
					url: '/pages/notice/notice'
				})
			},
			// 物业费/停车位状态 - 跳转到缴费中心
			goPayment() {
				uni.navigateTo({
					url: '/pages/payment/payment'
				})
			},
			// 服务点击
			onServiceClick(item) {
				uni.navigateTo({
					url: item.path
				})
			},
			// 切换房产
			switchProperty() {
				uni.showToast({
					title: '切换房产',
					icon: 'none'
				})
			},
			// 查看全部通知 - 跳转到社区公告页
			viewAllNotice() {
				uni.navigateTo({
					url: '/pages/notice/notice'
				})
			},
			// 通知点击 - 跳转到社区公告页
			onNoticeClick(item) {
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
		padding-bottom: 40rpx;
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

	/* 联系物业卡片 */
	.contact-card {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin: 20rpx 30rpx;
		background: linear-gradient(135deg, #4a8a8b 0%, #6ba8a9 100%);
		border-radius: 24rpx;
		padding: 40rpx;
	}

	.contact-left {
		flex: 1;
	}

	.contact-title {
		font-size: 36rpx;
		font-weight: bold;
		color: #ffffff;
		margin-bottom: 10rpx;
	}

	.contact-desc {
		font-size: 24rpx;
		color: rgba(255, 255, 255, 0.8);
	}

	.contact-btn {
		display: flex;
		align-items: center;
		background-color: #ffffff;
		border-radius: 40rpx;
		padding: 16rpx 32rpx;
	}

	.phone-icon {
		font-size: 32rpx;
		margin-right: 10rpx;
	}

	.btn-text {
		font-size: 26rpx;
		color: #2c7a7b;
		font-weight: bold;
	}

	/* 分区 */
	.section {
		margin: 20rpx 30rpx 0;
	}

	.section-title {
		font-size: 32rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 20rpx;
	}

	.section-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 20rpx;
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

	/* 便捷服务网格 */
	.service-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 20rpx;
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 30rpx;
	}

	.service-item {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.service-icon-wrap {
		width: 90rpx;
		height: 90rpx;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 16rpx;
	}

	.service-iconfont {
		font-size: 44rpx;
	}

	.service-name {
		font-size: 24rpx;
		color: #333333;
	}

	/* 房产卡片 */
	.property-card {
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 30rpx;
	}

	.property-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 24rpx;
	}

	.property-title {
		font-size: 32rpx;
		font-weight: bold;
		color: #333333;
	}

	.switch-link {
		display: flex;
		align-items: center;
		color: #2c7a7b;
		font-size: 26rpx;
	}

	.property-info {
		display: flex;
		align-items: center;
		margin-bottom: 24rpx;
		padding-bottom: 24rpx;
		border-bottom: 1rpx solid #f0f0f0;
	}

	.property-img {
		width: 100rpx;
		height: 100rpx;
		border-radius: 16rpx;
		background-color: #f0f0f0;
		margin-right: 20rpx;
	}

	.property-detail {
		flex: 1;
	}

	.property-name {
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 8rpx;
	}

	.property-owner {
		font-size: 24rpx;
		color: #999999;
	}

	/* 房产状态 */
	.property-status {
		display: flex;
		gap: 20rpx;
	}

	.status-item {
		flex: 1;
		background-color: #f5f7fa;
		border-radius: 16rpx;
		padding: 20rpx;
	}

	.status-label {
		display: flex;
		align-items: center;
		font-size: 24rpx;
		color: #666666;
		margin-bottom: 12rpx;
	}

	.status-icon {
		margin-right: 8rpx;
		font-size: 28rpx;
	}

	.status-value {
		display: flex;
		align-items: baseline;
		gap: 10rpx;
	}

	.status-text {
		font-size: 32rpx;
		font-weight: bold;
	}

	.status-text.paid {
		color: #2c7a7b;
	}

	.status-date {
		font-size: 22rpx;
		color: #999999;
	}

	.parking-num {
		font-size: 32rpx;
		font-weight: bold;
		color: #333333;
	}

	.parking-tag {
		font-size: 20rpx;
		color: #2c7a7b;
		background-color: #e8f4f8;
		padding: 4rpx 10rpx;
		border-radius: 6rpx;
	}

	/* 通知列表 */
	.notice-list {
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 0 24rpx;
	}

	.notice-item {
		display: flex;
		padding: 24rpx 0;
		border-bottom: 1rpx solid #f0f0f0;
	}

	.notice-item:last-child {
		border-bottom: none;
	}

	.notice-icon-wrap {
		width: 72rpx;
		height: 72rpx;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-right: 20rpx;
		flex-shrink: 0;
	}

	.notice-iconfont {
		font-size: 36rpx;
	}

	.notice-content {
		flex: 1;
	}

	.notice-title {
		font-size: 28rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 8rpx;
		line-height: 1.4;
	}

	.notice-desc {
		font-size: 24rpx;
		color: #666666;
		line-height: 1.5;
		margin-bottom: 8rpx;
	}

	.notice-time {
		font-size: 22rpx;
		color: #999999;
	}
</style>
