from gradio_client import Client
import gradio_client
from PIL import Image

client = Client("https://mrbeliever-background-remover.hf.space/--replicas/fjq6m/")
result = client.predict(
		gradio_client.file("test.jpg"),
		api_name="/predict"
)
print(result)

# 加载 result 中的图片
result_image_path = result
bg_image_path = 'bg.png'
output_image_path = 'output.png'

# 打开 result 图片并确保它是 RGBA 模式
result_image = Image.open(result_image_path).convert('RGBA')

# 加载背景图片并确保它是 RGBA 模式
bg_image = Image.open(bg_image_path).convert('RGBA')

# 确定裁剪和缩放操作
if bg_image.size[0] > result_image.size[0] or bg_image.size[1] > result_image.size[1]:
    # 如果背景图片的宽度或高度大于 result 图片，则进行裁剪
    crop_width = min(bg_image.size[0], result_image.size[0])
    crop_height = min(bg_image.size[1], result_image.size[1])
    left = (bg_image.size[0] - crop_width) // 2
    top = (bg_image.size[1] - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    bg_image_resized = bg_image.crop((left, top, right, bottom))
    # 如果裁剪后的图片仍然比 result 图片大，进行缩放
    if bg_image_resized.size != result_image.size:
        bg_image_resized = bg_image_resized.resize(result_image.size, Image.Resampling.LANCZOS)
else:
    bg_image_resized = bg_image_resized.resize(result_image.size, Image.Resampling.LANCZOS)

# 将 result 图片叠在裁剪和缩放后的背景图片上面
composite_image = Image.alpha_composite(bg_image_resized, result_image)

# 保存合成后的图片到本地目录
composite_image.save(output_image_path)

# 如果需要，显示合成后的图片
composite_image.show()