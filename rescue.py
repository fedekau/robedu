import time
import sys
sys.path.insert(0,'/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')

from pybot import usb4butia

robot =  usb4butia.USB4Butia()
version = robot.getFirmwareVersion()

FORWARD = 0
BACKWARDS = 1

SLOW = 128
MEDIUM = 512
FAST = 1023

THRESHOLD_LEFT = 20500
THRESHOLD_RIGHT = 20000

def forward(speed):
	robot.set2MotorSpeed(FORWARD, speed, FORWARD, speed)

def backwards(speed):
	robot.set2MotorSpeed(BACKWARDS, speed, BACKWARDS, speed)

def turnLeft(speed):
	robot.set2MotorSpeed(BACKWARDS, speed, FORWARD, speed)

def turnRight(speed):
	robot.set2MotorSpeed(FORWARD, speed, BACKWARDS, speed)


while True:
    sensor1 = robot.getGray(5)
    sensor2 = robot.getGray(6)

    print str(sensor1) + " " + str(sensor2)

    time.sleep(1)

    if ((sensor1 < THRESHOLD_LEFT) and (sensor2 < THRESHOLD_RIGHT)):
    	forward(MEDIUM)
    	print "FORWARD"
    else:
    	if(sensor1 < THRESHOLD_LEFT):
    		turnRight(MEDIUM)
    		print "RIGHT"
    	else:
    		turnLeft(MEDIUM)
    		print "LEFT"





