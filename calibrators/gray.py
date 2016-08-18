class GrayCalibrator:
    def __init__(self, sensor):
	self.sensor = sensor

    def calibrate(self):
	avg = []
	colors = ['white', 'black']
	for c in colors:
	    port = self.sensor.port
	    print "Please position the sensor in port %(port)s over a %(c)s surface" % locals()
	    raw_input("Press Enter to continue...")

	    a = self.measure_average()
	    avg.append(a)

	    print "Average for this sensor: %(a)s" % locals()

	threshold = min(avg[0], avg[1]) + (abs(avg[0] - avg[1]) / 2)
	self.sensor.threshold = threshold
	print "The threshold is: %(threshold)s" % locals()

    def measure_average(self):
	s = 0
	for i in range(0, 1000):
	    s += self.sensor.value()
	return  s / 1000

