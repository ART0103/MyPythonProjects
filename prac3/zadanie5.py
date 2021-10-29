# Необходимо найти два максимальных элемента массива без использования встроенной функции max
# Дополнение: Выполнить задачу за один проход по массиву
print('Введите произвольные отрицательные и положительные числа:')
array = list(map(int, input().split()))
max1 = array[0]
max2 = array[1]
for i in range(len(array)):
    if array[i] > max1:
        max1, max2 = array[i], max1
    elif (array[i] > max2) and (array[i] != max1):
        max2 = array[i]
print('Максимальные элементы массива:', max1, max2)
