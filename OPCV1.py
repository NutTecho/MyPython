import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')


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

