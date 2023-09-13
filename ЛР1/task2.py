str = input()
new_str = str.split()
max = 0
sum = 0
max_str = ''
for a in new_str:
    if len(a) <= max:
        continue
    max = len(a)
    max_str = a
for i in range(0, len(str)):
    if str[i].isdigit():
        sum += int(str[i])
print("Самое длинное слово в строке ", max_str)
print("Обратный регистр", str.swapcase())
print("Сумма цифр в строке ", sum)

