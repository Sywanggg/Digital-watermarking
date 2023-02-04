import numpy as np
from PIL import Image

# 图像读取
Image_path = input("输入图像地址:")
picture = Image.open(Image_path)
print("图像导入成功！")

# 隐藏信息
message = int(input("输入嵌入信息："))
ArrayofBin = []
Len = 0
while True:
    ArrayofBin.append(message%2)
    message = message//2
    Len = Len+1
    if message == 0:
        break
Data=np.asarray(picture)
flag=0
num=0

# 信息嵌入
for i in range(0,512):
    if flag == 1:
        break
    for j in range(0,512):
        if ArrayofBin[num] == 0 and (Data[i][j][0]) % 2 == 1:
            Data[i][j][0] = Data[i][j][0]-1
        elif ArrayofBin[num] == 1 and (Data[i][j][0]) % 2 == 0:
            Data[i][j][0] = Data[i][j][0] +1
        if ArrayofBin[num] == 0 and (Data[i][j][1]) % 2 == 1:
            Data[i][j][1] = Data[i][j][1] - 1
        elif ArrayofBin[num] == 1 and (Data[i][j][1]) % 2 == 0:
            Data[i][j][1] = Data[i][j][1] + 1
        if ArrayofBin[num] == 0 and (Data[i][j][2]) % 2 == 1:
            Data[i][j][2] = Data[i][j][2] - 1
        elif ArrayofBin[num] == 1 and (Data[i][j][2]) % 2 == 0:
            Data[i][j][2] = Data[i][j][2] + 1
    num = num + 1
    if num == Len:
        sign = 1
        break
nm1 = Image.fromarray(Data)
nm1.show()
Image0_path=input("输入保存地址:")
nm1.save(Image0_path)
print("信息嵌入成功！")