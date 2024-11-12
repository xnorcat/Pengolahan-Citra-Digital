#G64160017
import numpy as np
import cv2

# camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera = cv2.VideoCapture("C:\\Users\\mrhitj\\Desktop\\tutor\\a224y.gif")

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

#konvolusi manual
def konvolusi(image, kernel):
    row,col= image.shape
    mrow,mcol=kernel.shape
    h = int(mrow/2)

    canvas = np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if i==0 or i==row-1 or j==col-1:
                canvas.itemset((i,j),0)
                continue
            imgsum=0
            for k in range (-h, mrow-h):
                for l in range (-h, mcol-h):
                    res=image[i+k,j+l] * kernel[h+k,h+l]
                    imgsum+=res
                canvas.itemset((i,j), imgsum)
    return canvas

def kernel1(image):
    kernel = np.array([[-1/9, -1/9, -1/9],[-1/9, 8/9, -1/9],[-1/9, -1/9, -1/9]],np.float32)
    canvas = konvolusi(image, kernel)
    print("Hasil konvolusi kernel1 = ", canvas)
    return canvas

def kernel2(image):
    kernel = np.array([[0, 1/8, 0],[1/8, 1/2, 1/8],[0, 1/8, 0]],np.float32)
    canvas2 = konvolusi(image, kernel)
    print("Hasil konvolusi kernel2 = ", canvas2)
    return canvas2

while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1)
    image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    test1 = kernel1(image1)
    print("gambar1 ordo = ", image1.shape)
    print("gambar1 ori = ", image1)
    print("gambar1 HPF ordo = ", test1.shape)
    print("gambar1 HPF = ", test1)
    cv2.imshow("gambar1",image1)
    cv2.imshow("High pass",test1)

    test2=kernel2(image1)
    print("gambar2 ori ordo = ", image1.shape)
    print("gambar2 ori = ", image1)
    print("gambar1 LPF ordo = ", test2.shape)
    print("gambar2 LPF = ", test2)
    cv2.imshow("gambar2",image1)
    cv2.imshow("low pass",test2)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
