# Найти максимальный среди всех элементов тех строк заданной матрицы,
# которые упорядочены (либо по возрастанию, либо по убыванию).
def print_matrix(arr_2d):
    for arr in arr_2d:
        for el in arr:
            print(el, end=' ')
        print()


matrix = []
need_stop = False

while not need_stop:
    s = input()
    if s != '':
        split = s.split(' ')
        tmp = []
        for j in split:
            tmp.append(int(j))
        matrix.append(tmp)
    else:
        need_stop = True

print('Полученная матрица:')
print_matrix(matrix)
sorted_matrix = []

for i in range(len(matrix)):
    for j in range(len(matrix[0]) - 1):
        if matrix[i][j] < matrix[i][j + 1]:
            if j == (len(matrix[0]) - 2):
                sorted_matrix.append(matrix[i])
        else:
            break

for i in range(len(matrix)):
    for j in range(len(matrix[0]) - 1):
        if matrix[i][j] > matrix[i][j + 1]:
            if j == (len(matrix[0]) - 2):
                sorted_matrix.append(matrix[i])
        else:
            break
maximum = -99999
for i in range(len(sorted_matrix)):
    for j in range(len(sorted_matrix[0])):
        if sorted_matrix[i][j] > maximum:
            maximum = sorted_matrix[i][j]
print('Максимальное значение: ', maximum)
