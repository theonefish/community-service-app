<template>
	<view class="upload-images">
		<view class="image-list">
			<view
				v-for="(img, index) in imageList"
				:key="index"
				class="image-item"
			>
				<image :src="img" mode="aspectFill" class="preview-img"></image>
				<view class="delete-btn" @click="removeImage(index)" v-if="editable">
					<text class="delete-icon">×</text>
				</view>
			</view>
			<view
				v-if="editable && imageList.length < maxCount"
				class="upload-btn"
				@click="chooseImage"
			>
				<text class="plus-icon">+</text>
				<text class="upload-text">{{ imageList.length }}/{{ maxCount }}</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name: 'UploadImages',
		props: {
			imageList: { type: Array, default: () => [] },
			maxCount: { type: Number, default: 6 },
			editable: { type: Boolean, default: true }
		},
		emits: ['update:imageList', 'change'],
		methods: {
			chooseImage() {
				const remain = this.maxCount - this.imageList.length
				uni.chooseImage({
					count: remain,
					sizeType: ['compressed'],
					sourceType: ['album', 'camera'],
					success: (res) => {
						const newList = [...this.imageList, ...res.tempFilePaths]
						this.$emit('update:imageList', newList)
						this.$emit('change', newList)
					}
				})
			},
			removeImage(index) {
				const newList = this.imageList.filter((_, i) => i !== index)
				this.$emit('update:imageList', newList)
				this.$emit('change', newList)
			}
		}
	}
</script>

<style lang="scss">
	.upload-images {
		.image-list {
			display: flex;
			flex-wrap: wrap;
			gap: 8px;
		}

		.image-item, .upload-btn {
			width: calc((100% - 16px) / 3);
			aspect-ratio: 1;
			border-radius: 8px;
			overflow: hidden;
			position: relative;
		}

		.preview-img {
			width: 100%;
			height: 100%;
		}

		.delete-btn {
			position: absolute;
			top: 4px;
			right: 4px;
			width: 20px;
			height: 20px;
			border-radius: 50%;
			background: rgba(0, 0, 0, 0.5);
			display: flex;
			align-items: center;
			justify-content: center;

			.delete-icon {
				color: #fff;
				font-size: 16px;
				font-weight: bold;
			}
		}

		.upload-btn {
			border: 2px dashed #ddd;
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			background: #fafafa;

			.plus-icon {
				font-size: 28px;
				color: #ccc;
				line-height: 1;
			}

			.upload-text {
				font-size: 12px;
				color: #ccc;
				margin-top: 4px;
			}
		}
	}
</style>
