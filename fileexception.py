#!/usr/bin/python3

try:
	filptr=open("file.txt","r")
	try:
		filptr.write("Hello")
	finally:
		filptr.close()
		print("File is closed buddy")

except:
	print("error generated bbye")
