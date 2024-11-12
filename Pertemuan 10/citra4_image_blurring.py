import cv2
import numpy as np
from matplotlib import pyplot as plt

def showHistogramRGB(image, title):
    # Mengambil masing-masing warna merah, hijau dan biru dari citra
    red, green, blue = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    red = red.flatten()
    green = green.flatten()
    blue = blue.flatten()
    # Memasukkan data warna merah, hijau, dan biru ke plot
    plt.hist(red, bins=256, density=False, color='red', alpha=0.5)
    plt.hist(green, bins=256, density=False, color='green', alpha=0.4)
    plt.hist(blue, bins=256, density=False, color='blue', alpha=0.3)
    plt.title(title)
    plt.show()

def showHistogram(image, title):
    # Mengambil nilai mean dari warna biru
    image = image.mean(axis=2).flatten()
    plt.hist(image, bins=256, density=False, color='black')
    plt.title(title)
    plt.show()

img = cv2.imread("C:\\Users\\mrhitj\\Pictures\\roombaaa.jpeg")

blur1 = cv2.blur(img,(3,3)) # Average Filter
blur2 = cv2.GaussianBlur(img,(3,3),0)
median = cv2.medianBlur(img,3)
blur3 = cv2.bilateralFilter(img,9,75,75)

titles = ['Gambar Asli', 'Averaging',
          'Gaussian Blur', 'Bilateral Blur',
          'Median Blur']

images = [img, blur1, blur2, blur3, median]

for i in range(len(images)):
    showHistogram(images[i], titles[i])

for i in range(len(images)):
    showHistogramRGB(images[i], titles[i])

for i in range(5):
    cv2.imshow(titles[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
