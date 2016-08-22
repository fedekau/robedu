import os
import pdb

class GrayCalibrator:
    CONFIG_FILE = "gray_sensors.conf"
    MEASUREMENTS = 1000

    def __init__(self, sensors):
	self.sensors = sensors

    def calibrate(self):
	if (self.is_calibrated()):
	    self.load_calibration()
	else:
	    self.generate_calibration()

    def is_calibrated(self):
	return os.path.exists(self.CONFIG_FILE)

    def load_calibration(self):
	pdb.set_trace()
	with open(self.CONFIG_FILE, 'r') as f:
		config = f.readlines()
		for i in config:
		    p = int(i.split(' ')[0])
		    t = int(i.split(' ')[1])
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
	with open(self.CONFIG_FILE, "w") as f:
	    for s in self.sensors:
		f.write(str(s.port) + ' ' + str(s.threshold) + '\n')


    def measure_average(self):
	s = [0] * len(self.sensors)

	for i in range(0, self.MEASUREMENTS):
	    for sensor in self.sensors:
	        s[self.sensors.index(sensor)] += sensor.value()

	for sensor in self.sensors:
	    s[self.sensors.index(sensor)] = s[self.sensors.index(sensor)] / self.MEASUREMENTS
	return s


