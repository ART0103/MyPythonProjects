# Дан одномерный массив числовых значений, насчитывающий N элементов. Подсчитать количество чисел, делящихся на 3
# нацело, и среднее арифметическое чисел с чётными значениями. Поставить полученные величины на первое и последнее
# места в массиве (увеличив массив на 2 элемента).
r = 0
t = 0
m = 0
n = 0
print('Введите произвольные числа:')
a = list(map(int, input().split()))
for i in range(len(a)):
    if (a[i] % 3) == 0:
        t += 1
    if (a[i] % 2) != 0:
        continue
    m += 1
    n = n + a[i]
if m > 0:
    r = n / m
a.append(r)
a.reverse()
a.append(t)
a.reverse()
print('Итоговый резуьтат:', a)
