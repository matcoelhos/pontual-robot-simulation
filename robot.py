import math

#maximum linear speed of 100 (distance units)/s
#maximum rotation of 100 deg/s
mv = 100
momega = 100

class Robot:
	#Constructor: you must start your robot
	#at a position and rotation conditions
	def __init__(self,px,py,theta):
		self.px = px
		self.py = py
		self.omega = 0
		self.v = 0
		self.theta = theta

	# Change linear speed
	#range +- 100% from maximum linear speed
	def accell_l(self,percentage):
		if percentage > 100:
			percentage = 100
		elif percentage < -100:
			percentage = -100
		self.omega = 0
		self.v = float(percentage/100)*mv

	#Change angular speed
	#range +- 100% from maximum angular speed
	def accell_w(self,percentage):
		if percentage > 100:
			percentage = 100
		elif percentage < -100:
			percentage = -100
		self.v = 0
		self.omega = float(percentage/100)*momega

	#run simulation step (delta_t in seconds)
	def step(self,delta_t = 0.01):
		vx = self.v * math.cos(self.theta*math.pi/180)
		vy = self.v * math.sin(self.theta*math.pi/180)
		self.px = self.px + vx*delta_t
		self.py = self.py + vy*delta_t
		self.theta = self.theta + self.omega*delta_t
		if (self.theta >= 360):
			self.theta-=360

	## Sensors
	#Position
	def get_pos(self):
		return (int(self.px), int(self.py))
	#Rotation
	def get_theta(self):
		return self.theta