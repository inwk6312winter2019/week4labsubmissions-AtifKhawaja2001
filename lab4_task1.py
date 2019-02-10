import string

def lower():
	l = []
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
		#print(word)
		word1 = word.lower()
		print(word1)
(lower())

