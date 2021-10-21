# Для целочисленной квадратной матрицы найти число элементов, кратных k, и наибольший из этих элементов.
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

k = int(input('Введите число для определения нужных элементов: '))
sorted_matrix = []
counter = 0

if len(matrix) == len(matrix[0]):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] % k == 0:
                counter += 1
                sorted_matrix.append(matrix[i][j])

maxim = sorted_matrix[0]
for i in range(len(sorted_matrix)):
    maxim = sorted_matrix[i] if sorted_matrix[i] > maxim else maxim
print('Наибольшее значение:', maxim, 'Число элементов кратных k:', counter)
