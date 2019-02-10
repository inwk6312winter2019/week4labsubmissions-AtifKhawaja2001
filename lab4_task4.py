import string
def word_list():
	l = []
	res = []
	d = dict()
	c = 0
	punc = string.punctuation

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
		word = ''.join(l)
		word1 = word.lower()
		print(word1)

		word2 = word1.split()
		for i in word2:
			res.append(i)

	list_to_dict(res,d)

	l2 = []
	emp = []
	d1 = dict()
	myfile = open('words.txt')
	for word in myfile:
		emp.append(word)

	list_to_dict(emp,d1)

	difference(d,d1)

#This code prints the word that are in the book but not in word list
def difference(d,d1):
	diff = set(d) - set(d1)
	print(diff)

#^^^

def list_to_dict(res,d):
	for k in res:
		d[k] = d.get(k,0) + 1
		d.setdefault(k,d[k])
	#print(d)

word_list()
