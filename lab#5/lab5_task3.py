class Time(object):
	def __init__(self,hours,min,sec):
		self.hours = hours
		self.min = min
		self.sec = sec
	def time(self):
		print("{:02}:{:02}:{:02}".format(self.hours,self.min,self.sec))

t = Time(5,3,2)
t.time()
