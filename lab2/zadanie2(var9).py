# В данной действительной квадратной матрице порядка n найти наибольший по модулю элемент.
# Получить квадратную матрицу порядка n — 1 путем отбрасывания из исходной матрицы строки и столбца, на пересечении
# которых расположен элемент с найденным значением.
matrix = []
need_stop = False

while not need_stop:
    s = input()
    if s != '':
        split = s.split(' ')
        tmp = []
        for j in split:
            tmp.append(float(j))
        matrix.append(tmp)
    else:
        need_stop = True

maxim = matrix[0][0]
column = 0
row = 0

if len(matrix) == len(matrix[0]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if abs(matrix[i][j]) > maxim:
                maxim = abs(matrix[i][j])
                row = i
                column = j
    for i in range(len(matrix)):
        del matrix[i][column]
    del matrix[row]
print(matrix)