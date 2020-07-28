import math
import numpy as np

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
	#Rotary lidar (square hitbox)
	def get_lidar(self,grid,min_radius=10,max_radius=30):
		p0 = self.get_pos()
		print(p0[0],',',p0[1])
		p_max = grid.shape
		hitbox = np.zeros((2*max_radius,2*max_radius,3))
		for x in range(2*max_radius):
			for y in range(2*max_radius):
				px = (p0[0] - max_radius) + x
				py = (p0[1] - max_radius) + y
				if (px < 0 
					or py < 0 
					or px > p_max[0]-1 
					or py > p_max[1]-1
					or ((px > (p0[0] - min_radius) and px < (p0[0] + min_radius))
					and (py > (p0[1] - min_radius) and py < (p0[1] + min_radius)))):
						hitbox[x,y] = [255,255,255]
				else:
					hitbox[y,x] = grid[py,px] 
		return hitbox
