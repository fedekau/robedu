from behaviours.behaviour import Behaviour

class Turn(Behaviour):
    def __init__(self, robot):
	self.robot = robot

    def left(self, center = True, speed = Behaviour.MEDIUM):
	if (center):
		self.robot.set2MotorSpeed(self.BACKWARDS, speed, self.FORWARD, speed)
	else:
		self.robot.set2MotorSpeed(self.BACKWARDS, 0, self.FORWARD, speed)

    def right(self, center = True, speed = Behaviour.MEDIUM):
	if (center):
		self.robot.set2MotorSpeed(self.FORWARD, speed, self.BACKWARDS, speed)
	else:
		self.robot.set2MotorSpeed(self.FORWARD, speed, self.BACKWARDS, 0)

