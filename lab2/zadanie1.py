# Найти максимальный среди всех элементов тех строк заданной матрицы,
# которые упорядочены (либо по возрастанию, либо по убыванию).
import numpy as np


def print_matrix(arr_2d):
    for arr in arr_2d:
        for el in arr:
            print(el, end=' ')
        print()


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
print_matrix(a)
for i in range(p):
    for j in range(h - 1):
        if a[i, j] <= a[i, j + 1]:
            pr = True
        else:
            pr = False
        if pr:
            if a[i, j] <= maxim:
                continue
            maxim = a[i, j]
        else:
            pr = False
            maxim = 0
            continue
if maxim == 0:
    print('Упорядоченных строк не найдено')
else:
    print('Наибольшее значение:', maxim)
