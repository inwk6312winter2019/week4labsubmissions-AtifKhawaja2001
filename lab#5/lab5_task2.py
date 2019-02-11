import math
class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

#Returns distance between two points
	def distance_between_points(self,other):
		return math.sqrt(((other.x-self.x)**2)-((other.y-self.y)**2)) 

class Rectangle(Point):
	def __init__(self,width=0,height=0,corner=(0,0)):
		self.width=width
		self.height=height
		self.corner=Point(corner[0],corner[1])

	def __str__(self):
		return 'WIDTH::'+str(self.width)+' HEIGHT::'+str(self.height)+' CORNER X::'+str(self.corner.x)+' Y::'+str(self.corner.y)


	def corn(self):
		corner1=(self.corner.x,self.corner.y)
		cornerx=(self.corner.x+self.height,self.corner.y)
		cornery=(self.corner.x,self.corner.y+self.width)
		corner2=(cornerx[0],cornerx[1]+self.width)
		return (corner1,cornerx,cornery,corner2)

	def center(self):
		corners=self.corn()
		cornerx=corners[1]
		cornery=corners[2]
		return ((cornerx[0]+cornery[0])/2,(cornerx[1]+cornery[1])/2)

	def move_rectangle(self,dx,dy):
		corners=self.corn()
		cornerlist=[]
		for c in corners:
			cornerlist.append((c[0]+dx,c[1]+dy))
		return cornerlist

rec=Rectangle(20,30,(15,25))
rec2=rec

print('Coordinates = ',rec.corn())

print('Center = ',rec.center())


print('Modified Cordinates = ',rec.move_rectangle(20,20))


print('Moved Cordinates = ',rec2.move_rectangle(30,25))
