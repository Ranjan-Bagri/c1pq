def fibonacci():
	a=0
	b=1
	i=0
	while i<=20:
		c=a+b
		a=b
		b=c
		print(c)
		i+=1

fibonacci()