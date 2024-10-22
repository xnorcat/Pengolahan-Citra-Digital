import cv2
import numpy as np

image = cv2.imread("C:\\Users\\mrhitj\\Pictures\\roombaaa.jpeg")
image = cv2.GaussianBlur(image, (3,3), 0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ddepth = cv2.CV_16S
delta = 0
scale = 1

scharrX = cv2.Scharr(gray, ddepth, 1, 0, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
scharrY = cv2.Scharr(gray, ddepth, 0, 1, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

absoluteScharrX = cv2.convertScaleAbs(scharrX)
absoluteScharrY = cv2.convertScaleAbs(scharrY)
# absoluteScharrX = np.float32(absoluteScharrX)
# absoluteScharrY = np.float32(absoluteScharrY)


# scharr = np.sqrt(pow(absoluteScharrX, 2) + pow(absoluteScharrY, 2))
scharr = cv2.addWeighted(absoluteScharrX, 0.5, absoluteScharrY, 0.5, 0)
# _, scharr = cv2.threshold(scharr, 128, 255, cv2.THRESH_BINARY)
cv2.imshow("Scharr", scharr)
cv2.waitKey(0)
cv2.destroyAllWindows()
