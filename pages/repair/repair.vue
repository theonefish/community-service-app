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
			<view class="page-main-title">物业报修</view>
			<view class="page-desc">请填写报修信息，我们将尽快安排维修人员上门处理。</view>
		</view>

		<!-- 报修表单 -->
		<view class="form-section">
			<!-- 报修类型 -->
			<view class="form-item">
				<view class="form-label">报修类型 <text class="required">*</text></view>
				<view class="type-grid">
					<view 
						class="type-item" 
						v-for="(item, index) in repairTypes" 
						:key="index"
						:class="{ active: selectedType === item.value }"
						@click="selectType(item.value)"
					>
						<text class="type-icon">{{ item.icon }}</text>
						<text class="type-name">{{ item.label }}</text>
					</view>
				</view>
			</view>

			<!-- 报修地址 -->
			<view class="form-item">
				<view class="form-label">报修地址 <text class="required">*</text></view>
				<view class="input-wrap">
					<picker mode="selector" :range="addressList" :value="selectedAddress" @change="onAddressChange">
						<view class="picker-value">
							<text>{{ addressList[selectedAddress] }}</text>
							<text class="picker-arrow">></text>
						</view>
					</picker>
				</view>
			</view>

			<!-- 详细地址 -->
			<view class="form-item">
				<view class="form-label">详细地址</view>
				<input 
					class="form-input" 
					placeholder="请输入门牌号、楼层等详细信息"
					placeholder-class="input-placeholder"
					v-model="detailAddress"
				/>
			</view>

			<!-- 报修描述 -->
			<view class="form-item">
				<view class="form-label">问题描述 <text class="required">*</text></view>
				<textarea 
					class="form-textarea" 
					placeholder="请描述具体问题，以便我们更好地为您服务..."
					placeholder-class="input-placeholder"
					v-model="description"
					maxlength="200"
				/>
				<view class="word-count">{{ description.length }}/200</view>
			</view>

			<!-- 上传图片 -->
			<view class="form-item">
				<view class="form-label">上传图片（选填）</view>
				<view class="upload-wrap">
					<view class="upload-list">
						<view class="upload-item" v-for="(img, index) in imageList" :key="index">
							<image class="upload-img" :src="img" mode="aspectFill"></image>
							<view class="delete-btn" @click="deleteImage(index)">×</view>
						</view>
						<view class="upload-btn" @click="chooseImage" v-if="imageList.length < 6">
							<text class="upload-icon">📷</text>
							<text class="upload-text">{{ imageList.length }}/6</text>
						</view>
					</view>
				</view>
			</view>

			<!-- 预约时间 -->
			<view class="form-item">
				<view class="form-label">预约上门时间</view>
				<view class="time-options">
					<view 
						class="time-option" 
						v-for="(item, index) in timeOptions" 
						:key="index"
						:class="{ active: selectedTime === item.value }"
						@click="selectTime(item.value)"
					>
						{{ item.label }}
					</view>
				</view>
			</view>

			<!-- 联系人信息 -->
			<view class="form-item">
				<view class="form-label">联系人 <text class="required">*</text></view>
				<input 
					class="form-input" 
					placeholder="请输入联系人姓名"
					placeholder-class="input-placeholder"
					v-model="contactName"
				/>
			</view>

			<view class="form-item">
				<view class="form-label">联系电话 <text class="required">*</text></view>
				<input 
					class="form-input" 
					placeholder="请输入联系电话"
					placeholder-class="input-placeholder"
					v-model="contactPhone"
					type="number"
				/>
			</view>
		</view>

		<!-- 提交按钮 -->
		<view class="submit-section">
			<view class="submit-btn" @click="submitRepair">提交报修</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 报修类型
				selectedType: '',
				repairTypes: [
					{ label: '水电维修', value: 'water', icon: '💧' },
					{ label: '家电维修', value: 'appliance', icon: '🔌' },
					{ label: '门窗维修', value: 'door', icon: '🚪' },
					{ label: '墙面/地面', value: 'wall', icon: '🧱' },
					{ label: '管道疏通', value: 'pipe', icon: '🚿' },
					{ label: '其他问题', value: 'other', icon: '🔧' }
				],
				// 地址选择
				selectedAddress: 0,
				addressList: ['A区1栋', 'A区2栋', 'A区3栋', 'B区1栋', 'B区2栋', 'C区1栋'],
				// 详细地址
				detailAddress: '',
				// 问题描述
				description: '',
				// 图片列表
				imageList: [],
				// 时间选择
				selectedTime: '',
				timeOptions: [
					{ label: '尽快上门', value: 'asap' },
					{ label: '今天', value: 'today' },
					{ label: '明天', value: 'tomorrow' },
					{ label: '后天', value: 'day_after' }
				],
				// 联系人
				contactName: '',
				contactPhone: ''
			}
		},
		methods: {
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 选择报修类型
			selectType(value) {
				this.selectedType = value
			},
			// 地址选择变化
			onAddressChange(e) {
				this.selectedAddress = e.detail.value
			},
			// 选择时间
			selectTime(value) {
				this.selectedTime = value
			},
			// 选择图片
			chooseImage() {
				uni.chooseImage({
					count: 6 - this.imageList.length,
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
			// 提交报修
			submitRepair() {
				// 表单验证
				if (!this.selectedType) {
					uni.showToast({ title: '请选择报修类型', icon: 'none' })
					return
				}
				if (!this.description.trim()) {
					uni.showToast({ title: '请描述问题', icon: 'none' })
					return
				}
				if (!this.contactName.trim()) {
					uni.showToast({ title: '请输入联系人', icon: 'none' })
					return
				}
				if (!this.contactPhone.trim()) {
					uni.showToast({ title: '请输入联系电话', icon: 'none' })
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
				this.detailAddress = ''
				this.description = ''
				this.imageList = []
				this.selectedTime = ''
				this.contactName = ''
				this.contactPhone = ''
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
		font-size: 28rpx;
		color: #333333;
		margin-bottom: 16rpx;
		font-weight: bold;
	}

	.required {
		color: #e64340;
	}

	/* 报修类型网格 */
	.type-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 16rpx;
	}

	.type-item {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 24rpx 0;
		background-color: #f5f7fa;
		border-radius: 16rpx;
		border: 2rpx solid transparent;
	}

	.type-item.active {
		background-color: #e8f4f8;
		border-color: #2c7a7b;
	}

	.type-icon {
		font-size: 40rpx;
		margin-bottom: 8rpx;
	}

	.type-name {
		font-size: 24rpx;
		color: #666666;
	}

	.type-item.active .type-name {
		color: #2c7a7b;
		font-weight: bold;
	}

	/* 输入框 */
	.input-wrap {
		background-color: #f5f7fa;
		border-radius: 12rpx;
		padding: 20rpx 24rpx;
	}

	.picker-value {
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: 28rpx;
		color: #333333;
	}

	.picker-arrow {
		font-size: 28rpx;
		color: #999999;
	}

	.form-input {
		background-color: #f5f7fa;
		border-radius: 12rpx;
		padding: 20rpx 24rpx;
		font-size: 28rpx;
		color: #333333;
	}

	.input-placeholder {
		color: #cccccc;
		font-size: 28rpx;
	}

	/* 文本域 */
	.form-textarea {
		background-color: #f5f7fa;
		border-radius: 12rpx;
		padding: 20rpx 24rpx;
		font-size: 28rpx;
		color: #333333;
		width: 100%;
		height: 200rpx;
		box-sizing: border-box;
	}

	.word-count {
		text-align: right;
		font-size: 22rpx;
		color: #999999;
		margin-top: 8rpx;
	}

	/* 图片上传 */
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
		font-size: 22rpx;
		color: #999999;
	}

	/* 时间选项 */
	.time-options {
		display: flex;
		flex-wrap: wrap;
		gap: 16rpx;
	}

	.time-option {
		padding: 16rpx 32rpx;
		background-color: #f5f7fa;
		border-radius: 30rpx;
		font-size: 26rpx;
		color: #666666;
		border: 2rpx solid transparent;
	}

	.time-option.active {
		background-color: #e8f4f8;
		border-color: #2c7a7b;
		color: #2c7a7b;
		font-weight: bold;
	}

	/* 提交按钮 */
	.submit-section {
		margin: 40rpx 30rpx;
	}

	.submit-btn {
		background-color: #2c7a7b;
		color: #ffffff;
		font-size: 32rpx;
		font-weight: bold;
		text-align: center;
		padding: 28rpx 0;
		border-radius: 40rpx;
	}
</style>
