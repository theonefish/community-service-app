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

		<!-- 顶部横幅 -->
		<view class="banner-card">
			<view class="banner-content">
				<view class="banner-title">携手共建<br>更美好的社区环境</view>
				<view class="banner-desc">加入我们的志愿者网络，您的每一份力量都在为社区注入新的活力。选择您感兴趣的领域，用行动传递温暖。</view>
				<view class="banner-btn" @click="viewHours">查看我的志愿时长</view>
			</view>
		</view>

		<!-- 分类筛选 -->
		<view class="filter-section">
			<view 
				class="filter-item" 
				:class="{ active: currentFilter === 'all' }"
				@click="switchFilter('all')"
			>
				全部项目
			</view>
			<view 
				class="filter-item" 
				:class="{ active: currentFilter === 'elderly' }"
				@click="switchFilter('elderly')"
			>
				助老关怀
			</view>
			<view 
				class="filter-item" 
				:class="{ active: currentFilter === 'environment' }"
				@click="switchFilter('environment')"
			>
				环境保护
			</view>
		</view>

		<!-- 志愿项目列表 -->
		<view class="project-list">
			<!-- 项目1：带图片的大卡片 -->
			<view class="project-card featured" v-if="currentFilter === 'all' || currentFilter === 'environment'">
				<image class="project-image" src="/static/volunteer/park.jpg" mode="aspectFill"></image>
				<view class="project-tag">环境保护</view>
				<view class="project-content">
					<view class="project-header">
						<view class="project-title">周末中央公园清洁行动</view>
						<view class="status-tag recruiting">正在招募</view>
					</view>
					<view class="project-desc">协助社区维护中央公园的环境卫生。工作内容包括清理散落的垃圾、修剪低矮灌木以及向游客宣传环保知识。无需经验，提供必需工具和饮用水。</view>
					<view class="project-meta">
						<view class="meta-item">
							<text class="meta-icon">📅</text>
							<text>本周六 09:00-12:00</text>
						</view>
						<view class="meta-item">
							<text class="meta-icon">👥</text>
							<text>已报 12/20人</text>
						</view>
					</view>
					<view class="join-btn" @click="joinProject('周末中央公园清洁行动')">立即报名</view>
				</view>
			</view>

			<!-- 项目2：紧凑型卡片 -->
			<view class="project-card compact" v-if="currentFilter === 'all' || currentFilter === 'elderly'">
				<view class="compact-left">
					<view class="compact-icon-wrap">
						<text class="compact-icon">🤝</text>
					</view>
				</view>
				<view class="compact-right">
					<view class="compact-title">阳光敬老院探访</view>
					<view class="compact-desc">为社区孤寡老人送去温暖与陪伴。活动包含读报、聊天、协助整理内务等日常互动。用您的耐心点亮他们的周末。</view>
					<view class="compact-meta">
						<view class="meta-row">
							<text class="meta-label">时间</text>
							<text class="meta-value">本周日 14:00</text>
						</view>
						<view class="meta-row">
							<text class="meta-label">地点</text>
							<text class="meta-value">阳光敬老院</text>
						</view>
					</view>
					<view class="detail-link" @click="viewDetail('阳光敬老院探访')">
						<text>了解详情</text>
					</view>
				</view>
			</view>

			<!-- 项目3：紧凑型卡片 -->
			<view class="project-card compact" v-if="currentFilter === 'all'">
				<view class="compact-left">
					<view class="compact-icon-wrap" style="background-color: #e8e0f0;">
						<text class="compact-icon">📚</text>
					</view>
				</view>
				<view class="compact-right">
					<view class="compact-title">社区图书管理员</view>
					<view class="compact-desc">协助图书管理员进行新书上架、旧书修补以及读者借阅引导。适合喜爱安静环境、做事细致耐心的您参与。</view>
					<view class="compact-meta">
						<view class="meta-row">
							<text class="meta-label">要求</text>
							<text class="meta-value">年满18周岁</text>
						</view>
						<view class="meta-row">
							<text class="meta-label">时长</text>
							<text class="meta-value">每周至少2小时</text>
						</view>
					</view>
					<view class="detail-link" @click="viewDetail('社区图书管理员')">
						<text>了解详情</text>
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
				// 当前筛选
				currentFilter: 'all'
			}
		},
		methods: {
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 查看志愿时长
			viewHours() {
				uni.showToast({
					title: '查看我的志愿时长',
					icon: 'none'
				})
			},
			// 切换筛选
			switchFilter(filter) {
				this.currentFilter = filter
			},
			// 报名项目
			joinProject(name) {
				uni.showModal({
					title: '确认报名',
					content: `确认报名参加"${name}"吗？`,
					success: (res) => {
						if (res.confirm) {
							uni.showToast({
								title: '报名成功',
								icon: 'success'
							})
						}
					}
				})
			},
			// 查看详情
			viewDetail(name) {
				uni.showToast({
					title: `查看: ${name}`,
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

	/* 顶部横幅 */
	.banner-card {
		margin: 20rpx 30rpx;
		background: linear-gradient(135deg, #4a8a8b 0%, #6ba8a9 100%);
		border-radius: 24rpx;
		padding: 40rpx;
		color: #ffffff;
	}

	.banner-title {
		font-size: 40rpx;
		font-weight: bold;
		line-height: 1.4;
		margin-bottom: 16rpx;
	}

	.banner-desc {
		font-size: 24rpx;
		color: rgba(255, 255, 255, 0.9);
		line-height: 1.6;
		margin-bottom: 30rpx;
	}

	.banner-btn {
		display: inline-block;
		background-color: rgba(255, 255, 255, 0.2);
		color: #ffffff;
		font-size: 26rpx;
		padding: 16rpx 32rpx;
		border-radius: 30rpx;
		border: 1rpx solid rgba(255, 255, 255, 0.3);
	}

	/* 分类筛选 */
	.filter-section {
		display: flex;
		gap: 16rpx;
		padding: 20rpx 30rpx;
	}

	.filter-item {
		padding: 12rpx 28rpx;
		border-radius: 30rpx;
		font-size: 26rpx;
		color: #666666;
		background-color: #f0f0f0;
	}

	.filter-item.active {
		background-color: #2c7a7b;
		color: #ffffff;
	}

	/* 项目列表 */
	.project-list {
		padding: 0 30rpx;
	}

	/* 特色项目卡片（带图片） */
	.project-card.featured {
		background-color: #ffffff;
		border-radius: 20rpx;
		overflow: hidden;
		margin-bottom: 24rpx;
	}

	.project-image {
		width: 100%;
		height: 300rpx;
	}

	.project-tag {
		position: absolute;
		margin-top: -40rpx;
		margin-left: 24rpx;
		background-color: #2c7a7b;
		color: #ffffff;
		font-size: 22rpx;
		padding: 8rpx 20rpx;
		border-radius: 20rpx;
	}

	.project-content {
		padding: 24rpx;
	}

	.project-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 12rpx;
	}

	.project-title {
		font-size: 32rpx;
		font-weight: bold;
		color: #333333;
		flex: 1;
	}

	.status-tag {
		font-size: 20rpx;
		padding: 4rpx 12rpx;
		border-radius: 8rpx;
		flex-shrink: 0;
		margin-left: 12rpx;
	}

	.status-tag.recruiting {
		background-color: #e8f4f8;
		color: #2c7a7b;
	}

	.project-desc {
		font-size: 24rpx;
		color: #666666;
		line-height: 1.6;
		margin-bottom: 20rpx;
	}

	.project-meta {
		display: flex;
		gap: 24rpx;
		margin-bottom: 24rpx;
	}

	.meta-item {
		display: flex;
		align-items: center;
		font-size: 24rpx;
		color: #999999;
	}

	.meta-icon {
		margin-right: 6rpx;
		font-size: 24rpx;
	}

	.join-btn {
		background-color: #2c7a7b;
		color: #ffffff;
		font-size: 28rpx;
		font-weight: bold;
		text-align: center;
		padding: 20rpx 0;
		border-radius: 30rpx;
	}

	/* 紧凑型项目卡片 */
	.project-card.compact {
		display: flex;
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 24rpx;
		margin-bottom: 20rpx;
	}

	.compact-left {
		margin-right: 20rpx;
		flex-shrink: 0;
	}

	.compact-icon-wrap {
		width: 80rpx;
		height: 80rpx;
		background-color: #e8f4f8;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.compact-icon {
		font-size: 40rpx;
	}

	.compact-right {
		flex: 1;
	}

	.compact-title {
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 10rpx;
	}

	.compact-desc {
		font-size: 24rpx;
		color: #666666;
		line-height: 1.5;
		margin-bottom: 16rpx;
	}

	.compact-meta {
		background-color: #f5f7fa;
		border-radius: 12rpx;
		padding: 16rpx;
		margin-bottom: 16rpx;
	}

	.meta-row {
		display: flex;
		justify-content: space-between;
		margin-bottom: 8rpx;
	}

	.meta-row:last-child {
		margin-bottom: 0;
	}

	.meta-label {
		font-size: 24rpx;
		color: #999999;
	}

	.meta-value {
		font-size: 24rpx;
		color: #333333;
	}

	.detail-link {
		font-size: 26rpx;
		color: #2c7a7b;
	}
</style>
