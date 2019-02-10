import os

def walk_dir(dirname):
	for root,dirs,files in os.walk(dirname):
		for file in files:
			print(os.path.join(dirname,file))
		for dirt in dirs:
			print(os.path.join(dirname,dirt))

walk_dir(".")
