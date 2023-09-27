import json
firm_data = []
total_profit = 0
count_profitable_firms = 0

with open('firm_data.txt', 'r') as file:
    for line in file:
        line = line.strip()
        firm, ownership, revenue, costs = line.split()
        revenue = int(revenue)
        costs = int(costs)
        profit = revenue - costs
        if profit > 0:
            count_profitable_firms += 1
            total_profit += profit
        firm_data.append({firm: profit})

average_profit = total_profit / count_profitable_firms if count_profitable_firms > 0 else 0

result = [firm_data, {'average_profit': average_profit}]


with open('result.json', 'w') as file:
    json.dump(result, file)