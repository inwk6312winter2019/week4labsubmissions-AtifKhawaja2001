import string

def lower():
	l = []
	res = []
	punc = string.punctuation
	d = dict()
	c = 0
	myfile = open('book.txt')
	for line in myfile:
		line1 = line.strip(string.whitespace)
		for word in line1:
			for i in word:
				l.append(i)

		for i in range(len(l)):
			for j in punc:
				if l[i] == j:
					del(l[i])
					l.insert(i,' ')
	#print(l)
	final_word = ''.join(l)
	small_word = final_word.lower()
	print(small_word)

#^^^ This code reads the file, breaks lines into words, removes punctuation from the words and converts them to lowercase

	line = small_word.split()
	for i in line:
		res.append(i)
	for k in res:
		d[k] = d.get(k,0) + 1
		val = d[k]
		d.setdefault(k,val)
	print(d)
#^^^ This code creates a list 'res' from the result of above code and creates a dictionary containing keys and their values

	for k in d:
		if d[k] == 22:
			print("All the words corresponding to this key value = ",end=" ")
			print(k)

#^^^ This code prints some words from the dictionary based on number of times they are used

	num = small_word.split()
	for i in range(len(num)):
		c = c + 1
	print("The total number of words = ", c)

lower()

