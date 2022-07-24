from robolink import *
from robodk import *
RDK = Robolink()

#set robot arm from name
robot = RDK.Item('UR3')

#get target from name
set1 = RDK.Item('set1')
set2 = RDK.Item('set2')
set3 = RDK.Item('set3')

#get position of target
poseref1 = set1.Pose()
poseref2 = set2.Pose()
poseref3 = set3.Pose()

#ouput :
# transl(x,y,z)*rotx(x)*roty(y)*rotz(z)
# Pose(x, y, z,  178.189, 9.657, 180.000):
# [[ 1.00, -0.000, 0.000, x ],
#  [ 0.000, 1.000, 0.000, y ],
#  [ 0.000, 0.000, 1.000, z ],
#  [ 0.000, 0.000, 0.000, 1.000 ]]

#set visible item
set1.setVisible(True)
set2.setVisible(False)


# get item from project
# ITEM_TYPE_ROBOT
# ITEM_TYPE_OBJECT
# ITEM_TYPE_TARGET

gettarget = RDK.ItemList(ITEM_TYPE_TARGET, True)
getobject = RDK.ItemList(ITEM_TYPE_OBJECT, True)
getrobot = RDK.ItemList(ITEM_TYPE_ROBOT, True)
print(gettarget)
print(getobject)
roboti = RDK.Item(getrobot[0])
print(roboti.Name())
print(roboti.Childs()[0].Name())



# command move to target
# robot.MoveJ(set1)
# robot.MoveJ(set2)

# add new target and set position
tx = RDK.AddTarget('data' + str(i+1))
#tx.setPose(transl(500 + ((i+1)*30),70,200) * roty(-pi))
#print(tx.Pose())
#tx.setAsCartesianTarget()

#get item in project
# listrdk = RDK.ItemList()
# print(listrdk)
for i in gettarget:
    setx = RDK.Item(i)
    robot.MoveJ(setx)
    pause(0.5)
