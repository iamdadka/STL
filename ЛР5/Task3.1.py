import numpy as np
import matplotlib.pyplot as plt

def f(x, a):
    return np.e**(a*x) - 3.45 * a

x = 12.1
a_values = np.arange(-5, 12.1, 1.75)

y = f(x, a_values)

print("Значение функции:")
print(y)

print("Наибольшее значение: ", np.max(y))
print("Наименьшее значение: ", np.min(y))
print("Срденее значение: ", np.mean(y))

print("Количество элементов массива: ", len(y))
print("Отсортированный массив: ", y.sort())

plt.plot(a_values, y, marker='o', label='f(x)')
plt.plot(a_values, np.full_like(a_values, np.mean(y)), marker='s', label='Среднее значение')

plt.xlabel('a')
plt.ylabel('y')
plt.title('График функции f(x)')
plt.legend()

plt.show()