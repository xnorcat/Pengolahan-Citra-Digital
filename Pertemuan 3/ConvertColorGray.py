# Konversi warna ke abu abu
import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img0 = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg")
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)
print("gray = ", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
