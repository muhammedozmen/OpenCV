import cv2
import numpy as np

canvas = np.zeros((500,500,3), np.uint8) + 255

#lines
cv2.line(canvas, (100,100), (300,300), (0,0,255), thickness=5)
cv2.line(canvas, (300,350), (400,500), (255,0,0), 8)

#rectangles
cv2.rectangle(canvas, (30,30), (60,60), (0,255,0), 4)
cv2.rectangle(canvas, (50,50), (80,80), (0,255,0), -1)

#circles
cv2.circle(canvas, (100,100), 100, (255,0,0), 4)

#triangles
u1=(300,500)
u2=(300,400)
u3=(500,300)

cv2.line(canvas, u1, u2, (0,0,0), 4)
cv2.line(canvas, u2, u3, (0,0,0), 4)
cv2.line(canvas, u1, u3, (0,0,0), 4)

cv2.imshow("window", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()