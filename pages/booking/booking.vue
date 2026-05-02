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
			<view class="page-main-title">公共空间预约</view>
			<view class="page-desc">为社区居民提供高品质的共享空间，请选择您需要使用的设施并选择合适的时间段。</view>
		</view>

		<!-- 选择空间 -->
		<view class="section">
			<view class="section-label">选择空间</view>
			<view class="space-list">
				<view 
					class="space-card" 
					v-for="(item, index) in spaceList" 
					:key="index"
					:class="{ active: selectedSpace === index }"
					@click="selectSpace(index)"
				>
					<image class="space-image" :src="item.image" mode="aspectFill"></image>
					<view class="space-overlay">
						<view class="space-icon">{{ item.icon }}</view>
						<view class="space-name">{{ item.name }}</view>
					</view>
					<view class="space-info">
						<view class="space-desc">{{ item.desc }}</view>
						<view class="space-tags">
							<text class="space-tag">{{ item.price }}</text>
							<text class="space-tag">{{ item.capacity }}</text>
						</view>
					</view>
				</view>
			</view>
		</view>

		<!-- 选择日期与时间 -->
		<view class="section">
			<view class="section-label">选择日期与时间</view>
			<view class="datetime-card">
				<!-- 月份切换 -->
				<view class="month-switcher">
					<text class="month-arrow" @click="prevMonth">‹</text>
					<text class="month-text">{{ currentYear }}年{{ currentMonth }}月</text>
					<text class="month-arrow" @click="nextMonth">›</text>
				</view>

				<!-- 星期标题 -->
				<view class="week-header">
					<text v-for="(day, index) in weekDays" :key="index" class="week-day">{{ day }}</text>
				</view>

				<!-- 日期网格 -->
				<view class="date-grid">
					<view 
						v-for="(date, index) in dateList" 
						:key="index"
						class="date-item"
						:class="{ 
							active: selectedDate === date.day,
							disabled: date.disabled 
						}"
						@click="selectDate(date)"
					>
						<text v-if="date.day">{{ date.day }}</text>
					</view>
				</view>

				<!-- 可用时段 -->
				<view class="time-section">
					<view class="time-label">可用时段</view>
					<view class="time-grid">
						<view 
							v-for="(time, index) in timeSlots" 
							:key="index"
							class="time-item"
							:class="{ 
								active: selectedTime === time,
								disabled: time.disabled 
							}"
							@click="selectTime(time)"
						>
							{{ time.label }}
						</view>
					</view>
				</view>
			</view>
		</view>

		<!-- 预约须知 -->
		<view class="section">
			<view class="notice-card">
				<view class="notice-title">
					<text class="notice-icon">📋</text>
					<text>预约须知</text>
				</view>
				<view class="notice-list">
					<view class="notice-item" v-for="(item, index) in noticeList" :key="index">
						<text class="notice-dot">•</text>
						<text class="notice-text">{{ item }}</text>
					</view>
				</view>
			</view>
		</view>

		<!-- 确认预约按钮 -->
		<view class="submit-section">
			<view class="submit-btn" @click="confirmBooking">确认预约</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 当前年月
				currentYear: 2023,
				currentMonth: 10,
				// 星期标题
				weekDays: ['一', '二', '三', '四', '五', '六', '日'],
				// 日期列表
				dateList: [
					{ day: '' }, { day: '' }, { day: '' }, { day: '' }, { day: '' }, { day: '1' }, { day: '2' },
					{ day: '3' }, { day: '4' }, { day: '5', active: true }, { day: '6' }, { day: '7' }, { day: '8' }, { day: '9' },
					{ day: '10' }, { day: '11' }, { day: '12' }, { day: '13' }, { day: '14' }, { day: '15' }, { day: '16' },
					{ day: '17' }, { day: '18' }, { day: '19' }, { day: '20' }, { day: '21' }, { day: '22' }, { day: '23' },
					{ day: '24' }, { day: '25' }, { day: '26' }, { day: '27' }, { day: '28' }, { day: '29' }, { day: '30' },
					{ day: '31' }
				],
				// 选中的空间
				selectedSpace: 0,
				// 选中的日期
				selectedDate: '5',
				// 选中的时段
				selectedTime: '',
				// 空间列表
				spaceList: [
					{
						name: '健身中心',
						desc: '专业器械、全天候开放，每次限流10人。',
						price: '免费使用',
						capacity: '限10人',
						icon: '🏋️',
						image: '/static/booking/gym.jpg'
					},
					{
						name: '共享会议室',
						desc: '配备投影设备，适合商务会议及小型聚会。',
						price: '20点/小时',
						capacity: '限8人',
						icon: '🏢',
						image: '/static/booking/meeting.jpg'
					},
					{
						name: '网球场',
						desc: '标准场地网球设施，提供专业照明服务。',
						price: '10点/小时',
						capacity: '限4人',
						icon: '🎾',
						image: '/static/booking/tennis.jpg'
					}
				],
				// 时段列表
				timeSlots: [
					{ label: '08:00-09:00', disabled: false },
					{ label: '09:00-10:00', disabled: false },
					{ label: '10:00-11:00', disabled: false },
					{ label: '12:00-13:00', disabled: true },
					{ label: '13:00-14:00', disabled: false },
					{ label: '14:00-15:00', disabled: false },
					{ label: '15:00-16:00', disabled: false },
					{ label: '16:00-17:00', disabled: false },
					{ label: '17:00-18:00', disabled: false }
				],
				// 预约须知
				noticeList: [
					'请按照预约时间前10分钟到达现场进行签到。',
					'如需取消预约，请至少提前2个小时在系统内操作，否则可能扣除相应积分。',
					'请保持公共空间的整洁，使用完毕后请带走随身物品。',
					'如遇设备故障，请及时联系物业服务中心（电话：400-123-9999）。'
				]
			}
		},
		methods: {
			// 返回上一页
			goBack() {
				uni.navigateBack()
			},
			// 选择空间
			selectSpace(index) {
				this.selectedSpace = index
			},
			// 选择日期
			selectDate(date) {
				if (date.disabled || !date.day) return
				this.selectedDate = date.day
			},
			// 选择时段
			selectTime(time) {
				if (time.disabled) return
				this.selectedTime = time
			},
			// 上一月
			prevMonth() {
				if (this.currentMonth > 1) {
					this.currentMonth--
				} else {
					this.currentMonth = 12
					this.currentYear--
				}
			},
			// 下一月
			nextMonth() {
				if (this.currentMonth < 12) {
					this.currentMonth++
				} else {
					this.currentMonth = 1
					this.currentYear++
				}
			},
			// 确认预约
			confirmBooking() {
				if (!this.selectedTime) {
					uni.showToast({
						title: '请选择预约时段',
						icon: 'none'
					})
					return
				}
				uni.showModal({
					title: '确认预约',
					content: `预约${this.spaceList[this.selectedSpace].name}，${this.currentYear}年${this.currentMonth}月${this.selectedDate}日 ${this.selectedTime.label}`,
					success: (res) => {
						if (res.confirm) {
							uni.showToast({
								title: '预约成功',
								icon: 'success'
							})
						}
					}
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

	/* 分区 */
	.section {
		margin: 20rpx 30rpx 0;
	}

	.section-label {
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 20rpx;
	}

	/* 空间列表 */
	.space-list {
		display: flex;
		flex-direction: column;
		gap: 20rpx;
	}

	.space-card {
		background-color: #ffffff;
		border-radius: 20rpx;
		overflow: hidden;
		border: 2rpx solid transparent;
	}

	.space-card.active {
		border-color: #2c7a7b;
	}

	.space-image {
		width: 100%;
		height: 240rpx;
		position: relative;
	}

	.space-overlay {
		position: absolute;
		bottom: 80rpx;
		left: 24rpx;
		display: flex;
		align-items: center;
		gap: 12rpx;
	}

	.space-icon {
		font-size: 40rpx;
	}

	.space-name {
		font-size: 32rpx;
		font-weight: bold;
		color: #ffffff;
		text-shadow: 0 2rpx 4rpx rgba(0, 0, 0, 0.3);
	}

	.space-info {
		padding: 20rpx 24rpx;
	}

	.space-desc {
		font-size: 24rpx;
		color: #666666;
		margin-bottom: 12rpx;
	}

	.space-tags {
		display: flex;
		gap: 16rpx;
	}

	.space-tag {
		font-size: 22rpx;
		color: #2c7a7b;
		background-color: #e8f4f8;
		padding: 6rpx 16rpx;
		border-radius: 8rpx;
	}

	/* 日期时间卡片 */
	.datetime-card {
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 30rpx;
	}

	/* 月份切换 */
	.month-switcher {
		display: flex;
		align-items: center;
		justify-content: center;
		margin-bottom: 24rpx;
	}

	.month-arrow {
		font-size: 40rpx;
		color: #999999;
		padding: 0 30rpx;
	}

	.month-text {
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
	}

	/* 星期标题 */
	.week-header {
		display: grid;
		grid-template-columns: repeat(7, 1fr);
		text-align: center;
		margin-bottom: 16rpx;
	}

	.week-day {
		font-size: 24rpx;
		color: #999999;
	}

	/* 日期网格 */
	.date-grid {
		display: grid;
		grid-template-columns: repeat(7, 1fr);
		gap: 10rpx;
		margin-bottom: 30rpx;
	}

	.date-item {
		aspect-ratio: 1;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 50%;
		font-size: 26rpx;
		color: #333333;
	}

	.date-item.active {
		background-color: #2c7a7b;
		color: #ffffff;
	}

	.date-item.disabled {
		color: #cccccc;
	}

	/* 时段区域 */
	.time-section {
		border-top: 1rpx solid #f0f0f0;
		padding-top: 24rpx;
	}

	.time-label {
		font-size: 26rpx;
		color: #666666;
		margin-bottom: 16rpx;
	}

	.time-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 16rpx;
	}

	.time-item {
		padding: 16rpx 0;
		border-radius: 12rpx;
		font-size: 24rpx;
		color: #333333;
		background-color: #f5f7fa;
		text-align: center;
		border: 2rpx solid transparent;
	}

	.time-item.active {
		background-color: #2c7a7b;
		color: #ffffff;
	}

	.time-item.disabled {
		color: #cccccc;
		background-color: #f0f0f0;
	}

	/* 预约须知 */
	.notice-card {
		background-color: #ffffff;
		border-radius: 20rpx;
		padding: 30rpx;
	}

	.notice-title {
		display: flex;
		align-items: center;
		font-size: 30rpx;
		font-weight: bold;
		color: #333333;
		margin-bottom: 20rpx;
	}

	.notice-icon {
		margin-right: 12rpx;
		font-size: 32rpx;
	}

	.notice-list {
		display: flex;
		flex-direction: column;
		gap: 16rpx;
	}

	.notice-item {
		display: flex;
		align-items: flex-start;
	}

	.notice-dot {
		font-size: 28rpx;
		color: #2c7a7b;
		margin-right: 12rpx;
		line-height: 1.4;
	}

	.notice-text {
		flex: 1;
		font-size: 24rpx;
		color: #666666;
		line-height: 1.6;
	}

	/* 提交区域 */
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
