import matplotlib.pyplot as plt
import numpy as np
import  cv2
def demo1():
    x = range(4)
    y = (20, 25, 40, 30)
    xticks = ("Mocca","latte","Espresso","tea")
    plt.xticks(x,xticks)
    plt.plot(x, y,'r*--')
    plt.show()

def bar_sub():
    a = 0
    x = range(6)
    y = (100,150,120,200,180,210)
    xticks = ("Thailand","Japan","Australia","Canada","German","Spain")
    f,z = plt.subplots(2, 2)
    titles = ["graph1","graph2","graph3","graph4"]
    colors = ["red","green","blue","orange"]
    for r in range(2):
        for c in range(2):
            z[r, c].bar(x, y, color= colors[a])
            z[r,c].set_yticks(0.5)
            plt.sca(z[r, c])
            plt.title(titles[a])
            plt.xticks(x, xticks)
            plt.axhline(max(y),color = "black",linestyle = "--")
            plt.axhline(min(y), color="black", linestyle="--")

            plt.axhline(sum(y)/len(y),color = "pink",linestyle = "-")
            a=a+1
    f.tight_layout()
    plt.show()

def st1():
    #-------vdo capture--------------
    # cap = cv2.VideoCapture(0)
    # cap.set(3,400)
    # cap.set(4,600)
    # while (True):
    #     ret, frame = cap.read()
    #     # roi = frame[100:600,200:600]
    #     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #     blur = cv2.GaussianBlur(gray,(5,5),0)
        #   thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY)[1]

        #   cnt = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            # cnt = imutils.grab_c
   
    #     canny = cv2.Canny(gray,100,200)
    #     # cv2.imshow('frame', canny)

    #     cv2.putText(canny,'test',(10,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2,cv2.LINE_AA)
    #     cv2.imshow("Show",canny)

    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # cap.release()

    #-------image processing-------------------
    img = cv2.imread('xx.jpg')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_crop = img[100:600,200:600]
    gray = np.float(img_crop)
    corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
    corners = np.int0(corners)
    for c in corners:
        x,y = c.ravel()
        cv2.circle(img,(x,y),3,(255,0,0),-1)
    # template =cv2.imread('')

    # cv2.line(img_crop,(0,0),(100,400),(255,0,0,0),5)
    # cv2.circle(img_crop,(200,200),100,(0,255,255),-1)
    # cv2.rectangle(img_crop,(400,400),(300,300),(0,0,255),-1)
    # cv2.putText(img_crop,'Hello!',(100,100),cv2.FONT_HERSHEY_PLAIN,3,(128,128,255),2)
    # cv2.imshow('test',img_crop)

    # h,w,_ = template.shape
    # res = cv2.matchTemplate(ing,template,cv2.TM_CCOEFF)
    # min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
    # top_left = max_loc
    # bottom_right = (top_left[0]+w,top_left[1]+h)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # plt.imshow(img)
    # plt.show()

if __name__ == '__main__':
    #  bar_sub()
     st1()
