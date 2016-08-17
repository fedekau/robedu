from behaviours.behaviour import Behaviour

class Move(Behaviour):
    def __init__(self, robot):
	self.robot = robot

    def forward(self, speed):
	self.robot.set2MotorSpeed(self.FORWARD, speed, self.FORWARD, speed)

    def backwards(self, speed):
	self.robot.set2MotorSpeed(self.BACKWARDS, speed, self.BACKWARDS, speed)

