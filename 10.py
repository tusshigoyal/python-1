#! /usr/bin/python3
a=input("enter a number")
b=input("enter b number")

def name(a,b):
# here a=hello and b=world
# so var2 will be helloworld here

	var2=a+b
	print(var2,"<-- this is inside")

# whille return var2(helloworld)
	return var2

print(name(a,b))  # here print is helloworld

var2=a  
print("outside",var2)  #output -> hello
