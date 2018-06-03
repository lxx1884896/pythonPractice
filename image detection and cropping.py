#coding=utf-8
import cv2

import numpy as np

image = cv2.imread("C:\Users\lxx\Desktop\upan.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)


# blur and threshold the image
blurred = cv2.blur(gradient, (9, 9))
(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)


# perform a series of erosions and dilations
closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)



(_,cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))
print  box
# draw a bounding box arounded the detected barcode and display the image
# cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
# cv2.imshow("Image", image)
# cv2.imwrite("contoursImage2.jpg", image)




Xs = [i[0] for i in box]
Ys = [i[1] for i in box]
x1 = min(Xs)
x2 = max(Xs)
y1 = min(Ys)
y2 = max(Ys)
listBox=[[x1,y1],[x2,y1],[x2,y2],[x1,y2]]
box1=np.matrix(listBox)
print box1
font=cv2.FONT_HERSHEY_SIMPLEX#使用默认字体
#font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8)  # Creates a font
#font = ImageFont.truetype("simhei.ttf", 50, encoding="utf-8")
x=500
y=500

cv2.putText(image, "Hello World !", (x, y), font, 4,(255, 255, 255),15)  # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细


cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
cv2.imshow("Image", image)
cv2.imwrite("contoursImage2.jpg", image)




image1= image.copy()
cv2.drawContours(image1, [box1], -1, (0,0, 255), 3)
hight = y2 - y1
width = x2 - x1
cropImg = image[y1:y1+hight, x1:x1+width]

cv2.imshow("cropImg", cropImg)

cv2.imshow("Image1", image1)

cv2.waitKey(0)












