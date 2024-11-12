import cv2 #Menyertakan library cv2 dari opencv
import numpy as np #Menyertakan library numpy

#Membuat objek VideoCapture untuk mengambil video dari kamera pengguna dan menggunakan API DirectShow
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# camera = cv2.VideoCapture("C:\\Users\\mrhitj\\Pictures\\baa\\alice-aris.gif")

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

while True:
    ret, frame = camera.read() # Mengambil frame dari kamera
    frame = cv2.flip(frame, 1) # Membalikkan frame dari kamera secara vertikal

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Mengubah frame menjadi berwarna abu abu
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Mengubah frame menjadi berwarna HSV
    (thresh, BW) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) # Mengubah frame menjadi hitam putih

    cv2.imshow("Camera", frame) # Tampilkan frame atau video dari kamera
    cv2.imshow("Gray", gray) # Tampilkan frame kamera yang diubah menjadi abu abu
    cv2.imshow("HSV", hsv) # Menampilkan frame kamera yang diubah menjadi HSV
    cv2.imshow("BW", BW) # Menampilkan frame kamera yang diubah menjadi hitam putih

    print("gray = ", gray)
    print("BW = ", BW)

    if cv2.waitKey(1) == ord('q'):
        break # Hentikan rekaman kamera jika pengguna menekan huruf "q" pada keyboard

camera.release() # Menutup kamera
cv2.destroyAllWindows() # Menutup semua jendela
