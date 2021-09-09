# -*- coding: utf-8 -*-
"""
使用 OpenCV 打开一个彩色图像文件，对其进行灰度转换、二值等操作，
使用 imshow 函数显示原图像和变换后的图像，并将变换后的图像保存为新文件。
"""

import cv2

# 打开一个彩色图像文件
img = cv2.imread("apple.jpg", cv2.IMREAD_COLOR)

# 进行灰度转换
img1 = cv2.imread("apple.jpg", 0)  # 0 代表灰色，也可通过 cvtColor 进行转换

# 进行二值化操作


# 在屏幕上长时间显示图片
cv2.imshow("apple", img)
cv2.imshow("appleGray", img1)
cv2.waitKey(0)

# 将变换后的图像保存为新文件
cv2.imwrite("appleGray.jpg", img1)
