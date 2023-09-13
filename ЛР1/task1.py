num = int(input())
sum = 0
while num > 0:
    if num % 10 % 2 == 0:
        sum += num % 10
    num //= 10
print("Сумма чётных цифр числа: ", sum)
