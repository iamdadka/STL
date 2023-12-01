import numpy as np
X_col2 = np.arange(30, 42)
X_col3 = np.random.randint(60, 83, size=12)
Y = np.random.uniform(13.5, 18.6, size=12)

X = np.column_stack((np.ones(12), X_col2, X_col3))
A = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(Y))
Y_predicted = X.dot(A)

print("Вектор оценок A:")
print(A)

print("\nПроверка результатов:")
print("Исходные значения Y:")
print(Y)
print("Полученные значения Y:")
print(Y_predicted)