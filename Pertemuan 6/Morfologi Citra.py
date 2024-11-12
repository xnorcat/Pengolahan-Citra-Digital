import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg", 0)
img0 = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg", 0)
imgC = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg", 0)

img = cv2.resize(img, (250, 250));
img0 = cv2.resize(img0, (250, 250));
imgC = cv2.resize(imgC, (250, 250));

kernel = np.ones((5,5) , np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)
opening = cv2.morphologyEx(img0, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(imgC, cv2.MORPH_CLOSE, kernel)


titles = ["Normal Image", "Erosion", "Dilation", "Before Opening", "Opening", "Before Closing", "Closing"]

images = [img, erosion, dilation, img0, opening, imgC, closing]

# for i in range(7):
#     plt.subplot(2,5,i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# # plt.show()

for i in range(7):
    cv2.imshow(titles[i], images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
