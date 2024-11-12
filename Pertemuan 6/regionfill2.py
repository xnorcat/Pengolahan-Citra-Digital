import cv2

gambar = cv2.imread("C:\\Users\\mrhitj\\Pictures\\square.png",)

garis = cv2.findContours(gambar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
garis = garis[0] if len(garis) == 2 else garis[1]

for g in garis:
    cv2.drawContours(gambar,[g], 0, (255,255,255), -1)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20,20))
regionFill = cv2.morphologyEx(gambar, cv2.MORPH_OPEN, kernel, iterations=2)

cv2.imshow('gray', gambar)
cv2.imshow('region fill', regionFill)
cv2.waitKey(0)
