from math import factorial

xs = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
ys = [0.84270, 0.91031, 0.95229, 0.97635, 0.98909, 0.99532]

def u_dec(u, n):
    x_temp = u
    for i in range(0, n):
        x_temp *= (u - i)
        return x_temp


def forward(x, xp, yp):
    n = len(xp)
    y_diff = [[0]*n for i in range(n)]
    for i in range(0, n):
        y_diff[i][0] = yp[i]

    for i in range(1, n):
        for j in range(0, n - i):
            y_diff[j][i] = y_diff[j+1][i-1] - y_diff[j][i-1]

    res = y_diff[0][0]

    u = (x - xp[0])/(xp[1] - xp[0])

    for i in range(1, n):
        res += (u_dec(u, i)*y_diff[0][i])/factorial(i)

    return res

print(xs)
print(ys)
print(forward(1.433, xs, ys))
