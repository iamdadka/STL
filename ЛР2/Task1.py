def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
        return
    return result


def main():
    while True:
        operation = input("Введите операцию +, -, *, / или '0' для выхода: ")

        if operation == '0':
            break

        if operation not in ['+', '-', '*', '/']:
            print("Операция введена некорректно, попробуйте ещё раз")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            print("Результат:", result)

        except ValueError:
            print("Неверный тип данных")

main()

