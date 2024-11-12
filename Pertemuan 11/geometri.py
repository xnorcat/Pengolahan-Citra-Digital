import cv2
import numpy as np

images= [
         cv2.imread("C:\\Users\\mrhitj\\Pictures\\Screenshots\\Screenshot 2024-11-04 120639.png"),
         cv2.imread("C:\\Users\\mrhitj\\Pictures\\Screenshots\\Screenshot 2024-11-04 193721.png")]

def getCenterofLine(object1, object2, x = 0, y = 0):
    offset = (int(object1[0]/2) + int(object2[0]/2) + x,
              int(object1[1]/2) + int(object2[1]/2) + y)
    return offset

closeIterations = [7, 2]
openIterations = [1, 4]
kernelOpen = np.ones((5,5), np.uint8)
kernelClose = np.ones((5,5), np.uint8)
centers = []

for i in range(len(images)):
    images[i] = cv2.resize(images[i], (640, 480))
    gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Melakukan operasi closing dan opening pada citra
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernelClose, iterations = closeIterations[i])
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernelOpen, iterations = openIterations[i])

    # Segmentasi citra
    segment = cv2.Canny(opening, 200, 200)
    contours, hierarchy = cv2.findContours(segment, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    segment = cv2.cvtColor(segment, cv2.COLOR_GRAY2RGB)
    # cv2.drawContours(images[i], contours, -1, (0, 0, 255), 1)

    #Segmentasi, clustering, pemberian label, dan menghitung parameter pada citra

    for j in range(len(contours)):
        # Segmentasi, clustering dan pemberian label
        moments = cv2.moments(contours[j])
        centers.append((int(moments['m10']/moments['m00']), int(moments['m01'] / moments['m00']))) # Mencari centroid
        cv2.circle(images[i], centers[-1], 1, (0, 0, 255), -1) # Menggambar bulat pada centroid
        cv2.putText(images[i], str(j+1), centers[-1], cv2.FONT_HERSHEY_DUPLEX, 0.75, (255, 0, 0), 1) # Memberi nomor pada centroid

pixelDistance = cv2.norm(centers[0], centers[1], cv2.NORM_L2)
kmDistance = pixelDistance / 40.1836969001148 # 40 px / 1km
cv2.line(images[0], centers[0], centers[1], (0, 255, 255), 2)
cv2.putText(images[0], f'd = {pixelDistance} px', getCenterofLine(centers[0], centers[1]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 255), 1)
cv2.putText(images[0], f'd = {kmDistance} km', getCenterofLine(centers[0], centers[1], y=-20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 255), 1)

pixelDistance = cv2.norm(centers[2], centers[4], cv2.NORM_L2)
kmDistance = pixelDistance / 0.24705882352941178 # 0.24 px / 1m
cv2.line(images[1], centers[2], centers[4], (0, 255, 255), 2)
cv2.putText(images[1], f'd = {pixelDistance} px', getCenterofLine(centers[2], centers[4]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 255), 1)
cv2.putText(images[1], f'd = {kmDistance} m', getCenterofLine(centers[2], centers[4], y=-20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 255), 1)

for i in range(len(images)):
    cv2.imshow(f'Gambar {i+1}', images[i])
cv2.waitKey(0)
cv2.destroyAllWindows()
