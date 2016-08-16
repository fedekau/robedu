class GrayCalibrator:
    def __init__(self, sensor):
	self.sensor = sensor

    def calibrate(self):
	avg = []
	colors = ['white', 'black']
	for c in colors:
	    print "Please position the sensor in port %(self.sensor.port)s over a %(c)s surface" % locals()
	    input("Press Enter to continue...")

	    a = self.measure_average()
	    avg.append(a)

	    print "Average for this sensor: %(a)s" % locals()

	threshold = min(avg) + (abs([0] - [1]) / 2)
	sensor.threshold = threshold
	print "The threshold is: %(threshold)s" % locals()

    def measure_average(self):
	s = 0
	for i in range(0, 10000):
	    s += sensor.value()
	return  s / 10000

