# Расположить столбцы матрицы D[M, N] в порядке возрастания элементов k-й строки (1 <= k <= М).
import numpy as np


def print_matrix(arr_2d):
    for arr25 in arr_2d:
        for el in arr25:
            print(el, end=' ')
        print()


def mirror_matrix(arr_3d) -> object:
    rows_cnt = len(arr_3d)
    cols_cnt = len(arr_3d[0])

    new_matrix = [[0] * rows_cnt for _ in range(cols_cnt)]

    for i in range(rows_cnt):
        for j in range(cols_cnt):
            new_matrix[j][i] = arr_3d[i][j]
    return new_matrix


def selection_sort(arr24):
    tmp = arr24[:]
    for i in range(len(tmp)):
        minimum = i

        for j in range(i + 1, len(tmp)):
            # Выбор наименьшего значения
            if tmp[j] < tmp[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        tmp[minimum], tmp[i] = tmp[i], tmp[minimum]

    return tmp


a = 0
k = 0
j = 1
m = int(input('Введите количество строк в матрице:'))
n = int(input('Введите количество столбцов в матрице:'))
D = np.zeros((m, n))
tnp = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        a = int(input("Введите число:"))
        D[i,j] = a
        tnp[i,j] = a
print('Полученная матрица:')
print_matrix(D)
k = int(input("введите номер строки, элементы которой нужно расположить в порядке возрастания:"))
ind = []
arr = tnp[k - 1]
arr2 = selection_sort(D[k - 1])
print('arr=', arr)
print('arr2=', arr2)
for i in range(len(arr)):
    for j in range(len(arr2)):
        if arr[i] == arr2[j]:
            ind.append(j)
            break
print("ind=", ind)
rev = mirror_matrix(tnp)
print_matrix(rev)
t = []
for i in range(n):
    t.append(rev[ind[i]])
B = mirror_matrix(t)
print_matrix(B)
# for i in range(n):
#     c = t[i]
#     t[i] = t[ind[i]]
#     t[ind[i]] = c
# print_matrix(t)
# for i in range(m):
#     for j in range(n - 1):
#         while all(arr) != all(arr2):
#             D[i, j] = D[i, j + 1]
#             arr = D[k - 1]
# print_matrix(D)
