class Time(object):
	def __init__(self,hours,min,sec):
		self.hours = hours
		self.min = min
		self.sec = sec
	def print_time(self):
		print("{:02}:{:02}:{:02}" .format(self.hours,self.min,self.sec))


	def is_after(self,other):
		return ((self.hours)*3600 + (self.min)*60 + self.sec) < ((other.hours)*3600 + (other.min)*60 + other.sec)
#^^^The line above checks if self time is less than the other time or not. It returns the boolean function True or False based on the result

t1 =  Time(30,20,11)
t2 =  Time(30,20,12)

print(t1.is_after(t2))
