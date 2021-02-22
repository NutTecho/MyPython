# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
from tkinter import *

# Notify user:
# Program example:
RDK = Robolink()
root = Tk()

def runrobot(e):

    angle = int(e1.get())
    loop = int(e2.get())
    size = int(e3.get())

    robot = RDK.Item('UR3',ITEM_TYPE_ROBOT)

    home = RDK.Item('home')
    point1 = RDK.Item('point1')
    posref = point1.Pose()

    robot.MoveJ(home)
    robot.MoveJ(point1)

    for i in range(angle +1):
        ang = i*2*pi/angle #ang = 0, 60, 120, ..., 360
        posie = posref*rotz(ang)*transl(size,0,0)*rotz(-ang)
        robot.MoveL(posie)

    robot.MoveL(point1)
    robot.MoveJ(home)

l1 = Label(root,text = "Insert number")
l1.grid(row = 0,column = 0)

l2 = Label(root,text = "Insert loop")
l2.grid(row = 1,column = 0)

l3 = Label(root,text = "Insert size")
l3.grid(row = 2,column = 0)

e1 = Entry(root)
e1.grid(row = 0 , column = 1)

e2 = Entry(root)
e2.grid(row = 1,column = 1)

e3 = Entry(root)
e3.grid(row = 2,column = 1)

b1 = Button(root,text = "Enter")
b1.bind("<Button-1>",runrobot)
b1.grid(row = 3,column = 0,columnspan = 2)



root.mainloop()
