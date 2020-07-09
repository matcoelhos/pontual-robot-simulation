import cv2
from robot import Robot
import numpy as np

##Example of simulation
# Robot instance:
r = Robot(30,30,0)

def draw_robot(img, pos, theta):
	##Point parameters
	# Radius of circle 
	radius = 5
	# Blue color in BGR 
	color = (50, 255, 0) 
	# Line thickness of 2 px 
	thickness = 2
	img = cv2.circle(img, pos, radius, color, thickness)
	img = cv2.line(img, pos,
					(int(pos[0]+10*np.cos(theta*np.pi/180)),int(pos[1]+10*np.sin(theta*np.pi/180))),
					(0, 0, 255),2)
	return img

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
		img = draw_robot(img,pos, theta)
		
		#square movement 
		print(pos,theta)
		if (pos == (30,30)):
			if theta == 0:
				r.accell_l(100)
			else:
				r.accell_w(100)
		elif (pos == (230,30)):
			if theta == 90:
				r.accell_l(100)
			else:
				r.accell_w(100)
		elif (pos == (230,230)):
			if theta == 180:
				r.accell_l(80)
			else:
				r.accell_w(100)
		elif (pos == (30,230)):
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