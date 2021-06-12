import cv2
import pytesseract
import struct
import numpy as np
from pyzbar.pyzbar import decode
# faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def barcodecap():
    cap = cv2.VideoCapture(1)
    while True:
        ret, frame = cap.read()
        for barcode in decode(frame):
            # print(barcode)
            mydata = barcode.data.decode('utf-8')
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(frame,[pts],True,(255,0,255),5)
            pts2 = barcode.rect
            cv2.putText(frame,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# 0 = Orientation and script detection (OSD) only.
# 1 = Automatic page segmentation with OSD.
# 2 = Automatic page segmentation, but no OSD, or OCR
# 3 = Fully automatic page segmentation, but no OSD. (Default)
# 4 = Assume a single column of text of variable sizes.
# 5 = Assume a single uniform block of vertically aligned text.
# 6 = Assume a single uniform block of text.
# 7 = Treat the image as a single text line.
# 8 = Treat the image as a single word.
# 9 = Treat the image as a single word in a circle.
# 10 = Treat the image as a single character.
def vdo_ocr():
    cap = cv2.VideoCapture(0)
    pytesseract.pytesseract.tesseract_cmd = 'D:/tesseract-ocr/tesseract.exe'
    while (True):
        ret, frame = cap.read()
        himg,wimg,_ =  frame.shape
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        adth = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
        config = "--psm 4"
        boxes = pytesseract.image_to_boxes(adth)
        textdata = pytesseract.image_to_string(adth,config=config)
        print(textdata)

        for b in boxes.splitlines():
            # print(b)
            b = b.split(' ')
            # print(b)
            t,x,y,w,h = b[0],int(b[1]),int(b[2]),int(b[3]),int(b[4])
            cv2.rectangle(adth,(x,himg-y),(w,himg-h),(0,0,255),2)
            cv2.putText(adth,t,(x,himg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

        cv2.imshow('frame', adth)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()




def testocr():
    pytesseract.pytesseract.tesseract_cmd = 'D:/tesseract-ocr/tesseract.exe'
    img = cv2.imread("bigsleep.jpg")
    # img = cv2.resize(img,None,fx=0.5,fy=0.5)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    adth = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
    himg,wimg,_ =  img.shape
    config = "--psm 4"
    # boxes = pytesseract.image_to_boxes(gray)
    textdata = pytesseract.image_to_string(adth,config=config)
    print(textdata)
    # for b in boxes.splitlines():
    #     # print(b)
    #     b = b.split(' ')
    #     print(b)
    #     t,x,y,w,h = b[0],int(b[1]),int(b[2]),int(b[3]),int(b[4])
    #     cv2.rectangle(gray,(x,himg-y),(w,himg-h),(0,0,255),2)
    #     cv2.putText(gray,t,(x,himg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

    # print(pytesseract.image_to_string(gray))
    cv2.imshow('result',adth)
    cv2.waitKey(0)



def draw_bound(img, classifier, scaleFactor, minNeighbors, color, text):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
    coords = []
    for (x, y, w, h) in feature:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1)
        coords = [x, y, w, h]
    return img, coords


def detect(img, faceCascade, eyeCascade):
    img, coords = draw_bound(img, faceCascade, 1.1, 10, (255, 0, 0), "Face")
    img, coords = draw_bound(img, eyeCascade, 1.1, 12, (0, 0, 255), "eye")

    return img


def mainprogram():
    # cap = cv2.VideoCapture('rtsp://192.168.137.51:8080/h264_pcm.sdp')
    cap = cv2.VideoCapture(0)

    while (True):
        ret, frame = cap.read()
        frame = detect(frame, faceCascade, eyeCascade)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()




if __name__ == "__main__":
    # mainprogram()
    # testocr()
    # vdo_ocr()
    barcodecap()

