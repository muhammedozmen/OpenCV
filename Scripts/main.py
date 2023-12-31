import cv2
import numpy as np

canvas = np.zeros((600,600,3), np.uint8) + 255

f1=cv2.FONT_ITALIC

cv2.putText(canvas, "hello", (30,200), f1, 4, (255,0,0), cv2.LINE_AA)



cv2.imshow("window", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
