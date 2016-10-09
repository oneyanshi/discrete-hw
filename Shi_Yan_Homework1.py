'''
PYTHON VERSION 2.7.10
AUTHOR: YAN SHI
DATE: September 11, 2016

	PROMPT:

	Let R be the relation defined as follows:

	R = {(m, n) is a set of Z X Z | 0.5 <= m/n <= 1}

	Write a function which takes an integer argument m and
	returns a list consisting of exactly those integers n such that
	(m, n) is a set R.
'''

list_for_n = []
m = input("Enter an integer! ")

def find_integer(m):
	n = abs(m)
	if m%1==0:
		for n in range(n*-2, n*2+1):
			if n!=0:
				if m/n <= 0.5 or m/n <= 1:
					list_for_n.append(n)


	elif m%1!=0:
		print "Please provide an integer."
		m = input("Give me an integer! ")

	elif m==0:
		print "Sorry, can't divide 0/0 and it does not fit the constraints 0.5 <= m/n <= 1"

	print list_for_n

find_integer(m)
