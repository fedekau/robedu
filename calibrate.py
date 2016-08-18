import sys

sys.path.insert(0,'/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')

from pybot import usb4butia

from sensors.gray import Gray
from calibrators.gray import GrayCalibrator

robot =  usb4butia.USB4Butia()
version = robot.getFirmwareVersion()

center = Gray(robot, 4)
left = Gray(robot, 5)
right = Gray(robot, 6)

calibrator = GrayCalibrator(center, left, right)
calibrator.calibrate()

open('rescue.conf', 'w+').close()
conf = open('rescue.conf', 'a')

conf.writeln("center: {port: center.port, threshold: center.threshold}\n")
conf.writeln("left: {port: left.port, threshold: left.threshold}\n")
conf.writeln("right: {port: right.port, threshold: right.threshold}\n")

