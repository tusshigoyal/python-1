#!/usr/bin/python3

try:
	filptr=open("file.txt","r")
	try:
		filptr.write("Hello")
	finally:
		filptr.close()
		print("File is closed buddy")
		while True:
    x.append(i)
    y.append(psutil.cpu_percent())
    print(len(y))
    if len(y) >=20:
        y.pop(0)
        x.pop(0)
    ax.plot(x, y, color='b')  
    fig.canvas.draw()

except:
	print("error generated bbye")
