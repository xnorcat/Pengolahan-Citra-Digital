import cv2

img = cv2.imread("C:\\Users\\mrhitj\\Documents\\Python Code\\Pengolahan Citra Digital\\kucing2.jpg")

dstSkala = cv2.resize(img, None, fx=2.5, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("original",img)
cv2.imshow("hasil",dstSkala)

cv2.waitKey(0)
cv2.destroyAllWindows()
