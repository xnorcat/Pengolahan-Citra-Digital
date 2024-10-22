import cv2
import numpy as np

threshold = 0.2
kernel5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,20))
x_co = 0
y_co = 0
hsv = None
Hue = 0
Saturation = 0
Value = 0
threshold_Hue = 180*threshold
threshold_Saturation = 255*threshold
threshold_Value = 255*threshold

def on_mouse(event,x,y,flag,param):
  global x_co,y_co,Hue,Saturation,Value,hsv
  if(event==cv2.EVENT_LBUTTONDOWN):
    x_co=x
    y_co=y
    p_sel = hsv[y_co][x_co]
    Hue = p_sel[0]
    Saturation = p_sel[1]
    Value = p_sel[2]


cv2.namedWindow("camera", 1)
cv2.namedWindow("camera2", 2)
cv2.namedWindow("camera3", 3)
#cam = video.create_capture(0)
image = cv2.imread("C:\\Users\\mrhitj\\Documents\\floppa.webp")
# image.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# image.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # ret, src = image.read()
    source = cv2.blur(image, (3,3))
    hsv = cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
    cv2.setMouseCallback("camera2",on_mouse, 0);

    minColor = np.array([Hue-threshold_Hue,Saturation-threshold_Saturation,Value-threshold_Value])
    maxColor = np.array([Hue+threshold_Hue,Saturation+threshold_Saturation,Value+threshold_Value])
    mask = cv2.inRange(hsv, minColor, maxColor)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel5)

    #res = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.putText(mask,"H:" + str(Hue)+" S:"+str(Saturation)+" V:"+str(Value), (10,30), cv2.FONT_HERSHEY_PLAIN, 2.0, (255,255,255), thickness = 1)
    cv2.imshow("camera", mask)
    cv2.imshow("camera2", source)
    source_segmented = cv2.add(source,source,mask=mask)
    cv2.imshow("camera3", source_segmented)
    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()
