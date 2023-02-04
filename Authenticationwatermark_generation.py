import numpy as np
from PIL import Image

def authenticationwatermark_Generate(photo,water):
    # 预处理
    img = Image.open(photo).convert("RGB")
    width, height = img.size  # 读取文件大小

    img_water = Image.open(water).convert("RGB")
    img_water = img_water.resize((width, height))

    img = img.point(lambda i: (int(i >> 2)) << 2)
    img_water = img_water.point(lambda i: round(i / 85))

    img_pixels = list(img.getdata())
    water_pixels = list(img_water.getdata())

    newpixels = [0 for i in range(len(img_pixels))]

    for index in range(len(img_pixels)):
        list_temp = [];
        for i in range(3):
            list_temp.append(img_pixels[index][i] + water_pixels[index][i])
        newpixels[index] = tuple(list_temp)

    imn = Image.new("RGB", (width, height))
    imn.putdata(data=newpixels)
    imn.show()
    imn.save("./")

image = input("请输入图像地址:")
watermark = input("请输入水印地址:")
authenticationwatermark_Generate(image,watermark)