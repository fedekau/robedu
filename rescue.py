import time
import sys

sys.path.insert(0,'/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')

from pybot import usb4butia

from sensors.gray import Gray
from calibrators.gray import GrayCalibrator

from behaviours.move import Move
from behaviours.turn import Turn

robot =  usb4butia.USB4Butia()
version = robot.getFirmwareVersion()

left = Gray(robot, 5)
right = Gray(robot, 6)

leftCalibrator = GrayCalibrator(left)
rightCalibrator = GrayCalibrator(right)

leftCalibrator.calibrate()
rightCalibrator.calibrate()

move = Move(robot)
turn = Turn(robot)

while True:
    if ((left.seeing_white()) and (right.seeing_white())):
	move.forward()
    	print "FORWARD"
    else:
    	if(left.seeing_white()):
	    turn.right()
    	    print "RIGHT"
    	else:
	    turn.left()
	    print "LEFT"


