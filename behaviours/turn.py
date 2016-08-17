from behaviours.behaviour import Behaviour

class Turn(Behaviour):
    FORWARD = 0
    BACKWARDS = 1

    SLOW = 128
    MEDIUM = 512
    FAST = 1023

    def __init__(self, robot):
	self.robot = robot

    def left(self, speed):
	self.robot.set2MotorSpeed(self.BACKWARDS, speed, self.FORWARD, speed)

    def right(self, speed):
	self.robot.set2MotorSpeed(self.FORWARD, speed, self.BACKWARDS, speed)

