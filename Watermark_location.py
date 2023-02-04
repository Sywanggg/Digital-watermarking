import numpy as np
from PIL import Image


Image_path1 = input("输入原始图像地址:")
Image_path2 = input("输入嵌入图像地址:")
image1=Image.open(Image_path1)
image2=Image.open(Image_path2)
Data1=np.asarray(image1)
Data2=np.asarray(image2)
sign=0
num=0
ArrayofBin=[]
for i in range(0,512):
    for j in range(0,512):
        if (Data2[i][j][0]==Data1[i][j][0]-1 and  (Data1[i][j][0]) % 2 == 1) or (Data2[i][j][1]==Data1[i][j][1]-1 and (Data1[i][j][1])%2==1) or (Data2[i][j][2]==Data1[i][j][2]-1 and (Data1[i][j][2])%2==1):
            if sign==0:
                ArrayofBin.append(0)
                sign=1
        elif (Data2[i][j][0]==Data1[i][j][0]+1 and (Data1[i][j][0])%2 ==0) or (Data2[i][j][1]==Data1[i][j][1]+1 and(Data1[i][j][1])%2==0) or (Data2[i][j][2]==Data1[i][j][2]+1 and (Data1[i][j][2])%2==0):
            if sign==0:
                ArrayofBin.append(1)
                sign=1
        else:
            pass
    num+=1
    sign=0
ArrayofBin.reverse()
num1 = 0
for i in ArrayofBin:
    if i ==1:
        num1 = num1*2+1
    elif i==0:
        num1 = num1*2+0
print("定位水印成功,原有信息数值为:",int(num1))