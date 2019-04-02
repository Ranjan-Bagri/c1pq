from math import cos

def f(x):
    return cos(x)-3*x+1

def derive(func,a):
    h=1e-15
    s=func(a+h)-func(a)
    return float(s)/h

def newton_raphson(x):
    c = x
    n = 4

    for i in range(n):
    	k = c - (f(c)/derive(f,c))
    	c = k
    return k

print(newton_raphson(1))
