class String:
    def __init__(self, value):
        self.value = value

    def length(self):
        return len(self.value)

    def reverse(self):
        return self.value[::-1]

    def uppercase(self):
        return self.value.upper()

    def is_palindrome(self):
        return self.value == self.value[::-1]

    def starts_with(self, prefix):
        return self.value.startswith(prefix)

my_string = String("+Hello, world!")
print("Длина строки: ", my_string.length())
print("Перевернутая строка: ", my_string.reverse())
print("Строка в верхнем регистре: ", my_string.uppercase())
print("Является ли строка палиндромом: ", my_string.is_palindrome())
print("Начинается ли строка с + :", my_string.starts_with("+"))

