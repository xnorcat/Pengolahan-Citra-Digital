#memilih warna biru saja pada gambar gambar
import cv2 # menyertakan library cv2 dari opencv
import numpy as np


img0 = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg")
img = cv2.cvtColor(img0, cv2.COLOR_BGR2HSV)
# print("img = ", img)
print(img0.shape)
print("img0 = ", img0)

# lowBlue = np.array([30, 10, 10])
# highBlue = np.array([40, 255, 255])
# mask = cv2.inRange (img, lowBlue, highBlue)

#cv2.imshow("img0", img0)
#cv2.imshow("img", img)
#print(img.shape)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
