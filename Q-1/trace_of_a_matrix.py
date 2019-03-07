A=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
n=len(A)

for i in range(n):
	sum+=A[i][i]

print("Trace of this matrix is %s" % sum)