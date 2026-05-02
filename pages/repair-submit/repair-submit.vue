<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="custom-nav">
			<view class="nav-left" @click="goBack">
				<text class="back-arrow">←</text>
			</view>
			<view class="nav-title">社区服务</view>
			<view class="nav-right">
				<image class="avatar-small" src="/static/avatar/default.png" mode="aspectFill"></image>
			</view>
		</view>

		<!-- 页面标题 -->
		<view class="page-title-section">
			<view class="page-main-title">提交维修申请</view>
			<view class="page-desc">请填写下方表单，我们的专业团队将尽快为您处理。</view>
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
				placeholder="请详细描述您遇到的问题..."
				placeholder-class="input-placeholder"
				v-model="description"
				maxlength="300"
			/>
		</view>

		<!-- 上传照片 -->
		<view class="form-section">
			<view class="upload-area" @click="chooseImage" v-if="imageList.length === 0">
				<text class="upload-icon">📷</text>
				<text class="upload-text">点击上传照片</text>
				<text class="upload-hint">支持 JPG, PNG, 最大 5MB</text>
			</view>
			<view class="upload-list" v-else>
				<view class="upload-item" v-for="(img, index) in imageList" :key="index">
					<image class="upload-img" :src="img" mode="aspectFill"></image>
					<view class="delete-btn" @click="deleteImage(index)">×</view>
				</view>
				<view class="upload-btn" @click="chooseImage" v-if="imageList.length < 3">
					<text class="add-icon">+</text>
				</view>
			</view>
		</view>

		<!-- 偏好联系时间 -->
		<view class="form-section">
			<view class="form-label">偏好联系时间</view>
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
			<view class="submit-btn" @click="submitRepair">提交申请</view>
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
					{ label: '水管维修', value: 'plumbing', icon: '🔧' },
					{ label: '电路检修', value: 'electrical', icon: '⚡' },
					{ label: '家电维修', value: 'appliance', icon: '📺' },
					{ label: '其他服务', value: 'other', icon: '⋯' }
				],
				// 问题描述
				description: '',
				// 图片列表
				imageList: [],
				// 时间选择
				selectedTime: '',
				timeOptions: [
					{ label: '早上 (08:00 - 12:00)', value: 'morning' },
					{ label: '下午 (13:00 - 17:00)', value: 'afternoon' },
					{ label: '晚上 (18:00 - 21:00)', value: 'evening' }
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
			submitRepair() {
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
					uni.showToast({ title: '请选择偏好联系时间', icon: 'none' })
					return
				}

				uni.showModal({
					title: '确认提交',
					content: '确认提交维修申请吗？',
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
	}

	/* 网格图标 */
	.grid-icon {
		display: grid;
		grid-template-columns: 1fr 1fr;
		grid-template-rows: 1fr 1fr;
		gap: 4rpx;
		width: 40rpx;
		height: 40rpx;
	}

	.grid-cell {
		background-color: #2c7a7b;
		border-radius: 2rpx;
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

	/* 上传区域 */
	.upload-area {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 60rpx 0;
		background-color: #f5f7fa;
		border-radius: 16rpx;
		border: 2rpx dashed #cccccc;
	}

	.upload-icon {
		font-size: 56rpx;
		margin-bottom: 12rpx;
	}

	.upload-text {
		font-size: 28rpx;
		color: #666666;
		margin-bottom: 8rpx;
	}

	.upload-hint {
		font-size: 22rpx;
		color: #999999;
	}

	/* 上传列表 */
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
		align-items: center;
		justify-content: center;
		border: 2rpx dashed #cccccc;
	}

	.add-icon {
		font-size: 48rpx;
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
