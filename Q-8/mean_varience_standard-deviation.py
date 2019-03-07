x=[34,88,32,12,10]
mean=sum(x)/len(x)
sum=0
for i in range(len(x)):
	sub=(x[i]-mean)**2
	sum+=sub
var=sum/(len(x)-1)
sd=var**0.5
print(mean)
print(var)
print(sd)