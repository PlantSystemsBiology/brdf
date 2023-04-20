import cv2
import numpy as np
def FillHole(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    len_contour = len(contours)
    contour_list = []

    for i  in range(len_contour):
        drawing = np.zeros_like(mask, np.uint8)  # create a black image
        img_contour = cv2.drawContours(drawing, contours, i, (255, 0, 0), -1)
        contour_list.append(img_contour)

    out = sum(contour_list)
    return out

def delete(img):
    mask = np.zeros_like(img)
    # 先利用二值化去除图片噪声
    ret, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    n = len(contours)  # 轮廓的个数
    cv_contours = []
    for contour in contours:
         area = cv2.contourArea(contour)
         if area <= 800:
             cv_contours.append(contour)
             # x, y, w, h = cv2.boundingRect(contour)
             # img[y:y + h, x:x + w] = 255
         else:
             continue
    cv2.fillPoly(img, cv_contours, (255, 255, 255))
    return img

area = 0
def ostu(img):
    global area
    #image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转灰度
    blur =  cv2.GaussianBlur(img,(5,5),0) # 阈值一定要设为 0 ！高斯模糊
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 二值化 0 = black ; 1 = white
    # cv2.imshow('image', th3)
    # a = cv2.waitKey(0)
    # print a
    height, width = th3.shape
    for i in range(height):
        for j in range(width):
            if th3[i, j] == 255:
                area += 1
    return area