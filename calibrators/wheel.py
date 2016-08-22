import os
import time

class WheelCalibrator:
    CONFIG_FILE = "wheel_drift.conf"

    def __init__(self, move):
	self.move = move

    def calibrate(self):
	if (self.is_calibrated()):
	    self.load_calibration()
	else:
	    self.generate_calibration()

    def is_calibrated(self):
	return os.path.exists(self.CONFIG_FILE)

    def load_calibration(self):
	with open(self.CONFIG_FILE, 'r') as f:
		config = f.readlines()
	        self.move.drift = int(config[0])

    def generate_calibration(self):
	command = raw_input("Ingres: start, left, right or stop: ")
	while command != "stop":
		self.move.forward()
		time.sleep(5)
		
		self.move.stop()	
		command = raw_input("Ingres: start, left, right or stop: ")
		if (command == "left"):
			self.move.drift = self.move.drift + 1
		if (command == "right"):
			self.move.drift = self.move.drift - 1
			
		
	with open(self.CONFIG_FILE, "w") as f:
		f.write(str(self.move.drift) + '\n')

