import sys
import time

sys.path.insert(0,'/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')

from pybot import usb4butia

from sensors.gray import Gray
from calibrators.gray import GrayCalibrator
from calibrators.wheel import WheelCalibrator

from behaviours.move import Move
from behaviours.turn import Turn

robot =  usb4butia.USB4Butia()
version = robot.getFirmwareVersion()
print str(version)

left_inner = Gray(robot, 6)
left_outer = Gray(robot, 1)
right_inner = Gray(robot, 5)
right_outer = Gray(robot, 4)

move = Move(robot)
turn = Turn(robot)

grayCalibrator = GrayCalibrator([left_inner, right_inner, left_outer, right_outer])
grayCalibrator.calibrate()

wheelCalibrator = WheelCalibrator(move)
wheelCalibrator.calibrate()

while True:
    if ((left_inner.seeing_white()) and (right_inner.seeing_white()) and (left_outer.seeing_white()) and (right_outer.seeing_white())):
	move.forward()
    	print "FORWARD"

    else:    
	    if(left_inner.seeing_black() and (left_outer.seeing_black())):
		turn.left(False)
		time.sleep(1)
		print "CORNER RIGHT"
	    elif(right_inner.seeing_black() and (right_outer.seeing_black())):
		turn.right(False)
		time.sleep(1)
		print "CORNER LEFT"
	    elif(right_inner.seeing_black() or right_outer.seeing_black()):
		turn.right()
		print "RIGHT"
	    elif(left_inner.seeing_black() or left_outer.seeing_black()):
		turn.left()
		print "LEFT"

	


