import cv2

cap = cv2.VideoCapture(0)
# tracker = cv2.legacy_TrackerMOSSE.create()
tracker = cv2.legacy_TrackerCSRT.create()
success,img = cap.read()
bbox = cv2.selectROI("tracking",img,False)
tracker.init(img,bbox)

def drawbox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),3,1)
    cv2.putText(img,"tracking",(75,75),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

# webcamFeed = True
# pathImage = ""
# cap.set(10,160)
# heightImage = 640
# widthImage = 800
# utils.initializeTrackbars()
while True:
    timer = cv2.getTickCount()
    success,img = cap.read()
    success,bbox = tracker.update(img)
    print(bbox)

    if success:
        drawbox(img,bbox)
    else:
        cv2.putText(img,'Lost',(75,75),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)


    fps = cv2.getTickFrequency()/(cv2.getTickCount() - timer)
    cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    # blank image

    
    # imgBlank = np.zeros((heightImage,widthImage,3)np.uint8)
    
    # if webcamFeed : success,img = cap.read()
    # else : img = cv2.imread(pathImage)

    # img = cv2.resize(img,(widthImage,heightImage))
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    # blur = cv2.GaussianBlur(gray,(5,5),1)
    # thes = utils.valTrackbars()
    # imgThres = cv2.Canny(blur,thres[0],thres[1])
    # kernal = np.ones((5,5))
    # dial = cv2.dilate(thres,kernel,iterations = 2)
    # imgThreshold = cv2.erode(dial,kernal,iterations = 1)
        


    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()