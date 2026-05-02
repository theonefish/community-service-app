<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="page-header">
			<view class="back-btn" @click="goBack">
				<text class="back-arrow">←</text>
			</view>
			<view class="header-title">物业服务</view>
			<view class="header-right">
				<image class="avatar-small" src="/static/avatar/default.png" mode="aspectFill"></image>
			</view>
		</view>

		<!-- 页面标题 -->
		<view class="page-title-section">
			<view class="page-main-title">报修申请</view>
			<view class="page-desc">请详细描述您遇到的问题，我们将尽快安排专业维修人员为您服务。</view>
		</view>

		<!-- 服务类型 -->
		<view class="form-section">
			<view class="form-label">服务类型</view>
			<view class="type-grid">
				<view 
					class="type-item" 
					v-for="(item, index) in serviceTypes" 
					:key="index"
					:class="{ active: selectedType === item.value }"
					@click="selectType(item.value)"
				>
					<text class="type-icon">{{ item.icon }}</text>
					<text class="type-name">{{ item.label }}</text>
				</view>
			</view>
		</view>

		<!-- 问题描述 -->
		<view class="form-section">
			<view class="form-label">问题描述</view>
			<textarea 
				class="form-textarea" 
				placeholder="请详细描述您遇到的问题，例如：水管漏水、灯泡不亮等..."
				placeholder-class="input-placeholder"
				v-model="description"
				maxlength="300"
			/>
		</view>

		<!-- 上传照片 -->
		<view class="form-section">
			<view class="form-label">上传照片</view>
			<view class="upload-desc">提供现场照片有助于我们更准确地评估问题（最多3张）</view>
			<view class="upload-list">
				<view class="upload-item" v-for="(img, index) in imageList" :key="index">
					<image class="upload-img" :src="img" mode="aspectFill"></image>
					<view class="delete-btn" @click="deleteImage(index)">×</view>
				</view>
				<view class="upload-btn" @click="chooseImage" v-if="imageList.length < 3">
					<text class="upload-icon">📷</text>
					<text class="upload-text">添加照片</text>
				</view>
			</view>
		</view>

		<!-- 期望上门时间 -->
		<view class="form-section">
			<view class="form-label">期望上门时间</view>
			<view class="time-list">
				<view 
					class="time-item" 
					v-for="(item, index) in timeOptions" 
					:key="index"
					:class="{ active: selectedTime === item.value }"
					@click="selectTime(item.value)"
				>
					{{ item.label }}
				</view>
			</view>
		</view>

		<!-- 提交按钮 -->
		<view class="submit-section">
			<view class="submit-btn" @click="submitApply">提交申请</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 服务类型
				selectedType: '',
				serviceTypes: [
					{ label: '水暖维修', value: 'plumbing', icon: '🔧' },
					{ label: '电路维修', value: 'electrical', icon: '⚡' },
					{ label: '家电维修', value: 'appliance', icon: '📺' },
					{ label: '综合维修', value: 'general', icon: '🛠️' }
				],
				// 问题描述
				description: '',
				// 图片列表
				imageList: [],
				// 时间选择
				selectedTime: '',
				timeOptions: [
					{ label: '尽快上门', value: 'asap' },
					{ label: '明天上午 (09:00 - 12:00)', value: 'tomorrow_am' },
					{ label: '明天下午 (14:00 - 18:00)', value: 'tomorrow_pm' },
					{ label: '周末全天', value: 'weekend' }
				]
			}
		},
		methods: {
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 选择服务类型
			selectType(value) {
				this.selectedType = value
			},
			// 选择图片
			chooseImage() {
				uni.chooseImage({
					count: 3 - this.imageList.length,
					sizeType: ['compressed'],
					sourceType: ['album', 'camera'],
					success: (res) => {
						this.imageList = [...this.imageList, ...res.tempFilePaths]
					}
				})
			},
			// 删除图片
			deleteImage(index) {
				this.imageList.splice(index, 1)
			},
			// 选择时间
			selectTime(value) {
				this.selectedTime = value
			},
			// 提交申请
			submitApply() {
				// 表单验证
				if (!this.selectedType) {
					uni.showToast({ title: '请选择服务类型', icon: 'none' })
					return
				}
				if (!this.description.trim()) {
					uni.showToast({ title: '请描述问题', icon: 'none' })
					return
				}
				if (!this.selectedTime) {
					uni.showToast({ title: '请选择期望上门时间', icon: 'none' })
					return
				}

				uni.showModal({
					title: '确认提交',
					content: '确认提交报修申请吗？',
					success: (res) => {
						if (res.confirm) {
							uni.showToast({
								title: '提交成功',
								icon: 'success'
							})
							// 清空表单
							this.resetForm()
						}
					}
				})
			},
			// 重置表单
			resetForm() {
				this.selectedType = ''
				this.description = ''
				this.imageList = []
				this.selectedTime = ''
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

	/* 页面标题区域 */
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

	/* 表单区域 */
	.form-section {
		margin: 20rpx 30rpx;
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 30rpx;
	}

	.form-label {
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 24rpx;
	}

	/* 服务类型网格 */
	.type-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 20rpx;
	}

	.type-item {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 40rpx 0;
		background-color: #f5f7fa;
		border-radius: 16rpx;
		border: 2rpx solid transparent;
	}

	.type-item.active {
		background-color: #2c7a7b;
	}

	.type-icon {
		font-size: 48rpx;
		margin-bottom: 12rpx;
	}

	.type-name {
		font-size: 28rpx;
		color: #666666;
	}

	.type-item.active .type-name {
		color: #ffffff;
	}

	/* 文本域 */
	.form-textarea {
		background-color: #f5f7fa;
		border-radius: 16rpx;
		padding: 24rpx;
		font-size: 28rpx;
		color: #333333;
		width: 100%;
		height: 200rpx;
		box-sizing: border-box;
	}

	.input-placeholder {
		color: #cccccc;
		font-size: 28rpx;
	}

	/* 上传照片 */
	.upload-desc {
		font-size: 24rpx;
		color: #999999;
		margin-bottom: 20rpx;
	}

	.upload-list {
		display: flex;
		flex-wrap: wrap;
		gap: 16rpx;
	}

	.upload-item {
		position: relative;
		width: 160rpx;
		height: 160rpx;
		border-radius: 12rpx;
		overflow: hidden;
	}

	.upload-img {
		width: 100%;
		height: 100%;
	}

	.delete-btn {
		position: absolute;
		top: -8rpx;
		right: -8rpx;
		width: 36rpx;
		height: 36rpx;
		background-color: #e64340;
		color: #ffffff;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 24rpx;
	}

	.upload-btn {
		width: 160rpx;
		height: 160rpx;
		background-color: #f5f7fa;
		border-radius: 12rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		border: 2rpx dashed #cccccc;
	}

	.upload-icon {
		font-size: 48rpx;
		margin-bottom: 8rpx;
	}

	.upload-text {
		font-size: 24rpx;
		color: #999999;
	}

	/* 时间选项 */
	.time-list {
		display: flex;
		flex-direction: column;
		gap: 16rpx;
	}

	.time-item {
		padding: 24rpx 30rpx;
		background-color: #f5f7fa;
		border-radius: 12rpx;
		font-size: 28rpx;
		color: #666666;
		text-align: center;
		border: 2rpx solid transparent;
	}

	.time-item.active {
		background-color: #2c7a7b;
		color: #ffffff;
	}

	/* 提交按钮 */
	.submit-section {
		margin: 40rpx 30rpx;
	}

	.submit-btn {
		background: linear-gradient(135deg, #2c5f60 0%, #4a8a8b 100%);
		color: #ffffff;
		font-size: 32rpx;
		font-weight: bold;
		text-align: center;
		padding: 28rpx 0;
		border-radius: 40rpx;
	}
</style>
