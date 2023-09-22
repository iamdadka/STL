def process_data(data):
    if isinstance(data, list):
        even_sum = sum(num for num in data if num % 2 == 0)
        data = [num for num in data if num != 0]
        return even_sum, data

    elif isinstance(data, set):
        max_value = max(data)
        data = {num for num in data if num != max_value}
        return data

    elif isinstance(data, int):
        if data < 2:
            is_prime = False
        else:
            is_prime = True
            for i in range(2, int(data ** 0.5) + 1):
                if data % i == 0:
                    is_prime = False
                    break

        return is_prime

    elif isinstance(data, str):
        char_count = {}
        for char in data:
            char_count[char] = char_count.get(char, 0) + 1

        most_common_char = max(char_count, key = char_count.get)

        return most_common_char

list_data = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0]
even_sum, modified_list = process_data(list_data)
print("Сумма четных чисел:", even_sum)
print("Модифицированный список:", modified_list)


set_data = {1, 2, 3, 4, 5, 10, 7, 8, 9, 10}
modified_set = process_data(set_data)
print("Модифицированное множество:", modified_set)


number = 17
is_prime = process_data(number)
print("Число является простым:", is_prime)


string_data = "hello world"
most_common = process_data(string_data)
print("Наиболее часто встречающийся символ:", most_common)