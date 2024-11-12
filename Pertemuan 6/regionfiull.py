import cv2
import numpy as np

gambar = cv2.imread("C:\\Users\\mrhitj\\Pictures\\square.png", 0)


temp, gambarTh = cv2.threshold(gambar, 220, 255, cv2.THRESH_BINARY_INV)

gambarFill = gambar.copy()

row, col = gambarTh.shape[:2]
mask = np.zeros((row+2, col+2), np.uint8)

cv2.floodFill(gambarFill, mask, (0,0), 255)
gambarFillInverse = cv2.bitwise_not(gambarFill)

gambarHasil = gambarTh | gambarFillInverse


cv2.imshow("Fizll", gambarTh)
cv2.imshow("Fill", gambarHasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
