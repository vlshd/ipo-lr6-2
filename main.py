import random

height = random.randint(4, 8) # создает случайное количество столбцов
width = random.randint(4, 8) # создает случайно количество строк
values = [-3, -5, -2, -12, 0, 15, 4, 7, 2] # значения в матрице

matrix = [[random.choice(values) for _ in range(width)] for _ in range(height)] # создание матрицы

for i in matrix:
    print(' '.join(map(str, i))) # вывод матрицы преобразовывая i в строки, и затем в одну строку через пробел

sum3 = sum(value for row in matrix for value in row if value % 3 == 0) # сумма элементов кратных 3
print("Сумма всех элементов, кратных 3:", sum3) # вывод