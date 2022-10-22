from math import sqrt
import matplotlib.pyplot as plt

def equat(a,b,c):
    if pow(b,2)-4*a*c > 0:
        return (-b+sqrt(pow(b,2)-4*a*c))/(2*a), (-b-sqrt(pow(b,2)-4*a*c))/(2*a)
    elif pow(b,2)-4*a*c == 0:
        return (-b+sqrt(pow(b,2)-4*a*c))/(2*a)
    else:
        return('no real roots')

a, b, c = [int(i) for i in input('enter a, b, c: ').split(',')]

xs = list(range(int(input('enter left border: ')), int(input('enter right border: '))))
ys = [a*xs[j]**2 + b*xs[j] + c for j in range(len(xs))]
plt.plot(xs, ys)
plt.xlabel('x')
plt.ylabel('y')
plt.title('quadratic function')
plt.grid(True)
plt.show()