import cv2
import numpy as np

gambar = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg", 0)

_, gambarBiner = cv2.threshold(gambar, 128, 255, cv2.THRESH_BINARY)

gambar_cp = gambar.copy()
kernel = np.ones((3, 3), np.uint8)
thick = cv2.dilate(gambar, kernel, iterations=1)
bound = cv2.subtract(thick, gambar)

cv2.imshow("bound", bound)

cv2.waitKey(0)
cv2.destroyAllWindows()
