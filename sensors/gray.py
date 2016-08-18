class Gray:
    def __init__(self, robot, port, threshold = 30000):
	self.robot = robot
	self.port = port
	self.threshold = threshold

    def value(self):
	return self.robot.getGray(self.port)

    def seeing_white(self):
	return self.value() < self.threshold

    def seeing_black(self):
	return self.value() > self.threshold

