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

		<!-- 分类标签 -->
		<view class="category-section">
			<view 
				class="category-item" 
				v-for="(item, index) in categoryList" 
				:key="index"
				:class="{ active: currentCategory === item.value }"
				@click="switchCategory(item.value)"
			>
				{{ item.label }}
			</view>
		</view>

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

		<!-- 加载更多 -->
		<view class="load-more" @click="loadMore">
			<text>加载更多资讯</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 当前选中的分类
				currentCategory: 'all',
				// 分类列表
				categoryList: [
					{ label: '全部通知', value: 'all' },
					{ label: '重要通知', value: 'important' },
					{ label: '活动预告', value: 'activity' }
				],
				// 公告列表数据
				noticeList: [
					{
						tag: '通知',
						tagClass: 'tag-notice',
						date: '2025/10/21',
						title: '停水通知：A区水管网例行检修',
						desc: '接自来水公司通知，因例行管网维护检修，本社区住宅楼将于本周三下午14:00至18:00暂停供水，请大家提前做好储水准备。',
						link: '阅读更多',
						image: '/static/notice/water.jpg',
						category: 'important'
					},
					{
						tag: '活动',
						tagClass: 'tag-activity',
						date: '2025/10/18',
						title: '秋季社区文化节圆满落幕',
						desc: '感谢各位居民的积极参与！本次社区文化节吸引了超过500个家庭参与，各类文艺汇演和互动游戏活动均获得圆满成功，期待来年再聚。',
						link: '查看照片',
						image: '/static/notice/event.jpg',
						imageOverlay: true,
						category: 'activity'
					},
					{
						tag: '通知',
						tagClass: 'tag-notice',
						date: '2025/10/15',
						title: '关于启用全新智能门禁系统的说明',
						desc: '为了进一步提升小区的安全管理水平，物业服务中心已全面完成人脸识别智能门禁系统升级，请各位业主及时前往物业办公室进行人脸信息录入，以便正常使用。',
						link: '阅读详细说明',
						category: 'important'
					},
					{
						tag: '活动',
						tagClass: 'tag-activity',
						date: '2025/10/10',
						title: '垃圾分类积分兑换活动即将开始',
						desc: '本社区垃圾分类积分兑换活动将于本周五在小区中心广场举行，欢迎广大居民参与兑换各类生活用品。',
						link: '查看详情',
						image: '/static/notice/recycle.jpg',
						category: 'activity'
					}
				]
			}
		},
		computed: {
			// 根据分类筛选公告
			filteredNoticeList() {
				if (this.currentCategory === 'all') {
					return this.noticeList
				}
				return this.noticeList.filter(item => item.category === this.currentCategory)
			}
		},
		methods: {
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 切换分类
			switchCategory(value) {
				this.currentCategory = value
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

	/* 分类标签 */
	.category-section {
		display: flex;
		padding: 20rpx 30rpx;
		background-color: #ffffff;
		gap: 20rpx;
	}

	.category-item {
		padding: 12rpx 28rpx;
		border-radius: 30rpx;
		font-size: 26rpx;
		color: #666666;
		background-color: #f0f0f0;
		transition: all 0.3s;
	}

	.category-item.active {
		background-color: #2c7a7b;
		color: #ffffff;
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
