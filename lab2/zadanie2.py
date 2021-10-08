# Расположить столбцы матрицы D[M, N] в порядке возрастания элементов k-й строки (1 <= k <= М).
import numpy as np


def print_matrix(arr_2d):
    for arr in arr_2d:
        for el in arr:
            print(el, end=' ')
        print()


pr = False
k = 0
j = 1
pr = False
m = int(input('Введите количество строк в матрице:'))
n = int(input('Введите количество столбцов в матрице:'))
D = np.zeros((m, n))
maxim = 0
for i in range(m):
    for j in range(n):
        D[i, j] = int(input("Введите число:"))
print('Полученная матрица:')
print_matrix(D)
k = int(input("введите номер строки, элементы которой нужно расположить в порядке возрастания:"))
if (1 <= k) and (k <= m):
    pr = True
if pr:
    rows_cnt = len(D)
    cols_cnt = len(D[0])

    new_matix = [[0] * rows_cnt for _ in range(cols_cnt)]

    for i in range(rows_cnt):
        for j in range(cols_cnt):
            new_matix[j][i] = D[i][j]
