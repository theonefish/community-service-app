<template>
	<view class="container">
		<!-- 自定义导航栏 -->
		<view class="custom-nav">
			<view class="nav-left" @click="goBack">
				<text class="back-arrow">←</text>
			</view>
			<view class="nav-title">光耀智慧社区</view>
			<view class="nav-right">
				<image class="avatar-small" src="/static/avatar/default.png" mode="aspectFill"></image>
			</view>
		</view>

		<!-- 页面标题 -->
		<view class="page-title-section">
			<view class="page-main-title">快递包裹</view>
			<view class="page-desc">追踪和管理您的收件包裹。在快递柜使用安全的取件码提取您的物品。</view>
		</view>

		<!-- 标签切换 -->
		<view class="tab-section">
			<view 
				class="tab-item" 
				:class="{ active: currentTab === 0 }"
				@click="switchTab(0)"
			>
				待领取
			</view>
			<view 
				class="tab-item" 
				:class="{ active: currentTab === 1 }"
				@click="switchTab(1)"
			>
				已领取
			</view>
		</view>

		<!-- 包裹列表 -->
		<view class="package-list" v-if="currentTab === 0">
			<view class="package-card" v-for="(item, index) in pendingPackages" :key="index">
				<view class="package-header">
					<view class="package-left">
						<view class="package-icon-wrap">
							<text class="package-icon">📦</text>
						</view>
						<view class="package-info">
							<view class="package-name">{{ item.name }}</view>
							<view class="package-time">
								<text class="time-icon">⏰</text>
								<text>{{ item.time }}</text>
							</view>
						</view>
					</view>
					<view class="package-tag" :class="item.tagClass">{{ item.tag }}</view>
				</view>
				<view class="package-footer">
					<view class="tracking-num">运单号 {{ item.tracking }}</view>
					<view class="code-btn" @click="showCode(item)">
						<text>获取取件码</text>
						<text class="qr-icon">🔳</text>
					</view>
				</view>
			</view>
		</view>

		<!-- 已领取空状态 -->
		<view class="empty-state" v-if="currentTab === 1">
			<view class="empty-icon">📭</view>
			<view class="empty-text">暂无已领取包裹</view>
		</view>

		<!-- 取件码卡片 -->
		<view class="code-card">
			<view class="code-title">取件码</view>
			<view class="code-desc">在A柜机扫码或向前台出示</view>
			<view class="qr-wrap">
				<view class="qr-placeholder">
					<text class="qr-text">🔳</text>
				</view>
			</view>
			<view class="code-number">782-019</view>
		</view>

		<!-- 开放时间 -->
		<view class="hours-card">
			<view class="hours-title">
				<text class="hours-icon">ℹ️</text>
				<text>快递室开放时间</text>
			</view>
			<view class="hours-list">
				<view class="hours-item">
					<text class="hours-day">周一 - 周五:</text>
					<text class="hours-time">07:00 - 22:00</text>
				</view>
				<view class="hours-item">
					<text class="hours-day">周六 - 周日:</text>
					<text class="hours-time">08:00 - 20:00</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 当前标签页
				currentTab: 0,
				// 待领取包裹
				pendingPackages: [
					{
						name: '顺丰速运',
						time: '今天到达 10:42 AM',
						tracking: 'SF1049582910',
						tag: '快递柜 A3',
						tagClass: 'tag-blue'
					},
					{
						name: '京东物流',
						time: '昨天到达 4:15 PM',
						tracking: 'JD992837465',
						tag: '前台代收',
						tagClass: 'tag-purple'
					}
				]
			}
		},
		methods: {
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 切换标签
			switchTab(index) {
				this.currentTab = index
			},
			// 显示取件码
			showCode(item) {
				uni.showToast({
					title: `取件码: ${item.tracking}`,
					icon: 'none'
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
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.back-arrow {
		font-size: 40rpx;
		color: #333333;
	}

	.nav-title {
		font-size: 36rpx;
		font-weight: bold;
		color: #2c7a7b;
	}

	.nav-right {
		width: 60rpx;
		height: 60rpx;
	}

	.avatar-small {
		width: 56rpx;
		height: 56rpx;
		border-radius: 50%;
		background-color: #e0e0e0;
	}

	/* 页面标题 */
	.page-title-section {
		padding: 30rpx 30rpx 20rpx;
		background-color: #ffffff;
	}

	.page-main-title {
		font-size: 48rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 12rpx;
	}

	.page-desc {
		font-size: 26rpx;
		color: #999999;
		line-height: 1.6;
	}

	/* 标签切换 */
	.tab-section {
		display: flex;
		gap: 20rpx;
		padding: 20rpx 30rpx;
		background-color: #ffffff;
	}

	.tab-item {
		padding: 16rpx 40rpx;
		border-radius: 30rpx;
		font-size: 28rpx;
		color: #666666;
		background-color: #f0f0f0;
	}

	.tab-item.active {
		background-color: #2c7a7b;
		color: #ffffff;
	}

	/* 包裹列表 */
	.package-list {
		padding: 0 30rpx;
	}

	.package-card {
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 24rpx;
		margin-bottom: 20rpx;
	}

	.package-header {
		display: flex;
		justify-content: space-between;
		align-items: flex-start;
		margin-bottom: 20rpx;
	}

	.package-left {
		display: flex;
		align-items: center;
		flex: 1;
	}

	.package-icon-wrap {
		width: 80rpx;
		height: 80rpx;
		background-color: #f0f0f0;
		border-radius: 16rpx;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-right: 20rpx;
		flex-shrink: 0;
	}

	.package-icon {
		font-size: 40rpx;
	}

	.package-info {
		flex: 1;
	}

	.package-name {
		font-size: 32rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 8rpx;
	}

	.package-time {
		display: flex;
		align-items: center;
		font-size: 24rpx;
		color: #999999;
	}

	.time-icon {
		margin-right: 6rpx;
		font-size: 24rpx;
	}

	.package-tag {
		font-size: 22rpx;
		padding: 6rpx 16rpx;
		border-radius: 20rpx;
		flex-shrink: 0;
	}

	.tag-blue {
		background-color: #e8e0f0;
		color: #6666cc;
	}

	.tag-purple {
		background-color: #f0e8f0;
		color: #9966cc;
	}

	.package-footer {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding-top: 16rpx;
		border-top: 1rpx solid #f0f0f0;
	}

	.tracking-num {
		font-size: 26rpx;
		color: #666666;
	}

	.code-btn {
		display: flex;
		align-items: center;
		background-color: #2c7a7b;
		color: #ffffff;
		font-size: 24rpx;
		padding: 12rpx 24rpx;
		border-radius: 30rpx;
	}

	.qr-icon {
		margin-left: 8rpx;
		font-size: 24rpx;
	}

	/* 空状态 */
	.empty-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 80rpx 0;
	}

	.empty-icon {
		font-size: 80rpx;
		margin-bottom: 20rpx;
	}

	.empty-text {
		font-size: 28rpx;
		color: #999999;
	}

	/* 取件码卡片 */
	.code-card {
		margin: 20rpx 30rpx;
		background: linear-gradient(135deg, #4a8a8b 0%, #6ba8a9 100%);
		border-radius: 24rpx;
		padding: 40rpx;
		text-align: center;
		color: #ffffff;
	}

	.code-title {
		font-size: 36rpx;
		font-weight: bold;
		margin-bottom: 10rpx;
	}

	.code-desc {
		font-size: 24rpx;
		color: rgba(255, 255, 255, 0.8);
		margin-bottom: 30rpx;
	}

	.qr-wrap {
		display: flex;
		justify-content: center;
		margin-bottom: 20rpx;
	}

	.qr-placeholder {
		width: 280rpx;
		height: 280rpx;
		background-color: #ffffff;
		border-radius: 20rpx;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.qr-text {
		font-size: 120rpx;
	}

	.code-number {
		font-size: 40rpx;
		font-weight: bold;
		letter-spacing: 4rpx;
	}

	/* 开放时间卡片 */
	.hours-card {
		margin: 0 30rpx;
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 30rpx;
	}

	.hours-title {
		display: flex;
		align-items: center;
		font-size: 28rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 20rpx;
	}

	.hours-icon {
		margin-right: 10rpx;
		font-size: 28rpx;
	}

	.hours-list {
		display: flex;
		flex-direction: column;
		gap: 16rpx;
	}

	.hours-item {
		display: flex;
		justify-content: space-between;
		font-size: 26rpx;
	}

	.hours-day {
		color: #666666;
	}

	.hours-time {
		color: #333333;
		font-weight: bold;
	}
</style>
