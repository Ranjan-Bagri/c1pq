from random import *

def pi(n):
	square=0
	circle=0
	while square<n:
		x=random()
		y=random()
		if ((x**2+y**2)<=1):
			circle+=1
		square+=1
	return (circle/square)*4

print(pi(50000000))