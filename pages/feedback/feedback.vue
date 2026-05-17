<template>
	<view class="container">
		<NavBar title="投诉建议" :showBack="true" :showAvatar="true" bgColor="#2c7a7b" />

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

			<!-- 上传图片（使用 UploadImages 组件） -->
			<view class="form-item">
				<view class="form-label">
					<text class="label-icon">📷</text>
					<text>上传图片</text>
				</view>
				<UploadImages :maxCount="4" :imageList="imageList" @update:imageList="imageList = $event" />
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
		<view class="submit-section" style="padding: 20px 16px;">
			<view class="primary-btn" @click="submitFeedback">提交反馈</view>
		</view>
	</view>
</template>

<script>
	import { feedbackApi } from '@/api/index.js'

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
				// 提交中状态
				submitting: false,
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
			// 切换匿名
			toggleAnonymous(e) {
				this.isAnonymous = e.detail.value
			},
			// 提交反馈（通过 API）
			async submitFeedback() {
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
					success: async (res) => {
						if (res.confirm) {
							try {
								this.submitting = true
								await feedbackApi.submit({
									type: this.selectedType,
									description: this.description,
									images: this.imageList,
									isAnonymous: this.isAnonymous
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

	/* 提交按钮容器 */
	.submit-section {
		margin: 40rpx 30rpx;
	}
</style>
