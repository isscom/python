# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X

n = int(input('N: '))
a = [i for i in range(1, n+1)]
element_result = a[0]
print(a)
x = int(input('Х: '))
for element in a:
    if abs(element - x) < abs(element_result - x):
        element_result = element
print(f'-> {element_result}')