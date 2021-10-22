# Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел).
# Необходимо выбрать и отобразить на экране числа, присутствующие и в первом и во втором списках.
# Результат выведите на экран в виде строки чисел, записанных через пробел.Задачу решить с использованием множеств.
need_stop = False

final_set = set()
set1 = set()
set2 = set()

for i in range(2):
    s = input()
    if s != '':
        split = s.split(' ')
        if i == 1:
            for j in split:
                set1.add(int(j))
        else:
            for j in split:
                set2.add(int(j))
final_set = set1 | set2
print(' '.join(map(str, final_set)))

