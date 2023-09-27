with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку данных (для завершения введите пустую строку): ")
        if line == "":
            break
        f1.write(line + '\n')

with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    for line in f1:
        words = line.split()
        if len(words) >= 2 and words[1] in line:
            f2.write(line)

if f2.__sizeof__() == 0:
    with open('F2.txt', 'r') as f2:
        last_line = f2.readlines()[-1]
        digit_count = sum(1 for char in last_line if char.isdigit())
    print("Количество цифр в последней строке файла F2:", digit_count)
else:
    print("Файл 2 пустой")