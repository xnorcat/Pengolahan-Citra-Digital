# Konversi warna ke abu abu
import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img = cv2.imread("C:\\Users\mrhitj\\Pictures\\kmps\\EP.9.v0.1724856904.720p.mp4_snapshot_15.02_[2024.08.31_21.32.41].jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, BW) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Gray", gray)
cv2.imshow("BW", BW)
print("Original = ", img.shape)
print("Gray = ", gray.shape)
print("BW = ", BW.shape)
print(img)

# simpan hasil
cv2.imwrite("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos bw.jpg", BW)

cv2.waitKey(0)
cv2.destroyAllWindows()
