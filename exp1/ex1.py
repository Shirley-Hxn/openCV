"""
使用 OpenCV 打开一个彩色图像文件，对其进行灰度转换、二值等操作，
使用 imshow 函数显示原图像和变换后的图像，并将变换后的图像保存为新文件。
"""
import cv2


# 打开一个彩色图像文件
img = cv2.imread("apple.jpg", cv2.IMREAD_COLOR)

# 在屏幕上长时间显示图片
cv2.imshow("apple.pgn", img)




