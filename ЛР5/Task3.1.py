import numpy as np
import matplotlib.pyplot as plt

def l(x, c):
    return (np.abs(2*x-c))**(3/5)+0.567

x = 3.67
a_values = np.arange(-10, 1, 0.75)

y = l(x, a_values)

print("Значение функции:")
print(y)

print("Наибольшее значение: ", np.max(y))
print("Наименьшее значение: ", np.min(y))
print("Срденее значение: ", np.mean(y))

print("Количество элементов массива: ", len(y))
print("Отсортированный массив: ", y.sort())

plt.plot(a_values, y, marker='o', label='l(x)')
plt.plot(a_values, np.full_like(a_values, np.mean(y)), marker='s', label='Среднее значение')

plt.xlabel('a')
plt.ylabel('y')
plt.title('График функции l(x)')
plt.legend()

plt.show()