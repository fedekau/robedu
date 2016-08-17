from behaviours.behaviour import Behaviour

class Move(Behaviour):
    FORWARD = 0
    BACKWARDS = 1

    SLOW = 128
    MEDIUM = 512
    FAST = 1023

    def __init__(self, robot):
	self.robot = robot

    def forward(self, speed):
	self.robot.set2MotorSpeed(self.FORWARD, speed, self.FORWARD, speed)

    def backwards(self, speed):
	self.robot.set2MotorSpeed(self.BACKWARDS, speed, self.BACKWARDS, speed)

