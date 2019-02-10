import math
class point:

	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y
	def distance(a,b):
		dist = math.sqrt(((a.x - b.x))**2 + ((a.y - b.y))**2)
		return dist
pt1 = point(60,50)
pt2 = point(65,78)

print(point.distance(pt1,pt2))
