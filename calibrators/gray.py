import os

class GrayCalibrator:
    CONFIG_FILE = "gray_sensors.conf"
    MEASUREMENTS = 1000

    def __init__(self, sensors):
	self.sensors = sensors

    def calibrate(self):
	if (is_calibrated()):
	    load_calibration()
	else:
	    generate_calibration()

    def is_calibrated(self):
	return os.path.exists(CONFIG_FILE)

    def load_calibration(self):
	with open(CONFIG_FILE, 'a+') as f:
		config = f.readLines()
		for i in config:
		    p = i.split('\t')[0]
		    t = i.split('\t')[1]
		    sensor = next(s for s in sensor if s.port == p)
		    sensor.threshold = t

    def generate_calibration(self):
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
	with open(CONFIG_FILE, "w") as f:
	    for s in self.sensors:
		f.write(str(s.port) + '\t' + str(s.threshold) + '\n')


    def measure_average(self):
	s = [0] * len(self.sensors)

	for i in range(0, MEASUREMENTS):
	    for sensor in self.sensors:
	        s[self.sensors.index(sensor)] += sensor.value()

	for sensor in self.sensors:
	    s[self.sensors.index(sensor)] = s[self.sensors.index(sensor)] / MEASUREMENTS
	return s


