import math
from visual import *
Scale = 0.001


#Set up conversion from spherical coordinates to cartesian coordinates
def Spherical_to_Cartesian(r, theta, phi):
	x = r*sin(phi)*cos(theta)
	y = r*sin(phi)*sin(theta)
	z = r*cos(phi)
	return (x,y,z)
P = points(pos = [(0.000001,0,0)], size = 1, color = color.red)
Fly = arrow(pos = (0.000001,0,0), axis = (0,0,1), shaftwidth = 0.1)
ball = sphere(pos=(0,0,0), radius=1, opacity = 0.4)
CoordsOld = (0,0,0)
for t in range(1,20000):
	Phi = t*Scale
	Theta = 3*t*Scale
	Coords = Spherical_to_Cartesian(1.0,Theta,Phi)
	Fly.axis = Coords
	P.append(Coords)
	Velocity = 0
	for i in range(0,3):
		Velocity += (CoordsOld[i]-Coords[i])**2
	Velocity = sqrt(Velocity)
	print Velocity
	CoordsOld = Coords
	rate(1000)
	
