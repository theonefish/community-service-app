<template>
	<view class="container">
		<NavBar title="提交维修申请" :showBack="true" :showAvatar="true" bgColor="#2c7a7b" />

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
			<view class="form-label">上传照片</view>
			<UploadImages :maxCount="3" :imageList="imageList" @update:imageList="imageList = $event" />
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
		<view class="submit-section" style="padding: 20px 16px;">
			<view class="primary-btn" @click="submitRepair">提交申请</view>
		</view>
	</view>
</template>

<script>
	import { repairApi } from '@/api/index.js'

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
				// 提交中状态
				submitting: false,
				timeOptions: [
					{ label: '早上 (08:00 - 12:00)', value: 'morning' },
					{ label: '下午 (13:00 - 17:00)', value: 'afternoon' },
					{ label: '晚上 (18:00 - 21:00)', value: 'evening' }
				]
			}
		},
		methods: {
			// 选择服务类型
			selectType(value) {
				this.selectedType = value
			},
			// 选择时间
			selectTime(value) {
				this.selectedTime = value
			},
			// 提交申请（通过 API）
			async submitRepair() {
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
					success: async (res) => {
						if (res.confirm) {
							try {
								this.submitting = true
								await repairApi.submit({
									type: this.selectedType,
									description: this.description,
									time: this.selectedTime,
									images: this.imageList
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

	/* 提交按钮容器 */
	.submit-section {
		margin: 40rpx 30rpx;
	}
</style>
