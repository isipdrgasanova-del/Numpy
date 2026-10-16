import numpy as np

data_grades = np.array([
    68, 72, 55, 80, 91, 64, 77, 83, 59, 70,
    88, 62, 75, 95, 60, 100, 100, 100, 100, 100,
    67, 73, 58, 81, 90, 65, 78, 84, 61, 71,
    87, 63, 76, 94, 66, 100, 100, 100, 100, 100,
    69, 74, 56, 82, 92, 64, 79, 85, 60, 72,
    0, 0, 0, 0, 0, 65, 77, 83, 58, 70
])

mean_val = np.mean(data_grades)
median_val = np.median(data_grades)
std_val = np.std(data_grades)
var_val = np.var(data_grades)
max_val = np.max(data_grades)
min_val = np.min(data_grades)
range_val = max_val - min_val

print("Задание 1: Статистика по оценкам")
print(f"Среднее значение: {mean_val:.2f}")
print(f"Медиана: {median_val}")
print(f"Стандартное отклонение: {std_val:.2f}")
print(f"Дисперсия: {var_val:.2f}")
print(f"Максимум: {max_val}")
print(f"Минимум: {min_val}")
print(f"Размах: {range_val}")

percentiles = np.percentile(data_grades, [25, 50, 75, 90, 99])
print(f"Перцентили (25, 50, 75, 90, 99): {percentiles}")

q1 = np.percentile(data_grades, 25)
q3 = np.percentile(data_grades, 75)
iqr = q3 - q1

print(f"Первый квартиль (Q1): {q1}")
print(f"Третий квартиль (Q3): {q3}")
print(f"Межквартильный размах (IQR): {iqr}")

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = data_grades[(data_grades < lower_bound) | (data_grades > upper_bound)]

print(f"Границы выбросов: [{lower_bound}, {upper_bound}]")
print(f"Найденные выбросы: {outliers}")

count_60_80 = np.sum((data_grades >= 60) & (data_grades <= 80))
print(f"\nКоличество студентов с оценками от 60 до 80 включительно: {count_60_80}")
print("Нули — это пропуски экзамена, их следует удалить или заменить на медиану.")

A = np.array([68, 72, 55, 80, 91, 64, 77, 83, 59, 70, 88, 62, 75, 95, 60])

matrix = A.reshape(3, 5)
print("\n Задание 2: Работа с матрицей A")
print("Матрица 3x5:\n", matrix)
print("Размерность (shape):", matrix.shape)
print("Количество элементов:", matrix.size)

sum_rows = np.sum(matrix, axis=1)
sum_cols = np.sum(matrix, axis=0)
print("Сумма по строкам:", sum_rows)
print("Сумма по столбцам:", sum_cols)

transposed = matrix.T
print("Транспонированная матрица:\n", transposed)

print("\nСтатистика по всей матрице:")
print(f"Среднее: {np.mean(matrix):.2f}")
print(f"Стандартное отклонение: {np.std(matrix):.2f}")
print(f"Дисперсия: {np.var(matrix):.2f}")

matrix_q1 = np.percentile(matrix, 25)
matrix_q2 = np.percentile(matrix, 50)
matrix_q3 = np.percentile(matrix, 75)

print(f"Q1 (25%): {matrix_q1}")
print(f"Q2 (50%): {matrix_q2}")
print(f"Q3 (75%): {matrix_q3}")