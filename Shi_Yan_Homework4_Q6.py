'''
PYTHON VERSION 2.7.10
AUTHOR: YAN SHI
UPDATED: October 9, 2016

PROMPT:
    Write a function or a program which returns or prints the nth Fibonacci number.
'''

def fibonacci_numbers(number):
    a, b = 0, 1
    for i in range(number):
        a, b = b, a + b

    return a

print "This program prints the nth Fibonacci number."
number = input("What nth Fibonacci number are you looking for? ")
output = fibonacci_numbers(number)
print "The Fibonacci number is " + str(output) + "."
