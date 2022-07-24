import cv2
import numpy as np
import time
# from numba import cuda
import imutils
from imutils.video import FPS , WebcamVideoStream , FileVideoStream

# cuda.jit
def Concept1():
    vs = WebcamVideoStream(src=0).start()
    # cap = cv2.VideoCapture(0)
    new_frame_time = 0
    prev_frame_time = 0
    starttime = 0
    fr = 0
    fps = FPS().start()

    while True:
        # starttime = cv2.getTickCount()
        new_frame_time = time.time()
        # (grabbed , frame) = cap.read()
        frame = vs.read()
        frame = imutils.resize(frame,width = 800)

        if (new_frame_time-prev_frame_time > 0):
            fr = 1/(new_frame_time-prev_frame_time)

        prev_frame_time = new_frame_time
        # fr = (cv2.getTickCount() - starttime)/ cv2.getTickFrequency()
        cv2.putText(frame,"FPS: {:.2f}".format(fr),(10,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow('frame', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        fps.update()

   

    fps.stop()
    print("[INFO] elasped time : {:.2f}" .format(fps.elapsed()))
    print("[INFO] approx FPS : {:.2f}" .format(fps.fps()))

    cv2.destroyAllWindows()
    vs.stop()

if __name__ == "__main__":
     Concept1()
    # print(cv2.getBuildInformation())
