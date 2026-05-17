<template>
	<view class="container">
		<!-- 自定义导航栏 -->
		<view class="custom-nav">
			<view class="nav-left" @click="goBack">
				<text class="back-arrow">←</text>
			</view>
			<view class="nav-title">启明社区</view>
			<view class="nav-right">
				<image class="avatar-small" src="/static/avatar/default.png" mode="aspectFill"></image>
			</view>
		</view>

		<!-- 页面标题 -->
		<view class="page-title-section">
			<view class="page-main-title">社区活动</view>
			<view class="page-desc">参与我们精心策划的社区活动，与邻里建立联系，共同营造充满活力的社区文化。</view>
		</view>

		<!-- 分类筛选 -->
		<view class="filter-section">
			<view 
				class="filter-item" 
				:class="{ active: currentFilter === 'all' }"
				@click="switchFilter('all')"
			>
				全部活动
			</view>
			<view 
				class="filter-item" 
				:class="{ active: currentFilter === 'art' }"
				@click="switchFilter('art')"
			>
				文化艺术
			</view>
			<view 
				class="filter-item" 
				:class="{ active: currentFilter === 'health' }"
				@click="switchFilter('health')"
			>
				健康生活
			</view>
			<view 
				class="filter-item" 
				:class="{ active: currentFilter === 'family' }"
				@click="switchFilter('family')"
			>
				家庭亲子
			</view>
		</view>

		<!-- 精选推荐 -->
		<view class="section" v-if="currentFilter === 'all' || currentFilter === 'art'">
			<view class="section-label">精选推荐</view>
			<view class="featured-card">
				<image class="featured-image" src="/static/activity/pottery.jpg" mode="aspectFill"></image>
				<view class="featured-content">
					<view class="featured-tag">本周末</view>
					<view class="featured-title">春季陶艺体验工坊</view>
					<view class="featured-meta">
						<view class="meta-item">
							<text class="meta-icon">📅</text>
							<text>2024年4月15日 周六 14:00 - 16:00</text>
						</view>
						<view class="meta-item">
							<text class="meta-icon">📍</text>
							<text>社区艺术中心一层</text>
						</view>
					</view>
					<view class="featured-desc">在专业导师的指导下，体验泥土的魅力，亲手制作属于自己的陶瓷器具。适合所有水平，提供所需材料和工具。</view>
					<view class="join-btn" @click="joinActivity('春季陶艺体验工坊')">
						<text>报名参加</text>
						<text class="btn-arrow">→</text>
					</view>
				</view>
			</view>
		</view>

		<!-- 活动列表 -->
		<view class="activity-list">
			<view class="activity-item" v-for="(item, index) in activityList" :key="index" v-if="currentFilter === 'all' || item.category === currentFilter">
				<image class="activity-image" :src="item.image" mode="aspectFill"></image>
				<view class="activity-content">
					<view class="activity-title">{{ item.title }}</view>
					<view class="activity-meta">
						<text class="meta-icon">📅</text>
						<text>{{ item.date }}</text>
					</view>
					<view class="activity-meta">
						<text class="meta-icon">📍</text>
						<text>{{ item.location }}</text>
					</view>
					<view class="activity-status" v-if="item.status">
						<text class="status-icon">🔒</text>
						<text>{{ item.status }}</text>
					</view>
				</view>
				<view class="activity-action">
					<view class="action-btn" :class="{ disabled: item.isFull }" @click="joinActivity(item.title)">
						{{ item.isFull ? '名额已满' : '报名参加' }}
					</view>
				</view>
			</view>
		</view>

		<!-- 加载更多 -->
		<view class="load-more" @click="loadMore">
			<text>加载更多活动</text>
			<text class="load-arrow">↓</text>
		</view>
	</view>
</template>

<script>
	import { activityApi } from '@/api/index.js'

	export default {
		data() {
			return {
				// 当前筛选
				currentFilter: 'all',
				// 活动列表（从 API 获取）
				activityList: [],
				loading: true
			}
		},
		async onLoad() {
			await this.fetchActivities()
		},
		methods: {
			// 从 API 获取活动列表
			async fetchActivities(category = 'all') {
				try {
					this.loading = true
					this.activityList = await activityApi.getList(category)
				} catch (err) {
					console.error('获取活动列表失败:', err)
				} finally {
					this.loading = false
				}
			},
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 切换筛选
			switchFilter(filter) {
				this.currentFilter = filter
			},
			// 报名活动
			async joinActivity(item) {
				uni.showModal({
					title: '确认报名',
					content: `确认报名参加"${item.title}"吗？`,
					success: async (res) => {
						if (res.confirm) {
							try {
								await activityApi.join(item.id)
								uni.showToast({ title: '报名成功', icon: 'success' })
							} catch (err) {
								uni.showToast({ title: '报名失败', icon: 'none' })
							}
						}
					}
				})
			},
			// 加载更多
			loadMore() {
				uni.showToast({
					title: '加载更多活动...',
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
		font-size: 44rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 12rpx;
	}

	.page-desc {
		font-size: 26rpx;
		color: #999999;
		line-height: 1.6;
	}

	/* 分类筛选 */
	.filter-section {
		display: flex;
		gap: 16rpx;
		padding: 20rpx 30rpx;
		background-color: #ffffff;
		overflow-x: auto;
	}

	.filter-item {
		padding: 12rpx 28rpx;
		border-radius: 30rpx;
		font-size: 26rpx;
		color: #666666;
		background-color: #f0f0f0;
		white-space: nowrap;
		flex-shrink: 0;
	}

	.filter-item.active {
		background-color: #2c7a7b;
		color: #ffffff;
	}

	/* 分区 */
	.section {
		margin: 20rpx 30rpx 0;
	}

	.section-label {
		font-size: 28rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 16rpx;
	}

	/* 精选推荐卡片 */
	.featured-card {
		background-color: #ffffff;
		border-radius: 20rpx;
		overflow: hidden;
	}

	.featured-image {
		width: 100%;
		height: 300rpx;
	}

	.featured-content {
		padding: 24rpx;
	}

	.featured-tag {
		display: inline-block;
		background-color: #2c7a7b;
		color: #ffffff;
		font-size: 22rpx;
		padding: 6rpx 16rpx;
		border-radius: 8rpx;
		margin-bottom: 12rpx;
	}

	.featured-title {
		font-size: 34rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 16rpx;
	}

	.featured-meta {
		display: flex;
		flex-direction: column;
		gap: 8rpx;
		margin-bottom: 16rpx;
	}

	.meta-item {
		display: flex;
		align-items: center;
		font-size: 24rpx;
		color: #666666;
	}

	.meta-icon {
		margin-right: 8rpx;
		font-size: 24rpx;
	}

	.featured-desc {
		font-size: 24rpx;
		color: #666666;
		line-height: 1.5;
		margin-bottom: 20rpx;
	}

	.join-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: #2c7a7b;
		color: #ffffff;
		font-size: 28rpx;
		font-weight: bold;
		padding: 20rpx 0;
		border-radius: 30rpx;
	}

	.btn-arrow {
		margin-left: 8rpx;
		font-size: 28rpx;
	}

	/* 活动列表 */
	.activity-list {
		padding: 0 30rpx;
	}

	.activity-item {
		display: flex;
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 20rpx;
		margin-bottom: 20rpx;
		align-items: center;
	}

	.activity-image {
		width: 160rpx;
		height: 160rpx;
		border-radius: 16rpx;
		background-color: #f0f0f0;
		margin-right: 20rpx;
		flex-shrink: 0;
	}

	.activity-content {
		flex: 1;
	}

	.activity-title {
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 10rpx;
	}

	.activity-meta {
		display: flex;
		align-items: center;
		font-size: 24rpx;
		color: #666666;
		margin-bottom: 6rpx;
	}

	.activity-status {
		display: flex;
		align-items: center;
		font-size: 22rpx;
		color: #999999;
		margin-top: 8rpx;
	}

	.status-icon {
		margin-right: 6rpx;
		font-size: 22rpx;
	}

	.activity-action {
		margin-left: 16rpx;
		flex-shrink: 0;
	}

	.action-btn {
		background-color: #2c7a7b;
		color: #ffffff;
		font-size: 24rpx;
		padding: 12rpx 24rpx;
		border-radius: 24rpx;
		white-space: nowrap;
	}

	.action-btn.disabled {
		background-color: #cccccc;
	}

	/* 加载更多 */
	.load-more {
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 30rpx;
		font-size: 26rpx;
		color: #999999;
	}

	.load-arrow {
		margin-left: 8rpx;
		font-size: 24rpx;
	}
</style>
