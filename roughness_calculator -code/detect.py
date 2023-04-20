import cv2
import numpy as np
from model import FillHole,delete,ostu
from matplotlib import pyplot as plt
import os
imaPath = r"I:\cotton 1-6"#待处理文件路径
output = r"rice1"#结果保存路径
imaList = os.listdir(imaPath)
for files in imaList:
    area = 0
    path_ima = os.path.join(imaPath, files)
    path_processed = os.path.join(output, files)
    img = cv2.imread(path_ima)
    GrayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh1=cv2.threshold(GrayImage,180,255,cv2.THRESH_BINARY)
    #cv2.imwrite(path_processed, thresh1)
    thresh1 = delete(255-thresh1)#0
    thresh1 = FillHole(thresh1)
    thresh1 = delete(thresh1)
    #print('black:', len(thresh1[thresh1==255]))
    #print('white:', len(thresh1[thresh1==0]))
    #print('total:', len(thresh1[thresh1==255]) + len(thresh1[thresh1==0]))
    #print('imges:', thresh1.shape[0]*thresh1.shape[1])
    #cv2.imwrite(path_processed, thresh1)
    thresh1 = 255-thresh1
    A=thresh1
    B=thresh1
    kernel = np.ones((20,20))
    erodeImg = cv2.erode(B, kernel)
    img1 = cv2.GaussianBlur(erodeImg, (3, 3), 0)
    ret, thresh1 = cv2.threshold(img1, 0, 255, cv2.THRESH_OTSU)
    ret, thresh2 = cv2.threshold(A, 0, 255, cv2.THRESH_OTSU)
    print('未处理black:', len(thresh2[thresh2 == 0]))
    print('处理black:',len(thresh1[thresh1 == 0]))
    #print('black:', len(thresh1[thresh1 == 255]))
    #print(len(thresh1[thresh2 == 0]))
    #cv2.imwrite(path_processed, thresh1)
    #print('total:', len(thresh1[thresh1==255]) + len(thresh1[thresh1==0]))
    #print('imges:', thresh1.shape[0]*thresh1.shape[1])
    canny1 = cv2.Canny(thresh1, 50, 150)
    canny2 = cv2.Canny(thresh2,50,150)
    print('处理line:',len(canny1[canny1 == 255]))
    print('未处理line:', len(canny2[canny2 == 255]))
    print('%4f'%(len(canny1[canny1 == 255])/len(canny2[canny2==255])))
    #image = canny
    #canny = np.asanyarray(canny)
    #img[canny == 255] = [0,0,0]
    #print(path_processed)
