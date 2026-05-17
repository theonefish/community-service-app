<template>
	<view class="nav-bar" :style="{ background: bgColor, paddingTop: statusBarHeight + 'px' }">
		<view class="nav-bar-inner" :style="{ height: navHeight + 'px' }">
			<!-- 左侧返回按钮 -->
			<view v-if="showBack" class="nav-left" @click="handleBack">
				<view class="back-icon"></view>
			</view>
			<!-- 左侧自定义图标 -->
			<view v-if="showGrid" class="nav-left" @click="$emit('gridClick')">
				<view class="grid-icon">
					<view class="grid-dot" v-for="i in 9" :key="i"></view>
				</view>
			</view>

			<!-- 中间标题 -->
			<view class="nav-title" :class="{ 'no-back': !showBack && !showGrid }">{{ title }}</view>

			<!-- 右侧按钮 -->
			<view class="nav-right">
				<view v-if="showBell" class="bell-icon" @click="$emit('bellClick')">
					<view class="bell-body"></view>
					<view class="bell-bottom"></view>
					<view class="bell-sound"></view>
				</view>
				<view v-if="showAvatar" class="avatar-btn" @click="$emit('avatarClick')">
					<image :src="avatarSrc || '/static/avatar/default-avatar.jpg'" mode="aspectFill"></image>
				</view>
				<view v-if="showSetting" class="setting-btn" @click="$emit('settingClick')">
					<text>设置</text>
				</view>
				<slot name="right"></slot>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name: 'NavBar',
		props: {
			title: { type: String, default: '' },
			bgColor: { type: String, default: '#2c7a7b' },
			showBack: { type: Boolean, default: false },
			showGrid: { type: Boolean, default: false },
			showBell: { type: Boolean, default: false },
			showAvatar: { type: Boolean, default: false },
			showSetting: { type: Boolean, default: false },
			avatarSrc: { type: String, default: '' }
		},
		data() {
			return {
				statusBarHeight: 20,
				navHeight: 44
			}
		},
		mounted() {
			// #ifdef MP-WEIXIN
			const sysInfo = uni.getSystemInfoSync()
			this.statusBarHeight = sysInfo.statusBarHeight || 20
			// 微信小程序胶囊高度
			this.navHeight = 44
			// #endif
		},
		methods: {
			handleBack() {
				uni.navigateBack({ fail: () => uni.switchTab({ url: '/pages/index/index' }) })
			}
		}
	}
</script>

<style lang="scss">
	.nav-bar {
		width: 100%;
		position: relative;
		z-index: 999;

		.nav-bar-inner {
			display: flex;
			align-items: center;
			justify-content: space-between;
			padding: 0 16px;
		}

		.nav-left {
			width: 40px;
			height: 40px;
			display: flex;
			align-items: center;
			justify-content: center;
		}

		.back-icon {
			width: 24px;
			height: 24px;
			border-left: 3px solid #fff;
			border-bottom: 3px solid #fff;
			transform: rotate(45deg);
		}

		.grid-icon {
			width: 24px;
			height: 24px;
			display: flex;
			flex-wrap: wrap;
			justify-content: space-between;
			align-content: space-between;
			padding: 2px;

			.grid-dot {
				width: 5px;
				height: 5px;
				border-radius: 50%;
				background: #fff;
			}
		}

		.nav-title {
			font-size: 18px;
			font-weight: 600;
			color: #fff;
			flex: 1;
			text-align: center;

			&.no-back {
				margin-left: -40px;
			}
		}

		.nav-right {
			width: 40px;
			height: 40px;
			display: flex;
			align-items: center;
			justify-content: center;
			position: relative;
		}

		.bell-icon {
			width: 24px;
			height: 24px;
			position: relative;

			.bell-body {
				width: 18px;
				height: 18px;
				border: 2px solid #fff;
				border-radius: 50% 50% 0 0;
				border-bottom: none;
				position: absolute;
				bottom: 2px;
				left: 1px;
			}

			.bell-bottom {
				width: 12px;
				height: 3px;
				background: #fff;
				border-radius: 2px;
				position: absolute;
				bottom: 0;
				left: 4px;
			}

			.bell-sound {
				width: 4px;
				height: 4px;
				border-radius: 50%;
				background: #ff4757;
				position: absolute;
				top: 0;
				right: 0;
			}
		}

		.avatar-btn {
			width: 32px;
			height: 32px;
			border-radius: 50%;
			overflow: hidden;
			border: 2px solid rgba(255, 255, 255, 0.6);

			image {
				width: 100%;
				height: 100%;
			}
		}

		.setting-btn {
			color: #fff;
			font-size: 14px;
		}
	}
</style>
