def f(time, temp):
    return 2.5*(100-temp)

def rungeKutta(INIT_TIME, INIT_TEMP, time, h):
    n = int((time - INIT_TIME)/h)
    temp = INIT_TEMP

    for i in range(n):
        k1 = h*f(INIT_TIME, temp)
        k2 = h*f(INIT_TIME+0.5*h, temp+0.5*k1)
        k3 = h*f(INIT_TIME+0.5*h, temp+0.5*k2)
        k4 = h*f(INIT_TIME+h, temp+k3)

        temp += (1.0/6.0)*(k1+2*k2+2*k3+k4)
        INIT_TIME += h
    return temp

t0 = 0
theta0 = 25
t = 1
h = 0.2
print('The value of theta at given time is : %s'%rungeKutta(t0, theta0, t, h))
