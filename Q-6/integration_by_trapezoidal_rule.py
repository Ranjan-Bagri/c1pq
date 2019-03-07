from math import sqrt,sin,pi

def f(x):
	return (1/sqrt(1-0.25*((sin(x))**2)))

def trap(func,a,b):
	n = 1000
	h = (b-a)/n
	s = (1/2)*(func(a)+func(b))

	for i in range(1,n):
		s += func(a+i*h)
	return h*s

u_lim=pi/2
print(trap(f,0,u_lim))