def armstrong(x):
        k = str(x)
        res = 0
        
        for i in range(0,len(k)):
                res += int(k[i])**3

        if (res==x):
        	return "%s is an Armstrong Number"%x
        else:
        	return "%s is not an Armstrong Number"%x

print(armstrong(153))