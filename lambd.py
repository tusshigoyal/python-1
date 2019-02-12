#!/usr/bin/python3


def table(n):
	return lambda a: a*n

n = int(input("Enter number:"))

b = table(n)

for i in range(0,11):
	print(n,"X",i, "=", b(i))

