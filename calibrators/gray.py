class GrayCalibrator:
    MEASUREMENTS = 1000

    def __init__(self, sensors):
	self.sensors = sensors

    def calibrate(self):
	avg = []
	colors = ['white', 'black']
	for c in colors:
	    print "Please position the gray sensors over a %(c)s surface" % locals()
	    raw_input("Press Enter to continue...")

	    a = self.measure_average()
	    avg.append(a)

	    print "Average for the sensors are: %(a)s" % locals()

	for sensor in self.sensors:
	    i = self.sensors.index(sensor)
	    threshold = min(avg[0][i], avg[1][i]) + (abs(avg[0][i] - avg[1][i]) / 2)
	    self.sensor.threshold = threshold
	    print "The threshold for sensor in %(sensor.port)s is: %(threshold)s" % locals()

    def measure_average(self):
	s = [0] * len(self.sensors)

	for i in range(0, MEASUREMENTS):
	    for sensor in self.sensors:
	        s[self.sensors.index(sensor)] += sensor.value()

	for sensor in self.sensors:
	    s[self.sensors.index(sensor)] = s[self.sensors.index(sensor)] / MEASUREMENTS
	return s


