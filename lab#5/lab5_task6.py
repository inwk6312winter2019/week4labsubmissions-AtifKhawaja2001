class Point(object):
	def __init__(self,x = 0, y = 0):
		self.x = x
		self.y = y
	def __str__(self):
		return "string method"
	def __add__(self, other):
		pt_add = Point()
		if (type(other) == tuple):
			pt_add.x = self.x + other[0]
			pt_add.y = self.y + other[1]
			return pt_add
		else:
			pt_add.x = self.x + other.x
			pt_add.y = self.y + other.y
			return pt_add

point1 = Point(7,4)
point2 = (6,5)
print(point1.__str__())
sum1 = point1.__add__(point2)
print(sum1.x)
print(sum1.y)
