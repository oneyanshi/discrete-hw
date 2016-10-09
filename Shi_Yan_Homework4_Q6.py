'''
PYTHON VERSION 2.7.10
AUTHOR: YAN SHI
UPDATED: October 9, 2016

PROMPT:
    Write a function or a program which returns or prints the nth Fibonacci number.
    Fn = Fn-1 + Fn-2
    F0 = 0 and F1 = 1
'''

def fibonacci_numbers(number):
    f0, f1 = 0, 1
    for i in range(number):
        f0, f1 = f1, f0 + f1

    return f0

print "This program prints the nth Fibonacci number."
number = input("What nth Fibonacci number are you looking for? ")
output = fibonacci_numbers(number)
print "The Fibonacci number is " + str(output) + "."
