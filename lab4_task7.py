import string

def sed(pstring,rstring,file1,file2):
	try:

		myfile1 = open(file1)
		myfile2 = open(file2,'w+')


		content = myfile1.read()

		if pstring in content:
			content1 = content.replace(pstring,rstring)
		myfile2.write(content1)

		print(content)
		print(content1)

	except IOError:
		print("file not found")

	myfile1.close()
	myfile2.close()

sed('This is','These are','task7file1.txt','task7file2.txt')
