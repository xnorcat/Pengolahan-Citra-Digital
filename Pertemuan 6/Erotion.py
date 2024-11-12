import cv2
import numpy as np

gambar = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg", 0)
kernel = np.ones((5,5) , np.uint8)
hasilDilasi = cv2.dilate(gambar, kernel, iterations = 1)

cv2.imshow("Dilasi", hasilDilasi)
cv2.waitKey(0)
cv2.destroyAllWindows()
