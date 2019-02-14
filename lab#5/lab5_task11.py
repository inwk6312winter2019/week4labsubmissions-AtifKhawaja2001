class IP:
	def __init__(self,a,b):
		self.a = a
		self.b = b

	def __str__(self):
		return('IP Address = %s.%s.%s.%s/%d' % (self.a[0],self.a[1],self.a[2],self.a[3],self.b))

	def getnetwork(self):
		l1 = []
		net = format(self.a[0],'08b'),format(self.a[1],'08b'),format(self.a[2],'08b'),format(self.a[3],'08b')
		#^^^converts the given ip address from decimal to binary and puts the values inside a tuple

		d = divmod(self.b,8)
		#defines the to be network portion. For example if the result is (2,4) that means first two octets and 4 bits of third octet in network portion
		net1 = ('%s.%s.%s.%s' % (net[0],net[1],net[2],net[3]))
		list = net1.split('.')

		for i in range(d[0]):
			l1.append(list[i])
		for i in range(d[0]):
			del(list[0])

		l1.append(list[0][0:d[1]])
		#^^^Creates a new list called l1 with all the network bits in it using the result from divmod.

		sum1 = []
		for i in range(len(l1)):
			m = 128
			sum = 0
			for j in range(len(l1[i])):
				sum = sum + (int(l1[i][j])*m)
				m = m/2
			sum1.append(int(sum))
		#^^^sums up the values in list l1 to convert them from binary to decimal

		if d[0] < 3:
			sum1.append(0)

		for i in range(len(sum1)):
			sum1[i] = str(sum1[i])

		network = '.'.join(sum1)
		print("Network Address =",network,'/',self.b)

ip = IP([192,168,202,223],27)
print(ip)
ip.getnetwork()
