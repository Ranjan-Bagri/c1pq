x=[87,91,85,75,28,122,66,56]
mean=sum(x)/len(x)
print(mean)
x_square=[i**2 for i in x]
rms=(sum(x_square)/len(x))**0.5
print(rms)