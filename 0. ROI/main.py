import cv2
import numpy as np

img = cv2.imread("volvo.jpg")

color = img[200,300]
print(color)
# print(img.shape)
blue = img[200,300,0]
green = img[200,300,1]
red = img[200,300,2]
print(blue, green, red)

img[200,300, 0] = 0
print(img[200,300])

blue = img.item(200,300,0)
print(blue)
img.itemset((150,150,0),200)


cv2.imshow("car", img)

cv2.waitKey(0)
cv2.destroyAllWindows()