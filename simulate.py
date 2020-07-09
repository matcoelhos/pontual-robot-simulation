import cv2
from robot import Robot
import numpy as np
from math import pi

##Example of simulation
# Robot instance:
r = Robot(10,10,0)

##Point parameters
# Radius of circle 
radius = 2
# Blue color in BGR 
color = (50, 255, 0) 
# Line thickness of 2 px 
thickness = 2

##Empty grid
#You can replace using cv2.imread()
#to open you BG
grid = np.zeros((512,512,3))

#Simulation Loop
while True:
	try:
		#copy grid
		img = grid.copy()

		#get robot data (position and rotation)
		pos = r.get_pos()
		theta = r.get_theta()

		#draw robot on image
		img = cv2.circle(img, pos, radius, color, thickness)
		
		#square movement 
		print(pos,theta)
		if (pos == (10,10)):
			if theta == 0:
				r.accell_l(100)
			else:
				r.accell_w(100)
		elif (pos == (100,10)):
			if theta == 90:
				r.accell_l(100)
			else:
				r.accell_w(100)
		elif (pos == (100,100)):
			if theta == 180:
				r.accell_l(80)
			else:
				r.accell_w(100)
		elif (pos == (10,100)):
			if theta == 270:
				r.accell_l(80)
			else:
				r.accell_w(100)
		#run the simulation step after setting the parameters
		r.step(0.01)

		#display robot's last position
		cv2.imshow('grid',img)

		k = cv2.waitKey(10) & 0xFF
		if k == ord('q'):
			break

	except KeyboardInterrupt:
		break