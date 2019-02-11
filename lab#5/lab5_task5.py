class Point(object):
	def __init__(self,x = 0, y = 0):
		self.x = x
		self.y = y
	def __str__(self):
		return "string method"
	def __add__(self, other):
		return (self.x + other.x, self.y + other.y)

point1 = Point(4,6)
point2 = Point(5,9)
print(point1.__str__())
print(point1.__add__(point2))
