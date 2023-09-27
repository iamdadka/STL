prices = []
matching_items = []

with open('products.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        name, price = line.split()
        price = float(price)
        prices.append(price)

        if 10 <= price <= 50:
            matching_items.append(line)

average_price = sum(prices) / len(prices)

print("Товары с ценой от 10 до 50 рублей:")
for item in matching_items:
    print(item)

print("Средняя стоимость всех товаров:", average_price)