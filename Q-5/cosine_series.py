import math

def cos(x,n):
	cosine=0
	y=x*(math.pi/180)
	for i in range(n):
		sign=(-1)**i
		cosine+=(((y**(2*i))/(math.factorial(2*i)))*sign)
	return cosine

x=int(input('Enter the value in degree: '))
n=int(input('Enter the number of terms: '))

print(round(cos(x,n),3))