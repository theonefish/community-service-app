<template>
	<view class="filter-tabs" v-if="tabs.length > 0">
		<scroll-view scroll-x class="tabs-scroll" show-scrollbar="false">
			<view class="tabs-inner">
				<view
					v-for="(tab, index) in tabs"
					:key="index"
					class="tab-item"
					:class="{ active: current === index }"
					@click="$emit('change', index)"
				>
					<text class="tab-text">{{ tab }}</text>
					<view class="tab-line" v-if="current === index"></view>
				</view>
			</view>
		</scroll-view>
	</view>
</template>

<script>
	export default {
		name: 'FilterTabs',
		props: {
			tabs: { type: Array, default: () => [] },
			current: { type: Number, default: 0 }
		},
		emits: ['change']
	}
</script>

<style lang="scss">
	.filter-tabs {
		background: #fff;
		border-bottom: 1px solid #eee;

		.tabs-scroll {
			white-space: nowrap;

			.tabs-inner {
				display: inline-flex;
				padding: 0 16px;
			}

			.tab-item {
				padding: 12px 16px;
				position: relative;
				font-size: 14px;
				color: #666;
				transition: color 0.2s;

				&.active {
					color: #2c7a7b;
					font-weight: 600;

					.tab-line {
						position: absolute;
						bottom: 0;
						left: 50%;
						transform: translateX(-50%);
						width: 20px;
						height: 3px;
						background: #2c7a7b;
						border-radius: 2px;
					}
				}
			}
		}
	}
</style>
