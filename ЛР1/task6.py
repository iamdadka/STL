numbers = (-2, 5, -10, 8, -4, 3)
numbers_list = list(numbers)
for num in numbers_list:
    if num < 0:
        numbers_list.remove(num)
        break
numbers_tuple = tuple(numbers_list)
print("Кортеж без первого отрицательного элемента", numbers_tuple)
