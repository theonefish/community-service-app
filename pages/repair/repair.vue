<template>
	<view class="container">
		<NavBar title="物业报修" :showBack="true" :showAvatar="true" bgColor="#2c7a7b" />

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

			<!-- 上传图片（使用 UploadImages 组件） -->
			<view class="form-item">
				<view class="form-label">上传图片（选填）</view>
				<UploadImages :maxCount="6" :imageList="imageList" @update:imageList="imageList = $event" />
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
		<view class="submit-section" style="padding: 20px 16px;">
			<view class="primary-btn" @click="submitRepair">提交报修</view>
		</view>
	</view>
</template>

<script>
	import { repairApi } from '@/api/index.js'

	export default {
		data() {
			return {
				// 报修类型（从 API 获取）
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
				contactPhone: '',
				// 提交中状态
				submitting: false
			}
		},
		methods: {
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
			// 提交报修（通过 API）
			async submitRepair() {
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
					success: async (res) => {
						if (res.confirm) {
							try {
								this.submitting = true
								await repairApi.submit({
									type: this.selectedType,
									description: this.description,
									time: this.selectedTime,
									images: this.imageList,
									contactName: this.contactName,
									contactPhone: this.contactPhone,
									address: this.addressList[this.selectedAddress],
									detailAddress: this.detailAddress
								})
								uni.showToast({ title: '提交成功', icon: 'success' })
								this.resetForm()
							} catch (err) {
								uni.showToast({ title: '提交失败，请重试', icon: 'none' })
							} finally {
								this.submitting = false
							}
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

	/* 提交按钮容器 */
	.submit-section {
		margin: 40rpx 30rpx;
	}
</style>
