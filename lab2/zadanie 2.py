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

k1 = int(input('Введите значение k:'))
k = k1 - 1
a = []
for num in matrix[k]:
    a.append(num)

for i in range(len(matrix[0]) - 1):
    for j in range(len(matrix[0]) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            for m in range(len(matrix)):
                matrix[m][j], matrix[m][j+1] = matrix[m][j+1], matrix[m][j]
for i in matrix:
    print(*i)