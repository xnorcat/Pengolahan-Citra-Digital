import cv2
import numpy as np

images= [cv2.imread("C:\\Users\\mrhitj\\Pictures\\NGC_4298_and_NGC_4302_-_Heic1709a.jpg"),
         cv2.imread("C:\\Users\\mrhitj\\Pictures\\stephenson1.jpeg")]

iterations = [5, 1]
kernelOpen = np.ones((5,5), np.uint8)
kernelClose = np.ones((5,5), np.uint8)

for i in range(len(images)):
    images[i] = cv2.resize(images[i], (600, 600))
    gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Melakukan operasi closing dan opening pada citra
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernelClose, iterations = iterations[i])
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernelOpen)

    # Segmentasi citra
    segment = cv2.Canny(opening, 30, 200)
    contours, hierarchy = cv2.findContours(segment, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    segment = cv2.cvtColor(segment, cv2.COLOR_GRAY2RGB)
    cv2.drawContours(images[i], contours, -1, (0, 0, 255), 1)

    #Segmentasi, clustering, pemberian label, dan menghitung parameter pada citra
    centers = []
    for j in range(len(contours)):
        # Segmentasi, clustering dan pemberian label
        moments = cv2.moments(contours[j])
        centers.append((int(moments['m10']/moments['m00']), int(moments['m01'] / moments['m00']))) # Mencari centroid
        cv2.circle(images[i], centers[-1], 1, (0, 0, 255), -1) # Menggambar bulat pada centroid
        cv2.putText(images[i], str(j+1), centers[-1], cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 255, 255), 1) # Memberi nomor pada centroid

        # Menghitung parameter
        (x, y), (minorAxis, majorAxis), angle = cv2.fitEllipse(contours[j]) # Mengambil minor dan major axis
        eccentricity = np.sqrt(1 - (minorAxis**2 / majorAxis**2))
        area = cv2.contourArea(contours[j])
        perimeter = cv2.arcLength(contours[j], True)
        metric = (4 * np.pi * area) / perimeter**2

        print("----------------------")
        print(f'Eccentricity of object {j+1} in image {i+1} : {eccentricity}')
        print(f'Area of object {j+1} in image {i+1}         : {area}')
        print(f'Perimeter of object {j+1} in image {i+1}    : {perimeter}')
        print(f'Metric of object {j+1} in image {i+1}       : {metric}')

        # Pemberian label bentuk pada citra
        offset = (centers[-1][0] + 0, centers[-1][1] + 20) # Offset dari centroid untuk penempatan teks
        form = "Round" if round(metric, 1) >= 0.7 else "Ellipse"
        cv2.putText(images[i], str(form), offset, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)


for i in range(len(images)):
    cv2.imshow(f'Gambar {i+1}', images[i])
cv2.waitKey(0)
cv2.destroyAllWindows()
