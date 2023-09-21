def sum_columns(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    column_sums = [0] * num_cols
    for j in range(num_cols):
        has_negative = False
        for i in range(num_rows):
            if matrix[i][j] < 0:
                has_negative = True
                break
            column_sums[j] += matrix[i][j]
        if has_negative:
            column_sums[j] = 0
    return column_sums

matrix = [
    [1, 2, 3, 4],
    [5, -6, 7, 8],
    [9, 10, 11, -12],
    [-13, 14, 15, 16]
]

result = sum_columns(matrix)
print("Суммы столбцов без отрицательных элементов:", result)