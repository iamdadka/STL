n = int(input())
list = []
for i in range(1, n + 1):
    if n % i == 0:
        list.append(i)
print("Список делителей числа ", list)
print("Максимальный делитель числа ", max(list))
print("Минимальный делитель числа ", min(list))