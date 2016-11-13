'''
PYTHON VERSION 2.7.10
AUTHOR: YAN SHI
DATE: November 6, 2017

	PROMPT:

  Write a program which finds inverses mod n. Your program will need to check
  that an inverse exists, and then find it if it does.

  -->
  Given two integers a and m, we find modular multiplicative inverse of
  'a' under modulo m

  m(x) congruent 1 mod n

  x's value can be from 0 to m-1

  constraints:
  multiplicative inverse of a modulo n exists if and only if a and n are
  relatively prime (i.e. gcd(m, n) = 1)

  --> Extended Euclidean Algorithm
  ax + by = gcd(a, b)

'''
def gcd(m,n):
	m,n=abs(m),abs(n)
	m,n=max(m,n),min(m,n)
	mm,nn=m,n #Keep original values
	M=[1,0]
	N=[0,1]
	while n != 0:
		q,r=m//n,m%n
		M[0],N[0]=N[0],M[0]-N[0]*q
		M[1],N[1]=N[1],M[1]-N[1]*q
		m,n=n,r
	return m, M[1], N[1]

def modInverse(a, n):
	g, x, y = gcd(a, n)
	if g != 1:
		raise ValueError
	return x % n

def main():
	print "This calculates the multiplcative inverse of an integer a modulo n."
	a = input("Please input an integer a: ")
	n = input("Please input an integer modulo n: ")
	print modInverse(a, n)

	user_input = input("Would you like to try again? Y = 1 | N = 0 \n \n" )
	if user_input == 1:
		main()
	elif user_input == 0:
		return

	else:
		user_input = input("Please try again. Y = 1 | N = 0 \n \n ")

main()
