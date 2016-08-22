from behaviours.behaviour import Behaviour

class Turn(Behaviour):
    def __init__(self, robot):
	self.robot = robot

    def left(self, speed = Behaviour.MEDIUM):
	self.robot.set2MotorSpeed(self.BACKWARDS, 0, self.FORWARD, speed)

    def right(self, speed = Behaviour.MEDIUM):
	self.robot.set2MotorSpeed(self.FORWARD, speed, self.BACKWARDS, 0)

