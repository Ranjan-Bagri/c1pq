from math import factorial

xs = [2, 4, 6, 8, 10]
ys = [0.75, 2.00, 3.50, 5.35, 8.00]

def u_dec(u,n):
    x_temp = u
    for i in range(0,n):
        x_temp *= (u-i)
        return x_temp


def forward(x,xp,yp):
    n = len(xp)  
    y_diff = [[0]*n for i in range(n)]
    
    for i in range(0,n):
        y_diff[i][0] = yp[i]
    
    for i in range(1,n):
        for j in range(0,n-i):
            y_diff[j][i] = y_diff[j+1][i-1] - y_diff[j][i-1]

    sum = y_diff[0][0] 
    
    u = (x - xp[0])/(xp[1]-xp[0]) 

    for i in range(1,n):
        sum += (u_dec(u,i)*y_diff[0][i])/factorial(i)

    return sum

print(xs)
print(ys)
print(forward(5,xs,ys)) 
