<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="page-header">
			<view class="back-btn" @click="goBack">
				<text class="back-arrow">←</text>
			</view>
			<view class="header-title">个人中心</view>
			<view class="header-right" @click="goSetting">
				<text class="setting-icon">⚙️</text>
			</view>
		</view>

		<!-- 用户信息卡片 -->
		<view class="user-card">
			<!-- 头像区域 -->
			<view class="avatar-wrap">
				<image class="avatar" src="/static/avatar/default.png" mode="aspectFill"></image>
				<view class="edit-btn">
					<text class="edit-icon">✏️</text>
				</view>
			</view>
			<!-- 用户名和认证 -->
			<view class="user-name-wrap">
				<text class="user-name">林静宜</text>
				<view class="verify-badge">已认证</view>
			</view>
			<view class="user-uid">UID:88294105</view>
			<!-- 标签区域 -->
			<view class="user-tags">
				<view class="tag-item">
					<view class="tag-icon">🛡️</view>
					<text class="tag-text">实名用户</text>
				</view>
				<view class="tag-item">
					<view class="tag-icon">⭐</view>
					<text class="tag-text">金牌邻里</text>
				</view>
			</view>
		</view>

		<!-- 账户管理 -->
		<view class="section">
			<view class="section-title">账户管理</view>
			<view class="menu-list">
				<view class="menu-item" @click="goPoints">
					<view class="menu-icon-wrap" style="background-color: #e8f4f8;">
						<text class="menu-icon">🎁</text>
					</view>
					<view class="menu-info">
						<view class="menu-label">积分与优惠券</view>
						<view class="menu-value">128积分 / 3张券</view>
					</view>
				
				</view>
				<view class="menu-item" @click="onMenuClick('绑定手机')">
					<view class="menu-icon-wrap" style="background-color: #e8f4f8;">
						<text class="menu-icon">📱</text>
					</view>
					<view class="menu-info">
						<view class="menu-label">绑定手机</view>
						<view class="menu-value">138 **** 9920</view>
					</view>
				
				</view>
				<view class="menu-item" @click="goExpress">
					<view class="menu-icon-wrap" style="background-color: #e8f4f8;">
						<text class="menu-icon">📍</text>
					</view>
					<view class="menu-info">
						<view class="menu-label">收货地址</view>
						<view class="menu-value">3个常用地址</view>
					</view>
					
				</view>
			</view>
		</view>

		<!-- 安全与隐私 -->
		<view class="section">
			<view class="section-title">安全与隐私</view>
			<view class="menu-list">
				<view class="menu-item" @click="onMenuClick('修改密码')">
					<view class="menu-icon-wrap" style="background-color: #f0f0f0;">
						<text class="menu-icon">🔒</text>
					</view>
					<view class="menu-info">
						<view class="menu-label">账号密码</view>
						<view class="menu-value">修改登录密码</view>
					</view>
			
				</view>
				<view class="menu-item">
					<view class="menu-icon-wrap" style="background-color: #f0f0f0;">
						<text class="menu-icon">👆</text>
					</view>
					<view class="menu-info">
						<view class="menu-label">生物识别</view>
						<view class="menu-value">面容/指纹支付</view>
					</view>
					<switch class="menu-switch" :checked="bioEnabled" @change="toggleBio" color="#2c7a7b" />
				</view>
			</view>
		</view>

		<!-- 其他 -->
		<view class="section">
			<view class="section-title">其他</view>
			<view class="menu-list">
				<view class="menu-item" @click="goHelp">
					<view class="menu-icon-wrap" style="background-color: #f0f0f0;">
						<text class="menu-icon">📋</text>
					</view>
					<view class="menu-info">
						<view class="menu-label single">服务协议与隐私政策</view>
					</view>
					
				</view>
			</view>
		</view>

		<!-- 退出登录 -->
		<view class="logout-btn" @click="logout">
			<text class="logout-icon">↪️</text>
			<text class="logout-text">退出当前账号</text>
		</view>

		<!-- 版本号 -->
		<view class="version">VERSION 2.4.0 (LUMINA EDITION)</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 生物识别开关状态
				bioEnabled: true
			}
		},
		methods: {
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 进入设置
			goSetting() {
				uni.showToast({
					title: '设置',
					icon: 'none'
				})
			},
			// 跳转到积分与优惠券页
			goPoints() {
				uni.navigateTo({
					url: '/pages/points/points'
				})
			},
			// 收货地址 - 跳转到快递代收页
			goExpress() {
				uni.navigateTo({
					url: '/pages/express/express'
				})
			},
			// 服务协议 - 跳转到帮助中心
			goHelp() {
				uni.navigateTo({
					url: '/pages/help/help'
				})
			},
			// 菜单点击
			onMenuClick(name) {
				uni.showToast({
					title: name,
					icon: 'none'
				})
			},
			// 切换生物识别
			toggleBio(e) {
				this.bioEnabled = e.detail.value
				uni.showToast({
					title: this.bioEnabled ? '已开启' : '已关闭',
					icon: 'none'
				})
			},
			// 退出登录
			logout() {
				uni.showModal({
					title: '提示',
					content: '确定要退出当前账号吗？',
					success: (res) => {
						if (res.confirm) {
							uni.showToast({
								title: '已退出登录',
								icon: 'success'
							})
						}
					}
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

	/* 顶部导航栏 */
	.page-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 20rpx 30rpx;
		background-color: #ffffff;
	}

	.back-btn {
		width: 60rpx;
		height: 60rpx;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.back-arrow {
		font-size: 40rpx;
		color: #333333;
	}

	.header-title {
		font-size: 34rpx;
		font-weight: bold;
		color: #333333;
	}

	.header-right {
		width: 60rpx;
		height: 60rpx;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.setting-icon {
		font-size: 36rpx;
	}

	/* 用户信息卡片 */
	.user-card {
		background-color: #ffffff;
		margin: 20rpx 30rpx;
		border-radius: 24rpx;
		padding: 40rpx 30rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	/* 头像 */
	.avatar-wrap {
		position: relative;
		margin-bottom: 24rpx;
	}

	.avatar {
		width: 160rpx;
		height: 160rpx;
		border-radius: 50%;
		background-color: #e0e0e0;
	}

	.edit-btn {
		position: absolute;
		bottom: 0;
		right: 0;
		width: 48rpx;
		height: 48rpx;
		background-color: #2c7a7b;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		border: 4rpx solid #ffffff;
	}

	.edit-icon {
		font-size: 24rpx;
		color: #ffffff;
	}

	/* 用户名 */
	.user-name-wrap {
		display: flex;
		align-items: center;
		margin-bottom: 10rpx;
	}

	.user-name {
		font-size: 40rpx;
		font-weight: bold;
		color: #333333;
		margin-right: 12rpx;
	}

	.verify-badge {
		background-color: #e8f4f8;
		color: #2c7a7b;
		font-size: 20rpx;
		padding: 4rpx 12rpx;
		border-radius: 8rpx;
	}

	.user-uid {
		font-size: 26rpx;
		color: #999999;
		margin-bottom: 30rpx;
	}

	/* 用户标签 */
	.user-tags {
		display: flex;
		gap: 20rpx;
		width: 100%;
	}

	.tag-item {
		flex: 1;
		background-color: #f5f7fa;
		border-radius: 16rpx;
		padding: 24rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.tag-icon {
		font-size: 40rpx;
		margin-bottom: 8rpx;
	}

	.tag-text {
		font-size: 24rpx;
		color: #666666;
	}

	/* 分区 */
	.section {
		margin: 0 30rpx 20rpx;
	}

	.section-title {
		font-size: 24rpx;
		color: #2c7a7b;
		margin-bottom: 16rpx;
		padding-left: 10rpx;
	}

	/* 菜单列表 */
	.menu-list {
		background-color: #ffffff;
		border-radius: 20rpx;
		overflow: hidden;
	}

	.menu-item {
		display: flex;
		align-items: center;
		padding: 28rpx 24rpx;
		border-bottom: 1rpx solid #f0f0f0;
	}

	.menu-item:last-child {
		border-bottom: none;
	}

	.menu-icon-wrap {
		width: 72rpx;
		height: 72rpx;
		border-radius: 16rpx;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-right: 20rpx;
		flex-shrink: 0;
	}

	.menu-icon {
		font-size: 36rpx;
	}

	.menu-info {
		flex: 1;
	}

	.menu-label {
		font-size: 28rpx;
		color: #333333;
		margin-bottom: 6rpx;
	}

	.menu-label.single {
		margin-bottom: 0;
		line-height: 72rpx;
	}

	.menu-value {
		font-size: 24rpx;
		color: #666666;
	}

	.menu-arrow {
		font-size: 28rpx;
		color: #cccccc;
		margin-left: 10rpx;
	}

	.menu-switch {
		transform: scale(0.8);
	}

	/* 退出登录 */
	.logout-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 30rpx;
		margin: 20rpx 30rpx;
		background-color: #ffffff;
		border-radius: 20rpx;
	}

	.logout-icon {
		font-size: 32rpx;
		margin-right: 12rpx;
	}

	.logout-text {
		font-size: 30rpx;
		color: #e64340;
	}

	/* 版本号 */
	.version {
		text-align: center;
		font-size: 22rpx;
		color: #cccccc;
		margin-top: 30rpx;
	}
</style>
