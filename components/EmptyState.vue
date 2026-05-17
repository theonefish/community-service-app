<template>
	<view class="empty-state" :style="{ padding: padding }">
		<image v-if="image" :src="image" mode="aspectFit" class="empty-image"></image>
		<view class="empty-icon" v-else-if="icon" :class="icon"></view>
		<view class="empty-text">{{ text }}</view>
		<view v-if="showRetry" class="retry-btn" @click="$emit('retry')">重新加载</view>
		<slot></slot>
	</view>
</template>

<script>
	export default {
		name: 'EmptyState',
		props: {
			text: { type: String, default: '暂无数据' },
			image: { type: String, default: '' },
			icon: { type: String, default: '' },
			showRetry: { type: Boolean, default: false },
			padding: { type: String, default: '80px 0' }
		}
	}
</script>

<style lang="scss">
	.empty-state {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;

		.empty-image {
			width: 200px;
			height: 160px;
			margin-bottom: 16px;
		}

		.empty-icon {
			width: 80px;
			height: 80px;
			border-radius: 50%;
			background: #f0f0f0;
			margin-bottom: 16px;
		}

		.empty-text {
			font-size: 14px;
			color: #999;
		}

		.retry-btn {
			margin-top: 16px;
			padding: 8px 24px;
			border: 1px solid #2c7a7b;
			border-radius: 20px;
			color: #2c7a7b;
			font-size: 14px;
		}
	}
</style>
