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

