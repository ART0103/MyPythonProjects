# Расположить столбцы матрицы D[M, N] в порядке возрастания элементов k-й строки (1 <= k <= М).
import numpy as np


def print_matrix(arr_2d):
    for arr in arr_2d:
        for el in arr:
            print(el, end=' ')
        print()


def mirror_matrix(arr_2d):
    rows_cnt = len(D)
    cols_cnt = len(D[0])

    new_matrix = [[0] * rows_cnt for _ in range(cols_cnt)]

    for i in range(rows_cnt):
        for j in range(cols_cnt):
            new_matrix[j][i] = D[i][j]
    return new_matrix


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] < arr[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr

a = []
k = 0
j = 1
m = int(input('Введите количество строк в матрице:'))
n = int(input('Введите количество столбцов в матрице:'))
D = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        D[i, j] = int(input("Введите число:"))
print('Полученная матрица:')
print_matrix(D)
k = int(input("введите номер строки, элементы которой нужно расположить в порядке возрастания:"))
arr = D[k-1]
arr2 = selection_sort(arr)
for i in range(arr2):

