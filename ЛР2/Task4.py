def divide_numbers(a, b):
    try:
        result = a / b
        print("Результат деления:", result)
    except ZeroDivisionError:
        print("Ошибка деление на ноль")
    finally:
        print("Блок finally выполняется всегда")

divide_numbers(10, 2)

divide_numbers(5, 0)