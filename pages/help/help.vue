<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="page-header">
			<view class="back-btn" @click="goBack">
				<text class="back-arrow">←</text>
			</view>
			<view class="header-title">帮助中心</view>
			<view class="header-right"></view>
		</view>

		<!-- 欢迎语 -->
		<view class="welcome-section">
			<view class="welcome-title">您好，</view>
			<view class="welcome-subtitle">需要什么帮助？</view>
			<view class="welcome-desc">搜索常见问题或浏览下方分类。</view>
		</view>

		<!-- 搜索框 -->
		<view class="search-section">
			<view class="search-box">
				<text class="search-icon">🔍</text>
				<input 
					class="search-input" 
					placeholder="搜索问题、关键字..." 
					placeholder-class="search-placeholder"
					v-model="searchKeyword"
					@confirm="onSearch"
				/>
			</view>
		</view>

		<!-- 分类网格 -->
		<view class="category-section">
			<view class="category-grid">
				<view 
					class="category-item" 
					v-for="(item, index) in categoryList" 
					:key="index"
					@click="onCategoryClick(item)"
				>
					<view class="category-icon-wrap" :style="{ backgroundColor: item.bgColor }">
						<text class="category-icon">{{ item.icon }}</text>
					</view>
					<view class="category-name">{{ item.name }}</view>
					<view class="category-desc">{{ item.desc }}</view>
				</view>
			</view>
		</view>

		<!-- 热门问题 -->
		<view class="section">
			<view class="section-header">
				<text class="section-title">热门问题</text>
				<view class="section-more" @click="viewAllQuestions">
					<text>查看全部</text>
				</view>
			</view>
			<view class="question-list">
				<view 
					class="question-item" 
					v-for="(item, index) in hotQuestions" 
					:key="index"
					@click="onQuestionClick(item)"
				>
					<text class="question-text">{{ item }}</text>
					<text class="question-arrow">></text>
				</view>
			</view>
		</view>

		<!-- 在线人工客服 -->
		<view class="service-card">
			<view class="service-content">
				<view class="service-left">
					<view class="service-title">在线人工客服</view>
					<view class="service-desc">专业客服为您实时在线解答疑问</view>
					<view class="service-time">(09:00-21:00)</view>
					<view class="consult-btn" @click="consultService">立即咨询</view>
				</view>
				<view class="service-right">
					<text class="headset-icon">🎧</text>
				</view>
			</view>
		</view>

		<!-- 服务热线 -->
		<view class="hotline-card">
			<view class="hotline-left">
				<view class="hotline-icon-wrap">
					<text class="hotline-icon">📞</text>
				</view>
				<view class="hotline-info">
					<view class="hotline-label">24小时服务热线</view>
					<view class="hotline-number">400-123-4567</view>
				</view>
			</view>
			<view class="call-btn" @click="callHotline">
				<text class="call-icon">📞</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 搜索关键词
				searchKeyword: '',
				// 分类列表
				categoryList: [
					{
						name: '物业报修',
						desc: '漏水、电路故障、公区维护等指引。',
						icon: '🏠',
						bgColor: '#e8f4f8',
						path: '/pages/repair-apply/repair-apply'
					},
					{
						name: '停车服务',
						desc: '月卡办理、临停缴费及车位租赁。',
						icon: '🅿️',
						bgColor: '#e8f4f8',
						path: '/pages/payment/payment'
					},
					{
						name: '社区活动',
						desc: '活动报名流程及志愿者加入说明。',
						icon: '📅',
						bgColor: '#e8f4f8',
						path: '/pages/activity/activity'
					},
					{
						name: 'App 使用',
						desc: '账号安全、通知设置及功能向导。',
						icon: '📱',
						bgColor: '#e8f4f8',
						path: ''
					}
				],
				// 热门问题
				hotQuestions: [
					'如何修改社区通行二维码的有效期？',
					'缴纳物业费后如何在线开具发票？',
					'地下车库地锁损坏由谁负责维修？'
				]
			}
		},
		methods: {
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 搜索
			onSearch() {
				if (!this.searchKeyword.trim()) {
					uni.showToast({
						title: '请输入搜索内容',
						icon: 'none'
					})
					return
				}
				uni.showToast({
					title: `搜索: ${this.searchKeyword}`,
					icon: 'none'
				})
			},
			// 分类点击 - 跳转到对应功能页面
			onCategoryClick(item) {
				if (item.path) {
					uni.navigateTo({
						url: item.path
					})
				} else {
					uni.showToast({
						title: item.name,
						icon: 'none'
					})
				}
			},
			// 查看全部问题
			viewAllQuestions() {
				uni.showToast({
					title: '查看全部',
					icon: 'none'
				})
			},
			// 问题点击
			onQuestionClick(question) {
				uni.showToast({
					title: question,
					icon: 'none'
				})
			},
			// 立即咨询
			consultService() {
				uni.showToast({
					title: '正在连接客服...',
					icon: 'none'
				})
			},
			// 拨打热线
			callHotline() {
				uni.makePhoneCall({
					phoneNumber: '4001234567',
					fail: () => {
						uni.showToast({
							title: '拨打失败',
							icon: 'none'
						})
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
	}

	/* 欢迎语 */
	.welcome-section {
		padding: 30rpx 30rpx 20rpx;
		background-color: #ffffff;
	}

	.welcome-title {
		font-size: 44rpx;
		font-weight: bold;
		color: #333333;
	}

	.welcome-subtitle {
		font-size: 44rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 12rpx;
	}

	.welcome-desc {
		font-size: 26rpx;
		color: #999999;
	}

	/* 搜索框 */
	.search-section {
		padding: 20rpx 30rpx;
		background-color: #ffffff;
	}

	.search-box {
		display: flex;
		align-items: center;
		background-color: #f5f7fa;
		border-radius: 40rpx;
		padding: 20rpx 30rpx;
	}

	.search-icon {
		font-size: 32rpx;
		margin-right: 16rpx;
		color: #999999;
	}

	.search-input {
		flex: 1;
		font-size: 28rpx;
		color: #333333;
	}

	.search-placeholder {
		color: #cccccc;
		font-size: 28rpx;
	}

	/* 分类区域 */
	.category-section {
		padding: 20rpx 30rpx;
		background-color: #ffffff;
	}

	.category-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 20rpx;
	}

	.category-item {
		background-color: #f8f9fa;
		border-radius: 20rpx;
		padding: 30rpx;
	}

	.category-icon-wrap {
		width: 72rpx;
		height: 72rpx;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 16rpx;
	}

	.category-icon {
		font-size: 36rpx;
	}

	.category-name {
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 8rpx;
	}

	.category-desc {
		font-size: 22rpx;
		color: #999999;
		line-height: 1.5;
	}

	/* 分区 */
	.section {
		margin: 20rpx 30rpx 0;
	}

	.section-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 20rpx;
	}

	.section-title {
		font-size: 32rpx;
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

	/* 问题列表 */
	.question-list {
		background-color: #ffffff;
		border-radius: 20rpx;
		overflow: hidden;
	}

	.question-item {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 30rpx 24rpx;
		border-bottom: 1rpx solid #f0f0f0;
	}

	.question-item:last-child {
		border-bottom: none;
	}

	.question-text {
		flex: 1;
		font-size: 28rpx;
		color: #333333;
		margin-right: 20rpx;
	}

	.question-arrow {
		font-size: 28rpx;
		color: #cccccc;
	}

	/* 在线客服卡片 */
	.service-card {
		margin: 20rpx 30rpx;
		background: linear-gradient(135deg, #2c5f60 0%, #3a7a7b 100%);
		border-radius: 24rpx;
		padding: 40rpx;
		position: relative;
		overflow: hidden;
	}

	.service-content {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.service-left {
		flex: 1;
	}

	.service-title {
		font-size: 34rpx;
		font-weight: bold;
		color: #ffffff;
		margin-bottom: 10rpx;
	}

	.service-desc {
		font-size: 24rpx;
		color: rgba(255, 255, 255, 0.8);
		margin-bottom: 6rpx;
	}

	.service-time {
		font-size: 22rpx;
		color: rgba(255, 255, 255, 0.6);
		margin-bottom: 20rpx;
	}

	.consult-btn {
		display: inline-block;
		background-color: #ffffff;
		color: #2c7a7b;
		font-size: 26rpx;
		padding: 14rpx 32rpx;
		border-radius: 30rpx;
		font-weight: bold;
	}

	.service-right {
		width: 120rpx;
		height: 120rpx;
		display: flex;
		align-items: center;
		justify-content: center;
		opacity: 0.2;
	}

	.headset-icon {
		font-size: 100rpx;
	}

	/* 服务热线卡片 */
	.hotline-card {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin: 0 30rpx;
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 30rpx;
	}

	.hotline-left {
		display: flex;
		align-items: center;
	}

	.hotline-icon-wrap {
		width: 80rpx;
		height: 80rpx;
		background-color: #e8f4f8;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-right: 20rpx;
	}

	.hotline-icon {
		font-size: 40rpx;
	}

	.hotline-info {
		display: flex;
		flex-direction: column;
	}

	.hotline-label {
		font-size: 22rpx;
		color: #999999;
		margin-bottom: 6rpx;
	}

	.hotline-number {
		font-size: 32rpx;
		font-weight: bold;
		color: #333333;
	}

	.call-btn {
		width: 72rpx;
		height: 72rpx;
		background-color: #f5f7fa;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.call-icon {
		font-size: 36rpx;
	}
</style>
