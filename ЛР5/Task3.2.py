import matplotlib.pyplot as plt
import numpy as np
def z(x, y):
    return x**0.25 + y**0.25
def p(x, y):
    return x**2 - y**2
def t(x, y):
    return 2 * x + 3 * y
def k(x, y):
    return x**2 + y**2
def s(x, y):
    return 2 + 2*x + 2*y - x**2 - y**2

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

X, Y = np.meshgrid(x, y)

plt.figure(figsize=(12, 6))

plt.subplot(231)
plt.plot(x, z(x, 0), label='y=0')
plt.plot(x, z(x, 5), label='y=5')
plt.plot(x, z(x, 10), label='y=10')
plt.xlabel('x')
plt.ylabel('z')
plt.title('z(x, y)')
plt.legend()

plt.subplot(232)
plt.plot(x, p(x, 0), label='y=0')
plt.plot(x, p(x, 5), label='y=5')
plt.plot(x, p(x, 10), label='y=10')
plt.xlabel('x')
plt.ylabel('p')
plt.title('p(x, y)')
plt.legend()

plt.subplot(233)
plt.plot(x, t(x, 0), label='y=0')
plt.plot(x, t(x, 5), label='y=5')
plt.plot(x, t(x, 10), label='y=10')
plt.xlabel('x')
plt.ylabel('t')
plt.title('t(x, y)')
plt.legend()

plt.subplot(234)
plt.plot(x, k(x, 0), label='y=0')
plt.plot(x, k(x, 5), label='y=5')
plt.plot(x, k(x, 10), label='y=10')
plt.xlabel('x')
plt.ylabel('k')
plt.title('k(x, y)')
plt.legend()

plt.subplot(235)
plt.plot(x, s(x, 0), label='y=0')
plt.plot(x, s(x, 5), label='y=5')
plt.plot(x, s(x, 10), label='y=10')
plt.xlabel('x')
plt.ylabel('s')
plt.title('s(x, y)')
plt.legend()
plt.show()
