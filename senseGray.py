import sys
sys.path.insert(0,'/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')


from pybot import usb4butia

robot =  usb4butia.USB4Butia()
version = robot.getFirmwareVersion()

while True:
    sensor1 = robot.getGray(5)
    sensor2 = robot.getGray(6)
    print str(sensor1) + " --- " + str(sensor2)
