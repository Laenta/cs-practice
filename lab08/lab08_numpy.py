import numpy as np

# === Задание 1. Создание векторов и матриц ===
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("=== Задание 1. Создание векторов и матриц ===")
print("Массив hours:", hours)
print("Форма массива hours:", hours.shape)
print("Количество измерений:", hours.ndim)
print("Общее количество элементов:", hours.size)
print("Тип данных элементов:", hours.dtype)

print("\nМассив line:", line)
print("Массив zeros:", zeros)
print("Матрица unknown_table:\n", unknown_table)
print("Единичная матрица identity:\n", identity)


# === Задание 2. Индексы и срезы в векторе ===
print("\n=== Задание 2. Индексы и срезы в векторе ===")
print("Третий элемент массива:", hours.item(2))
print("Последний элемент массива:", hours[-1])
print("Элементы с индексами со второго по пятый:", hours[2:6])
print("Каждый второй элемент массива:", hours[::2])
print("Массив в обратном порядке:", hours[::-1])


# === Задание 3. Строки и столбцы таблицы ===
temperatures = np.array((
    (12, 14, 13, 15),
    (11, 13, 16, 17),
    (10, 12, 15, 18),
))

print("\n=== Задание 3. Строки и столбцы таблицы ===")
print("Форма таблицы:", temperatures.shape)
print("Количество измерений:", temperatures.ndim)
print("Количество элементов:", temperatures.size)
print("Значение из второй строки и третьего столбца:", temperatures.item(1, 2))
print("Первая строка таблицы:", temperatures[0, :])
print("Последний столбец таблицы:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент размером 2 на 2:\n", temperatures[0:2, 1:3])


# === Задание 4. Прямоугольные срезы ===
matrix = np.arange(1, 26).reshape(5, 5)

print("\n=== Задание 4. Прямоугольные срезы ===")
first_three_rows = matrix[:3, :]
print("Первые три строки:\n", first_three_rows)
print("Форма фрагмента:", first_three_rows.shape)

last_two_rows = matrix[-2:, :]
print("\nПоследние две строки:\n", last_two_rows)
print("Форма фрагмента:", last_two_rows.shape)

first_two_cols = matrix[:, :2]
print("\nПервые два столбца:\n", first_two_cols)
print("Форма фрагмента:", first_two_cols.shape)

middle_block = matrix[1:4, 2:5]
print("\nСтроки с индексами 1–3 и столбцы 2–4:\n", middle_block)
print("Форма фрагмента:", middle_block.shape)

bottom_right_corner = matrix[-2:, -2:]
print("\nУгловой блок 2 на 2 в правом нижнем углу:\n", bottom_right_corner)
print("Форма фрагмента:", bottom_right_corner.shape)


# === Задание 5. Изменение массива с помощью срезов ===
print("\n=== Задание 5. Изменение массива с помощью срезов ===")
vector = np.arange(10, 60, 10)
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

# Метод .copy() нужен для создания независимой копии массива в памяти.
# При обычном присваивании новая переменная ссылается на те же данные,
# поэтому любые изменения в ней испортили бы исходный массив hours.
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1

print("Изменённый массив changed_hours:", changed_hours)
print("Исходный массив hours:", hours)

changed_matrix = matrix.copy()
changed_matrix