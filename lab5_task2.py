import math

class rectangle:

	def __init__(self,w=0,h=0):
		self.w = w
		self.h = h
	def find_center(w,h):
		xcenter=box.corner.x + (w)/2
		ycenter=box.corner.y + (h)/2
		print('(%g,%g)'%(xcenter,ycenter))
class point:

	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

box = rectangle(4,2)
box.corner = point(1,1)

rectangle.find_center(box.w,box.h)
