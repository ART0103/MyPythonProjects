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