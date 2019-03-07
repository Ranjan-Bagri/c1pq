def factorial(n):
	f = 1
	for i in range(2,n+1):
		f*=i
	return f

def n_c_r(N,n):
    return factorial(N)/(factorial(n)*factorial(N-r))

print(n_c_r(7,3))