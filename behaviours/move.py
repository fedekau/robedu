from behaviours.behaviour import Behaviour

class Move(Behaviour):
    def __init__(self, robot):
	self.robot = robot
	self.drift = 0

    def forward(self, speed = Behaviour.MEDIUM):
	self.robot.set2MotorSpeed(self.FORWARD, speed + self.drift, self.FORWARD, speed)

    def backwards(self, speed = Behaviour.MEDIUM):
	self.robot.set2MotorSpeed(self.BACKWARDS, speed + self.drift, self.BACKWARDS, speed)

    def stop (self):
	self.robot.set2MotorSpeed(0,0,0,0)

