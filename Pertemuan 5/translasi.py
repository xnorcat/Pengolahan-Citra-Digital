import cv2
import numpy as np
img = cv2.imread("C:\\Users\\mrhitj\\Documents\\Python Code\\Pengolahan Citra Digital\\kucing2.jpg")

print(img.shape)

row, column, color = img.shape

MTranslasi = np.float32([
    [2, 0 , 100],
    [0, 2, 50]
])

print(MTranslasi, '\n')

dst = cv2.warpAffine(img, MTranslasi, (column, row))

cv2.imshow("title", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
