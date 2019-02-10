import os
import hashlib

def walk_dir(dirname):
	l = []
	l1 = []
	l_sum = []
	l1_sum = []

	for root,dirs,files in os.walk(dirname):
		for file in files:
			#print(os.path.join(dirname,file))
			l.append(file)
			sum = hashlib.md5(file.encode('utf-8')).hexdigest()
			l_sum.append(sum)
			if '.txt' in file:
				print(file)
			else:
				continue

	print(l_sum)

	for i in range(len(l_sum)):
		for j in range(len(l_sum)):
			if i == j:
				continue
			elif l_sum[i] == l_sum[j]:
				print('A duplicate has been found')
				print(l[i],' ',l[j])


walk_dir('.')
