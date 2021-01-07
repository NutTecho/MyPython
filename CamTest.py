import cv2
import datetime
import numpy as np
#cap = cv2.VideoCapture('rtsp://192.168.137.51:8080/h264_pcm.sdp')
cap = cv2.VideoCapture(0)
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#
cap.set(3,1208)
cap.set(4,720)

# print(cap.get(3))
# print(cap.get(4))

def grayCon(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(gray,100,200)
    return canny

while (True):
    ref, frame = cap.read()
    roi = frame[:1208,0:720]
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1)
    kernel = np.ones((3,3),np.uint8)
    closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=4)
    result = closing.copy()
    contours,hierachy = cv2.findContours(result,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    num = 0
    for cnt in contours:
       area = cv2.contourArea(cnt)
       cv2.putText(roi, str(area), (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
       if area<5000 or area>35000:
            continue
       else:
        ellipse = cv2.fitEllipse(cnt)
        cv2.ellipse(roi,ellipse,(0,255,0),2)
        num+=1
        
    cv2.putText(roi,str(num),(10,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow("Show",roi)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    # R = frame[:, :, 2]
    # G = frame[:, :, 1]
    # B = frame[:, :, 0]
    #mark = (R<50)&(G>160)&(B<50)
    # date = str(datetime.datetime.now())
    # frame = cv2.putText(frame,date,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2,cv2.LINE_AA)

   # _,th1 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
    #th2 = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    # process = grayCon(frame)

    #cv2.imshow('R', R)
    #cv2.imshow('G', G)
    #cv2.imshow('B', B)

