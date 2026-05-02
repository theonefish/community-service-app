<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="page-header">
			<view class="back-btn" @click="goBack">
				<text class="back-arrow">←</text>
				<text class="back-text">返回</text>
			</view>
			<view class="header-title">积分与优惠券</view>
			<view class="header-right"></view>
		</view>

		<!-- 积分余额卡片 -->
		<view class="points-card">
			<view class="points-bg">
				<view class="star-decoration">⭐</view>
			</view>
			<view class="points-label">我的积分余额</view>
			<view class="points-value">
				<text class="points-number">12,850</text>
				<text class="points-unit">积分</text>
			</view>
			<view class="points-actions">
				<view class="action-btn btn-primary" @click="exchangePoints">立即兑换</view>
				<view class="action-btn btn-secondary" @click="pointsRule">积分规则</view>
			</view>
		</view>

		<!-- 积分明细 -->
		<view class="section">
			<view class="section-header">
				<text class="section-title">积分明细</text>
				<view class="section-more" @click="viewAllPoints">
					<text>查看全部</text>
				</view>
			</view>
			<view class="points-list">
				<view class="points-item" v-for="(item, index) in pointsList" :key="index">
					<view class="points-icon-wrap" :style="{ backgroundColor: item.bgColor }">
						<text class="points-icon">{{ item.icon }}</text>
					</view>
					<view class="points-info">
						<view class="points-item-title">{{ item.title }}</view>
						<view class="points-item-desc">{{ item.date }} · {{ item.desc }}</view>
					</view>
					<view class="points-change" :class="{ minus: item.value < 0 }">
						{{ item.value > 0 ? '+' : '' }}{{ item.value }}
					</view>
				</view>
			</view>
		</view>

		<!-- 我的优惠券 -->
		<view class="section">
			<view class="coupon-tabs">
				<view 
					class="tab-item" 
					:class="{ active: currentTab === 0 }"
					@click="switchTab(0)"
				>
					待使用(3)
				</view>
				<view 
					class="tab-item" 
					:class="{ active: currentTab === 1 }"
					@click="switchTab(1)"
				>
					已失效
				</view>
			</view>

			<!-- 优惠券列表 -->
			<view class="coupon-list" v-if="currentTab === 0">
				<!-- 消费券 -->
				<view class="coupon-card money-coupon">
					<view class="coupon-left">
						<view class="coupon-amount">
							<text class="amount-symbol">¥</text>
							<text class="amount-number">50</text>
						</view>
						<view class="coupon-condition">满200可用</view>
					</view>
					<view class="coupon-right">
						<view class="coupon-name">全场通用消费券</view>
						<view class="coupon-desc">社区指定合作超市使用</view>
						<view class="coupon-footer">
							<view class="coupon-date">📅 2023.12.31</view>
							<view class="use-btn" @click="useCoupon">去使用</view>
						</view>
					</view>
				</view>

				<!-- 服务券 -->
				<view class="coupon-card service-coupon">
					<view class="coupon-tag">停车服务</view>
					<view class="coupon-content">
						<view class="service-title">免费停车2小时</view>
						<view class="service-desc">访客或自用车均可使用，全天候有效</view>
						<view class="activate-link" @click="activateCoupon">
							<text>立即激活</text>
							<text class="link-arrow">→</text>
						</view>
					</view>
				</view>

				<!-- 折扣券 -->
				<view class="coupon-card discount-coupon">
					<view class="coupon-left">
						<view class="discount-amount">
							<text class="discount-number">8.5</text>
							<text class="discount-unit">折</text>
						</view>
						<view class="discount-type">洗车专用</view>
					</view>
					<view class="coupon-right">
						<view class="coupon-name">精致洗车体验券</view>
						<view class="coupon-desc">含内饰除菌与除尘服务</view>
						<view class="coupon-footer">
							<view class="coupon-date">📅 2023.11.15</view>
							<view class="use-btn" @click="useCoupon">去使用</view>
						</view>
					</view>
				</view>
			</view>

			<!-- 已失效空状态 -->
			<view class="empty-state" v-if="currentTab === 1">
				<view class="empty-icon">🗑️</view>
				<view class="empty-text">暂无已失效优惠券</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 当前优惠券标签页
				currentTab: 0,
				// 积分明细数据
				pointsList: [
					{
						title: '社区公益活动奖励',
						date: '2023年10月24日',
						desc: '垃圾分类宣传',
						value: 500,
						icon: '🌱',
						bgColor: '#e8f4f8'
					},
					{
						title: '物业费缴纳成功',
						date: '2023年10月20日',
						desc: '线上自动缴费',
						value: 200,
						icon: '🏠',
						bgColor: '#e8f4f8'
					},
					{
						title: '兑换超市代金券',
						date: '2023年10月15日',
						desc: '50元无门槛',
						value: -1000,
						icon: '🎫',
						bgColor: '#fce8e8'
					}
				]
			}
		},
		methods: {
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 立即兑换
			exchangePoints() {
				uni.showToast({
					title: '立即兑换',
					icon: 'none'
				})
			},
			// 积分规则
			pointsRule() {
				uni.showToast({
					title: '积分规则',
					icon: 'none'
				})
			},
			// 查看全部积分明细
			viewAllPoints() {
				uni.showToast({
					title: '查看全部',
					icon: 'none'
				})
			},
			// 切换优惠券标签
			switchTab(index) {
				this.currentTab = index
			},
			// 使用优惠券 - 跳转到缴费中心使用
			useCoupon() {
				uni.navigateTo({
					url: '/pages/payment/payment'
				})
			},
			// 激活优惠券 - 跳转到缴费中心
			activateCoupon() {
				uni.navigateTo({
					url: '/pages/payment/payment'
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
		display: flex;
		align-items: center;
		width: 120rpx;
	}

	.back-arrow {
		font-size: 36rpx;
		color: #333333;
		margin-right: 8rpx;
	}

	.back-text {
		font-size: 28rpx;
		color: #333333;
	}

	.header-title {
		font-size: 34rpx;
		font-weight: bold;
		color: #333333;
	}

	.header-right {
		width: 120rpx;
	}

	/* 积分余额卡片 */
	.points-card {
		position: relative;
		margin: 20rpx 30rpx;
		background: linear-gradient(135deg, #2c5f60 0%, #3a7a7b 100%);
		border-radius: 24rpx;
		padding: 40rpx;
		overflow: hidden;
	}

	.points-bg {
		position: absolute;
		top: 0;
		right: 0;
		width: 200rpx;
		height: 200rpx;
		opacity: 0.1;
	}

	.star-decoration {
		font-size: 160rpx;
		position: absolute;
		top: -20rpx;
		right: -20rpx;
	}

	.points-label {
		font-size: 24rpx;
		color: rgba(255, 255, 255, 0.8);
		margin-bottom: 16rpx;
	}

	.points-value {
		display: flex;
		align-items: baseline;
		margin-bottom: 30rpx;
	}

	.points-number {
		font-size: 72rpx;
		font-weight: bold;
		color: #ffffff;
		margin-right: 12rpx;
	}

	.points-unit {
		font-size: 28rpx;
		color: rgba(255, 255, 255, 0.9);
	}

	.points-actions {
		display: flex;
		gap: 20rpx;
	}

	.action-btn {
		padding: 16rpx 40rpx;
		border-radius: 30rpx;
		font-size: 28rpx;
		text-align: center;
	}

	.btn-primary {
		background-color: #ffffff;
		color: #2c7a7b;
	}

	.btn-secondary {
		background-color: rgba(255, 255, 255, 0.2);
		color: #ffffff;
		border: 1rpx solid rgba(255, 255, 255, 0.3);
	}

	/* 分区 */
	.section {
		margin: 0 30rpx 20rpx;
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

	/* 积分明细列表 */
	.points-list {
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 0 24rpx;
	}

	.points-item {
		display: flex;
		align-items: center;
		padding: 28rpx 0;
		border-bottom: 1rpx solid #f0f0f0;
	}

	.points-item:last-child {
		border-bottom: none;
	}

	.points-icon-wrap {
		width: 72rpx;
		height: 72rpx;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-right: 20rpx;
		flex-shrink: 0;
	}

	.points-icon {
		font-size: 36rpx;
	}

	.points-info {
		flex: 1;
	}

	.points-item-title {
		font-size: 28rpx;
		color: #333333;
		margin-bottom: 8rpx;
	}

	.points-item-desc {
		font-size: 22rpx;
		color: #999999;
	}

	.points-change {
		font-size: 32rpx;
		font-weight: bold;
		color: #2c7a7b;
	}

	.points-change.minus {
		color: #e64340;
	}

	/* 优惠券标签页 */
	.coupon-tabs {
		display: flex;
		gap: 20rpx;
		margin-bottom: 20rpx;
	}

	.tab-item {
		padding: 12rpx 32rpx;
		border-radius: 30rpx;
		font-size: 26rpx;
		color: #666666;
		background-color: #f0f0f0;
	}

	.tab-item.active {
		background-color: #2c7a7b;
		color: #ffffff;
	}

	/* 优惠券列表 */
	.coupon-list {
		display: flex;
		flex-direction: column;
		gap: 20rpx;
	}

	/* 通用优惠券卡片 */
	.coupon-card {
		background-color: #ffffff;
		border-radius: 20rpx;
		overflow: hidden;
		display: flex;
	}

	/* 金额优惠券 */
	.money-coupon {
		display: flex;
		padding: 0;
	}

	.coupon-left {
		width: 180rpx;
		background: linear-gradient(135deg, #e8f4f8 0%, #d0e8f0 100%);
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 30rpx 0;
		flex-shrink: 0;
	}

	.coupon-amount {
		display: flex;
		align-items: baseline;
		margin-bottom: 8rpx;
	}

	.amount-symbol {
		font-size: 28rpx;
		color: #2c7a7b;
		font-weight: bold;
	}

	.amount-number {
		font-size: 56rpx;
		font-weight: bold;
		color: #2c7a7b;
	}

	.coupon-condition {
		font-size: 22rpx;
		color: #666666;
	}

	.coupon-right {
		flex: 1;
		padding: 24rpx;
		display: flex;
		flex-direction: column;
		justify-content: center;
	}

	.coupon-name {
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 8rpx;
	}

	.coupon-desc {
		font-size: 24rpx;
		color: #999999;
		margin-bottom: 16rpx;
	}

	.coupon-footer {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.coupon-date {
		font-size: 22rpx;
		color: #999999;
	}

	.use-btn {
		background-color: #2c7a7b;
		color: #ffffff;
		font-size: 24rpx;
		padding: 10rpx 24rpx;
		border-radius: 24rpx;
	}

	/* 服务券 */
	.service-coupon {
		flex-direction: column;
		padding: 24rpx;
	}

	.coupon-tag {
		display: inline-block;
		background-color: #e8e0f0;
		color: #666666;
		font-size: 20rpx;
		padding: 4rpx 16rpx;
		border-radius: 8rpx;
		margin-bottom: 16rpx;
		align-self: flex-start;
	}

	.service-title {
		font-size: 34rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 10rpx;
	}

	.service-desc {
		font-size: 24rpx;
		color: #999999;
		margin-bottom: 16rpx;
	}

	.activate-link {
		display: flex;
		align-items: center;
		font-size: 26rpx;
		color: #2c7a7b;
	}

	.link-arrow {
		margin-left: 8rpx;
		font-size: 28rpx;
	}

	/* 折扣券 */
	.discount-coupon {
		display: flex;
		padding: 0;
	}

	.discount-amount {
		display: flex;
		align-items: baseline;
		margin-bottom: 8rpx;
	}

	.discount-number {
		font-size: 48rpx;
		font-weight: bold;
		color: #2c7a7b;
	}

	.discount-unit {
		font-size: 28rpx;
		color: #2c7a7b;
		margin-left: 4rpx;
	}

	.discount-type {
		font-size: 22rpx;
		color: #666666;
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
</style>
