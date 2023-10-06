with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку данных (для завершения введите пустую строку): ")
        if line == "":
            break
        f1.write(line + '\n')

with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    lines = f1.readlines()
    if len(lines) > 0:
        words = lines[0].split()
        if len(words) >= 2:
            target_word = words[1]
            matching_lines = [line for line in lines if target_word in line]
            f2.writelines(matching_lines)

with open('F2.txt', 'r') as f2:
    lines = f2.readlines()
    last_line = lines[len(lines)-1].strip()
    digit_count = sum(c.isdigit() for c in last_line)

print("Количество цифр в последней строке файла F2:", digit_count)