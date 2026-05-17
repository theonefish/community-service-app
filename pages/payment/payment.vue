<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="page-header">
			<view class="back-btn" @click="goBack">
				<text class="back-arrow">←</text>
			</view>
			<view class="header-title">缴费中心</view>
			<view class="header-right">
				<image class="avatar-small" src="/static/avatar/default.png" mode="aspectFill"></image>
			</view>
		</view>

		<!-- 待缴总计卡片 -->
		<view class="total-card">
			<view class="total-label">当前待缴总计(元)</view>
			<view class="total-amount">¥1,280.50</view>
			<view class="total-info">
				<text class="info-icon">ℹ️</text>
				<text class="info-text">包含 3 项待处理账单</text>
			</view>
			<view class="pay-btn" @click="payAll">立即缴费</view>
		</view>

		<!-- 待缴明细 -->
		<view class="section">
			<view class="section-title">待缴明细</view>
			<view class="bill-list">
				<view class="bill-item" v-for="(item, index) in pendingBills" :key="index">
					<view class="bill-left">
						<view class="bill-icon-wrap" :style="{ backgroundColor: item.bgColor }">
							<text class="bill-icon">{{ item.icon }}</text>
						</view>
						<view class="bill-info">
							<view class="bill-name">{{ item.name }}</view>
							<view class="bill-date">{{ item.date }}</view>
							<view class="bill-detail">{{ item.detail }}</view>
						</view>
					</view>
					<view class="bill-amount">¥{{ item.amount }}</view>
				</view>
			</view>
		</view>

		<!-- 历史账单 -->
		<view class="section">
			<view class="section-header">
				<text class="section-title">历史账单</text>
				<view class="section-more" @click="viewAllHistory">
					<text>查看全部</text>
				</view>
			</view>
			<view class="history-list">
				<view class="history-item" v-for="(item, index) in historyBills" :key="index">
					<view class="history-left">
						<view class="history-icon-wrap">
							<text class="history-icon">📋</text>
						</view>
						<view class="history-info">
							<view class="history-name">{{ item.name }}</view>
							<view class="history-time">支付时间: {{ item.time }}</view>
						</view>
					</view>
					<view class="history-right">
						<view class="history-amount">¥{{ item.amount }}</view>
						<view class="history-status">{{ item.status }}</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import { paymentApi } from '@/api/index.js'

	export default {
		data() {
			return {
				// 待缴账单列表（从 API 获取）
				pendingBills: [],
				// 历史账单（从 API 获取）
				historyBills: [],
				loading: true
			}
		},
		async onLoad() {
			await this.fetchPaymentData()
		},
		methods: {
			// 从 API 获取缴费数据
			async fetchPaymentData() {
				try {
					this.loading = true
					const [pending, history] = await Promise.all([
						paymentApi.getPendingBills(),
						paymentApi.getHistoryBills()
					])
					this.pendingBills = pending || []
					this.historyBills = history || []
				} catch (err) {
					console.error('获取缴费数据失败:', err)
				} finally {
					this.loading = false
				}
			},
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 立即缴费（全部）
			async payAll() {
				uni.showModal({
					title: '确认缴费',
					content: '确认缴纳全部待缴费用吗？',
					success: async (res) => {
						if (res.confirm) {
							try {
								const ids = this.pendingBills.map(b => b.id)
								await paymentApi.pay(ids)
								uni.showToast({ title: '支付成功', icon: 'success' })
								// 刷新数据
								await this.fetchPaymentData()
							} catch (err) {
								uni.showToast({ title: '支付失败', icon: 'none' })
							}
						}
					}
				})
			},
			// 查看全部历史
			viewAllHistory() {
				uni.showToast({
					title: '查看全部历史账单',
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
		height: 60rpx;
	}

	.avatar-small {
		width: 56rpx;
		height: 56rpx;
		border-radius: 50%;
		background-color: #e0e0e0;
	}

	/* 待缴总计卡片 */
	.total-card {
		margin: 20rpx 30rpx;
		background: linear-gradient(135deg, #4a8a8b 0%, #6ba8a9 100%);
		border-radius: 24rpx;
		padding: 40rpx;
		color: #ffffff;
	}

	.total-label {
		font-size: 24rpx;
		color: rgba(255, 255, 255, 0.8);
		margin-bottom: 12rpx;
	}

	.total-amount {
		font-size: 64rpx;
		font-weight: bold;
		margin-bottom: 20rpx;
	}

	.total-info {
		display: flex;
		align-items: center;
		margin-bottom: 30rpx;
	}

	.info-icon {
		font-size: 24rpx;
		margin-right: 8rpx;
	}

	.info-text {
		font-size: 24rpx;
		color: rgba(255, 255, 255, 0.9);
	}

	.pay-btn {
		background-color: #ffffff;
		color: #2c7a7b;
		font-size: 30rpx;
		font-weight: bold;
		text-align: center;
		padding: 24rpx 0;
		border-radius: 40rpx;
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

	/* 待缴账单列表 */
	.bill-list {
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 0 24rpx;
	}

	.bill-item {
		display: flex;
		justify-content: space-between;
		align-items: flex-start;
		padding: 28rpx 0;
		border-bottom: 1rpx solid #f0f0f0;
	}

	.bill-item:last-child {
		border-bottom: none;
	}

	.bill-left {
		display: flex;
		flex: 1;
	}

	.bill-icon-wrap {
		width: 72rpx;
		height: 72rpx;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-right: 20rpx;
		flex-shrink: 0;
	}

	.bill-icon {
		font-size: 36rpx;
	}

	.bill-info {
		flex: 1;
	}

	.bill-name {
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 6rpx;
	}

	.bill-date {
		font-size: 24rpx;
		color: #999999;
		margin-bottom: 8rpx;
	}

	.bill-detail {
		font-size: 22rpx;
		color: #666666;
		background-color: #f5f7fa;
		padding: 8rpx 16rpx;
		border-radius: 8rpx;
		display: inline-block;
	}

	.bill-amount {
		font-size: 32rpx;
		font-weight: bold;
		color: #e64340;
		margin-left: 20rpx;
	}

	/* 历史账单 */
	.history-list {
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 0 24rpx;
	}

	.history-item {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 24rpx 0;
		border-bottom: 1rpx solid #f0f0f0;
	}

	.history-item:last-child {
		border-bottom: none;
	}

	.history-left {
		display: flex;
		align-items: center;
		flex: 1;
	}

	.history-icon-wrap {
		width: 64rpx;
		height: 64rpx;
		background-color: #f0f0f0;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		margin-right: 20rpx;
		flex-shrink: 0;
	}

	.history-icon {
		font-size: 32rpx;
	}

	.history-info {
		flex: 1;
	}

	.history-name {
		font-size: 28rpx;
		color: #333333;
		margin-bottom: 6rpx;
	}

	.history-time {
		font-size: 22rpx;
		color: #999999;
	}

	.history-right {
		display: flex;
		flex-direction: column;
		align-items: flex-end;
	}

	.history-amount {
		font-size: 28rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 6rpx;
	}

	.history-status {
		font-size: 22rpx;
		color: #2c7a7b;
		background-color: #e8f4f8;
		padding: 4rpx 12rpx;
		border-radius: 8rpx;
	}
</style>
