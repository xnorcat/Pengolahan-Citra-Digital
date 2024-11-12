import cv2
import numpy as np
image = cv2.imread("C:\\Users\\mrhitj\\Pictures\\NGC_4298_and_NGC_4302_-_Heic1709a.jpg")

canny = cv2.Canny(image, 150, 100, 3, L2gradient=True)

cv2.imshow("Original", image)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
