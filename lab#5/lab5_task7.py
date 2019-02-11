class Kangaroo:
	def __init__(self):
		self.pouch_contents=[]
	def put_in_pouch(self,ob):
		self.pouch_contents.append(ob)
	def __str__(self):
		return "string object = "+str(self.pouch_contents)

kanga=Kangaroo()
roo=Kangaroo()
roo.pouch_contents.append('roo object')
kanga.put_in_pouch(roo)

for ob in kanga.pouch_contents:
	print('Kanga object = ',ob)
