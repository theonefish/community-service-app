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
			<view class="page-main-title">投诉建议</view>
			<view class="page-desc">您的反馈是我们提升服务质量的动力。请详细描述您遇到的问题或建议，我们将尽快处理。</view>
		</view>

		<!-- 反馈表单 -->
		<view class="form-section">
			<!-- 反馈类型 -->
			<view class="form-item">
				<view class="form-label">
					<text class="label-icon">☸️</text>
					<text>反馈类型</text>
				</view>
				<view class="type-list">
					<view 
						class="type-tag" 
						v-for="(item, index) in feedbackTypes" 
						:key="index"
						:class="{ active: selectedType === item.value }"
						@click="selectType(item.value)"
					>
						{{ item.label }}
					</view>
				</view>
			</view>

			<!-- 详细描述 -->
			<view class="form-item">
				<view class="form-label">
					<text class="label-icon">📝</text>
					<text>详细描述</text>
				</view>
				<textarea 
					class="form-textarea" 
					placeholder="请详细描述您的建议或遇到的问题，以便我们更好地为您服务..."
					placeholder-class="input-placeholder"
					v-model="description"
					maxlength="500"
				/>
			</view>

			<!-- 上传图片 -->
			<view class="form-item">
				<view class="upload-list">
					<view class="upload-item" v-for="(img, index) in imageList" :key="index">
						<image class="upload-img" :src="img" mode="aspectFill"></image>
						<view class="delete-btn" @click="deleteImage(index)">×</view>
					</view>
					<view class="upload-btn" @click="chooseImage" v-if="imageList.length < 4">
						<text class="upload-icon">📷</text>
						<text class="upload-text">添加图片</text>
					</view>
				</view>
			</view>
		</view>

		<!-- 联系方式 -->
		<view class="form-section">
			<view class="contact-header">
				<view class="form-label">
					<text class="label-icon">📧</text>
					<text>联系方式</text>
				</view>
				<view class="anonymous-switch">
					<text class="switch-label">匿名提交</text>
					<switch :checked="isAnonymous" @change="toggleAnonymous" color="#2c7a7b" />
				</view>
			</view>

			<view class="contact-form" v-if="!isAnonymous">
				<view class="contact-item">
					<text class="contact-icon">👤</text>
					<input 
						class="contact-input" 
						placeholder="您的姓名(选填)"
						placeholder-class="input-placeholder"
						v-model="contactName"
					/>
				</view>
				<view class="contact-item">
					<text class="contact-icon">📱</text>
					<input 
						class="contact-input" 
						placeholder="联系电话(选填)"
						placeholder-class="input-placeholder"
						v-model="contactPhone"
						type="number"
					/>
				</view>
				<view class="contact-item">
					<text class="contact-icon">🏠</text>
					<input 
						class="contact-input" 
						placeholder="楼栋房号(选填)"
						placeholder-class="input-placeholder"
						v-model="roomNumber"
					/>
				</view>
			</view>
		</view>

		<!-- 提交按钮 -->
		<view class="submit-section">
			<view class="submit-btn" @click="submitFeedback">提交反馈</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 反馈类型
				selectedType: '',
				feedbackTypes: [
					{ label: '噪音扰民', value: 'noise' },
					{ label: '环境卫生', value: 'hygiene' },
					{ label: '安保问题', value: 'security' },
					{ label: '服务态度', value: 'attitude' },
					{ label: '设施报修', value: 'facility' },
					{ label: '其他建议', value: 'other' }
				],
				// 问题描述
				description: '',
				// 图片列表
				imageList: [],
				// 是否匿名
				isAnonymous: false,
				// 联系人信息
				contactName: '',
				contactPhone: '',
				roomNumber: ''
			}
		},
		methods: {
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 选择反馈类型 - 设施报修直接跳转到报修申请页
			selectType(value) {
				if (value === 'facility') {
					uni.navigateTo({
						url: '/pages/repair-apply/repair-apply'
					})
					return
				}
				this.selectedType = value
			},
			// 选择图片
			chooseImage() {
				uni.chooseImage({
					count: 4 - this.imageList.length,
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
			// 切换匿名
			toggleAnonymous(e) {
				this.isAnonymous = e.detail.value
			},
			// 提交反馈
			submitFeedback() {
				// 表单验证
				if (!this.selectedType) {
					uni.showToast({ title: '请选择反馈类型', icon: 'none' })
					return
				}
				if (!this.description.trim()) {
					uni.showToast({ title: '请描述您的问题或建议', icon: 'none' })
					return
				}

				uni.showModal({
					title: '确认提交',
					content: '确认提交您的反馈吗？',
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
				this.isAnonymous = false
				this.contactName = ''
				this.contactPhone = ''
				this.roomNumber = ''
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

	.form-item {
		margin-bottom: 30rpx;
	}

	.form-item:last-child {
		margin-bottom: 0;
	}

	.form-label {
		display: flex;
		align-items: center;
		font-size: 28rpx;
		color: #333333;
		margin-bottom: 20rpx;
		font-weight: bold;
	}

	.label-icon {
		margin-right: 12rpx;
		font-size: 32rpx;
	}

	/* 反馈类型标签 */
	.type-list {
		display: flex;
		flex-wrap: wrap;
		gap: 16rpx;
	}

	.type-tag {
		padding: 16rpx 32rpx;
		background-color: #f5f7fa;
		border-radius: 30rpx;
		font-size: 26rpx;
		color: #666666;
		border: 2rpx solid transparent;
	}

	.type-tag.active {
		background-color: #2c7a7b;
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
		height: 240rpx;
		box-sizing: border-box;
	}

	.input-placeholder {
		color: #cccccc;
		font-size: 28rpx;
	}

	/* 图片上传 */
	.upload-list {
		display: flex;
		flex-wrap: wrap;
		gap: 16rpx;
	}

	.upload-item {
		position: relative;
		width: 140rpx;
		height: 140rpx;
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
		width: 32rpx;
		height: 32rpx;
		background-color: #e64340;
		color: #ffffff;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 24rpx;
	}

	.upload-btn {
		width: 140rpx;
		height: 140rpx;
		background-color: #f5f7fa;
		border-radius: 12rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		border: 2rpx dashed #cccccc;
	}

	.upload-icon {
		font-size: 40rpx;
		margin-bottom: 8rpx;
	}

	.upload-text {
		font-size: 22rpx;
		color: #999999;
	}

	/* 联系方式头部 */
	.contact-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 20rpx;
	}

	.anonymous-switch {
		display: flex;
		align-items: center;
	}

	.switch-label {
		font-size: 24rpx;
		color: #999999;
		margin-right: 12rpx;
	}

	/* 联系方式表单 */
	.contact-form {
		display: flex;
		flex-direction: column;
		gap: 16rpx;
	}

	.contact-item {
		display: flex;
		align-items: center;
		background-color: #f5f7fa;
		border-radius: 12rpx;
		padding: 20rpx 24rpx;
	}

	.contact-icon {
		font-size: 32rpx;
		margin-right: 16rpx;
	}

	.contact-input {
		flex: 1;
		font-size: 28rpx;
		color: #333333;
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
