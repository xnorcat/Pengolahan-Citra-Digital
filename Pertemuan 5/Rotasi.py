import cv2

img = cv2.imread("C:\\Users\\mrhitj\\Documents\\Python Code\\Pengolahan Citra Digital\\kucing2.jpg")

row, column, color = img.shape

MRotasi = cv2.getRotationMatrix2D((column/2, row/2), 90, 1)

print(MRotasi)

dstRotasi = cv2.warpAffine(img, MRotasi, (column, row))

cv2.imshow("title", dstRotasi)

cv2.waitKey(0)
cv2.destroyAllWindows()
