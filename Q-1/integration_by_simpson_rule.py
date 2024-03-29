from math import *

def f(x):
	return log(x)

def simp(func,a,b):
	n = 1000000
	h = (b-a)/n
	c=d=0
	for i in range(1,n,2):
		c += func(a+i*h)
	for j in range(2,n,2):
		d += func(a+i*h)
	return (1/3)*h*(func(a)+func(b)+4*c+2*d)

print(simp(f,4,5.2))