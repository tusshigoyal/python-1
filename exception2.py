#!/usr/bin/python3

try:
	a=10
	b=0
	c=a/b
	print(c)

except ArithmeticError:
	print("Arithmatic Exception")

else: 
	print("Divided!!!!")

