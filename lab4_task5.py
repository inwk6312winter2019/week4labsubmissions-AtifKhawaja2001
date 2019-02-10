import string
import math

def lower():
	res = []
	l = []
	punc = string.punctuation
	d = dict()
	c = 0
	myfile = open('book.txt')
	for line in myfile:
		line1 = line.strip(string.whitespace)
		for word in line1:
			c = c+1
			for i in word:
				l.append(i)

		for i in range(len(l)):
			for j in punc:
				if l[i] == j:
					del(l[i])
					l.insert(i,' ')


	final_word = ''.join(l)
	small_word = final_word.lower()
	#print(small_word)

	line = small_word.split()
	for i in line:
		res.append(i)

	list_to_dict(res,d)

def list_to_dict(res,d):

	for k in res:
		d[k] = d.get(k,0) + 1
		val = d[k]
		d.setdefault(k,val)
	frequent_words(d)

def frequent_words(d):
	lt = []
	sub = []
	t = d.items()
	for key,value in t:
		lt.append(key)
		lt.append(value)
#^^^ This code creates a dict_items object and then puts that into a list called lt.

	for i in range(0,len(lt),2):
		sub.append(lt[i:i+2])
	sub.sort(key = lambda s:s[1],reverse = True)
#^^^ This code creates a sublist called sub from list lt which has sublists of two indices containing key and value pair of each word.
#^^^ Then it also sorts the sublist with respect to 2nd index in each sublist (because 2nd index is the value).
	rank = 0
	a = []
	b = []
	print('Rank','Word','Freq','log_f','log_r', sep = '\t\t\t')
	print('\n')
	for i in range(len(sub)):
		sub1 = sub[i]
		rank = rank + 1
		log_r = math.log10(rank)
		a.append(log_r)
		for j in range(0,len(sub1)-1):
			log_f = math.log10(sub1[j+1])
			b.append(log_f)
			print(rank, sub1[j], sub1[j+1], log_f, log_r, sep = '\t\t\t ')

	matplot(a,b)

#^^^ This code prints only the words from first 20 indices in list sub which are eventually the most frequently used 20 words in the book.
import matplotlib.pyplot as pyplot
def matplot(log_r,log_f):
	pyplot.clf()
	pyplot.xscale('log')
	pyplot.yscale('log')
	pyplot.title("zipf")
	pyplot.xlabel("rank")
	pyplot.ylabel("frequency")
	pyplot.plot(log_r,log_f)
	pyplot.show()

lower()
