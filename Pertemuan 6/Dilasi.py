import cv2
import numpy as np

gambar = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg", 0)
kernel = np.ones((5,5) , np.uint8)
hasilOpening = cv2.morphologyEx(gambar, cv2.MORPH_OPEN, kernel)

cv2.imshow("Opening", hasilOpening)
cv2.waitKey(0)
cv2.destroyAllWindows()
