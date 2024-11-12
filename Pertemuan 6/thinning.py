import cv2

gambar = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg", 0)
thinning = cv2.ximgproc.thinning(gambar)

cv2.imshow("Thinning", thinning)
cv2.waitKey(0)
cv2.destroyAllWindows()
