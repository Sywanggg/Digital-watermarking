from PIL import Image
from PIL import ImageChops

def Watermark_detection(image,water):
    img = Image.open(image).convert("RGB")
    width, height = img.size  # 读取文件大小

    img_water = Image.open(water).convert("RGB")
    img_water = img_water.resize((width, height))  # 将水印缩放至文件大小

    img_pixels = list(img.getdata())
    print(img_pixels[:10])
    # 得到的实际水印
    img_get = img.point(lambda i: (int(i & 3)) * 85)
    img_get.show()
    # 理论上应得到的水印
    img_water = img_water.point(lambda i: round(i / 85) * 85)
    print(watermark_verificate(img_get, img_water))

def watermark_verificate(im1,im2):
    return ImageChops.difference(im1,im2).getbbox() is None

image = input("请输入图像地址:")
watermark = input("请输入水印地址:")
Watermark_detection(image,watermark)