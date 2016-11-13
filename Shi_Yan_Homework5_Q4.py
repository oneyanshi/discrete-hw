'''
PYTHON VERSION 2.7.10
AUTHOR: YAN SHI
DATE: November 6, 2017

	PROMPT:

	Write a program whose input is an integer a and a modulus n, and
	returns an integer b such that b is congruent to a mod n and b
	lies in the range

	-[n/2] + 1, ..., [n/2]

	For example, the range of modulus 10 would be -4, -3, -2, ... 3, 4, 5;
	for modulus 7, it would be -3, -2, ... 2, 3

	--> Within notes:
	We say that the integers b and a are congruent modulo n if n divides
	b-a evenly  (n | b-a)

'''


def findIntegerB():
	print "b congruent a mod n"
	integer_a = input("Please input an integer, a: ")
	modulus = input("Please input a modulus, n: ")

	for integer_b in range(-(modulus/2)+1, (modulus/2)+1):
		if (integer_b - integer_a) % modulus == 0:
			print integer_b
run = True
while run:
	findIntegerB()
	user_input= input("Would you like to try again? Yes = 1 | No = 0: ")
	if user_input == 1:
		findIntegerB()
	elif user_input == 0:
		run = False
	else:
		user_input = input("Please try again.")
