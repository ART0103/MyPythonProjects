# Найти максимальный среди всех элементов тех строк заданной матрицы,
# которые упорядочены (либо по возрастанию, либо по убыванию).
import numpy as np

с = 0
pr = False
p = int(input('Введите количество строк в матрице:'))
h = int(input('Введите количество столбцов в матрице:'))
a = np.zeros((p, h))
maxim = a[0, 0]
for i in range(p):
    for j in range(h):
        a[i, j] = int(input("Введите число:"))
print('Полученная матрица:')
print(a)
for i in range(p):
    for j in range(h - 1):
        if a[i, j] <= a[i, j + 1]:
            pr = True
            if pr == True:
                if (a[i, j] > maxim):
                    maxim = a[i, j]
        else:
            pr = False
            maxim = 0
if maxim == 0:
    print('Упорядоченных строк не найдено')
else:
    print('Наибольшее значение:', maxim)
