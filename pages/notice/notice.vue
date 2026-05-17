<template>
	<view class="container">
		<!-- 页面标题区域 -->
		<view class="page-header">
			<view class="back-btn" @click="goBack">
				<text class="back-arrow">←</text>
			</view>
			<view class="header-title">社区公告</view>
			<view class="header-right"></view>
		</view>

		<!-- 标题和描述 -->
		<view class="title-section">
			<view class="main-title">社区<br>公告</view>
			<view class="title-desc">获取我们充满活力的社区的最新动态、重要通知和精选新闻，保持信息灵通。</view>
		</view>

		<!-- 分类标签（使用 FilterTabs 组件） -->
		<FilterTabs :tabs="categoryLabels" :current="currentCategoryIndex" @change="switchCategory" />

		<!-- 公告列表 -->
		<view class="notice-list">
			<view class="notice-card" v-for="(item, index) in filteredNoticeList" :key="index" @click="viewDetail(item)">
				<!-- 图片区域 -->
				<view class="notice-image-wrap" v-if="item.image">
					<image class="notice-image" :src="item.image" mode="aspectFill"></image>
					<view class="image-overlay" v-if="item.imageOverlay">
						<view class="overlay-icon">💡</view>
						<view class="overlay-title">COMMUNITY</view>
						<view class="overlay-subtitle">EVENT</view>
					</view>
				</view>

				<!-- 内容区域 -->
				<view class="notice-content">
					<view class="notice-meta">
						<view class="notice-tag" :class="item.tagClass">{{ item.tag }}</view>
						<view class="notice-date">{{ item.date }}</view>
					</view>
					<view class="notice-title">{{ item.title }}</view>
					<view class="notice-desc">{{ item.desc }}</view>
					<view class="notice-link" v-if="item.link">
						<text>{{ item.link }}</text>
						<text class="link-arrow"> ></text>
					</view>
				</view>
			</view>
		</view>

		<!-- 空状态 -->
		<EmptyState v-if="filteredNoticeList.length === 0" text="暂无公告" />

		<!-- 加载更多 -->
		<view class="load-more" @click="loadMore" v-if="filteredNoticeList.length > 0">
			<text>加载更多资讯</text>
		</view>
	</view>
</template>

<script>
	import { noticeApi } from '@/api/index.js'

	export default {
		data() {
			return {
				// 当前选中的分类索引
				currentCategoryIndex: 0,
				// 分类标签文本
				categoryLabels: ['全部通知', '重要通知', '活动预告'],
				// 分类列表
				categoryList: [
					{ label: '全部通知', value: 'all' },
					{ label: '重要通知', value: 'important' },
					{ label: '活动预告', value: 'activity' }
				],
				// 公告列表数据（从 API 获取）
				noticeList: [],
				loading: true
			}
		},
		async onLoad() {
			await this.fetchNotices()
		},
		computed: {
			// 当前选中的分类值
			currentCategory() {
				return this.categoryList[this.currentCategoryIndex]?.value || 'all'
			},
			// 根据分类筛选公告（前端筛选，也可改为后端筛选）
			filteredNoticeList() {
				if (this.currentCategory === 'all') {
					return this.noticeList
				}
				return this.noticeList.filter(item => item.category === this.currentCategory)
			}
		},
		methods: {
			// 从 API 获取公告列表
			async fetchNotices(category = 'all') {
				try {
					this.loading = true
					this.noticeList = await noticeApi.getList(category)
				} catch (err) {
					console.error('获取公告列表失败:', err)
				} finally {
					this.loading = false
				}
			},
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 切换分类（接收 FilterTabs 的索引参数）
			switchCategory(index) {
				this.currentCategoryIndex = index
			},
			// 查看详情 - 活动类跳转到社区活动页，其他弹toast
			viewDetail(item) {
				if (item.category === 'activity') {
					uni.navigateTo({
						url: '/pages/activity/activity'
					})
				} else {
					uni.showToast({
						title: `查看: ${item.title}`,
						icon: 'none'
					})
				}
			},
			// 加载更多
			loadMore() {
				uni.showToast({
					title: '加载更多...',
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

	/* 标题区域 */
	.title-section {
		padding: 40rpx 30rpx 30rpx;
		background-color: #ffffff;
	}

	.main-title {
		font-size: 56rpx;
		font-weight: bold;
		color: #1a1a2e;
		line-height: 1.3;
		margin-bottom: 20rpx;
	}

	.title-desc {
		font-size: 26rpx;
		color: #666666;
		line-height: 1.6;
	}

	/* 公告列表 */
	.notice-list {
		padding: 20rpx 30rpx;
	}

	/* 公告卡片 */
	.notice-card {
		background-color: #ffffff;
		border-radius: 20rpx;
		margin-bottom: 24rpx;
		overflow: hidden;
	}

	/* 图片区域 */
	.notice-image-wrap {
		position: relative;
		width: 100%;
		height: 300rpx;
		background-color: #2c3e50;
	}

	.notice-image {
		width: 100%;
		height: 100%;
	}

	/* 图片遮罩层（用于活动类卡片） */
	.image-overlay {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background-color: rgba(0, 0, 0, 0.5);
	}

	.overlay-icon {
		font-size: 60rpx;
		margin-bottom: 16rpx;
	}

	.overlay-title {
		color: #ffffff;
		font-size: 32rpx;
		font-weight: bold;
		letter-spacing: 4rpx;
	}

	.overlay-subtitle {
		color: #ffffff;
		font-size: 28rpx;
		letter-spacing: 6rpx;
		margin-top: 8rpx;
	}

	/* 内容区域 */
	.notice-content {
		padding: 24rpx;
	}

	.notice-meta {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 16rpx;
	}

	.notice-tag {
		display: inline-block;
		padding: 6rpx 16rpx;
		border-radius: 8rpx;
		font-size: 22rpx;
	}

	/* 通知标签样式 */
	.tag-notice {
		background-color: #2c7a7b;
		color: #ffffff;
	}

	/* 活动标签样式 */
	.tag-activity {
		background-color: #e8f4f8;
		color: #2c7a7b;
	}

	.notice-date {
		font-size: 24rpx;
		color: #999999;
	}

	.notice-title {
		font-size: 32rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 12rpx;
		line-height: 1.4;
	}

	.notice-desc {
		font-size: 26rpx;
		color: #666666;
		line-height: 1.6;
		margin-bottom: 16rpx;
	}

	.notice-link {
		display: flex;
		align-items: center;
		font-size: 26rpx;
		color: #2c7a7b;
	}

	.link-arrow {
		margin-left: 8rpx;
		font-size: 28rpx;
	}

	/* 加载更多 */
	.load-more {
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 30rpx;
		margin: 0 30rpx;
		background-color: #e8f0f0;
		border-radius: 16rpx;
		font-size: 28rpx;
		color: #2c7a7b;
	}
</style>
