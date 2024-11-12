# Konversi warna ke abu abu
import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg")
row, col = img.shape[0:2]
cv2.imshow("Original", img)
print(img.shape)
for i in range(row):
    for j in range(col):
        #Find the average of the BGR picel values
        img[i, j] = sum(img[i, j]) * 0.33
        #sum[i, j] = sum(img[i, j]) * 0.33

cv2.imshow("Hasil ", img)
print("img = ", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
