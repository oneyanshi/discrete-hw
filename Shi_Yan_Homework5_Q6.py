'''
PYTHON VERSION 2.7.10
AUTHOR: YAN SHI
DATE: November 6, 2017

	PROMPT:

  Write a program which raises a to the k mod n. Remember that a^k
  will start getting big fast, so you'll want to "mod out" by n after
  each new multiplication by a.

  answer = a^k mod n

'''

def raisePowerMod(a, k, n):
	answer = 1
	while 1:
		if k % 2 == 1:
			answer = answer * a % n
		k /=2
		if k == 0:
			break
		a = a * a % n

	return answer

def main():
	print "This finds a^k mod n."
	a, k, n = input("a: "), input("k: "), input("n: ")
	print "The answer is: " + str(raisePowerMod(a, k, n))
	user_input = input("Would you like to try again? Y = 1 | N = 0 \n" )
	if user_input == 1:
		main()
	elif user_input == 0:
		return 
	else:
		user_input = "Invalid. Y = 1 | N = 0 \n"

main()
