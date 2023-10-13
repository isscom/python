# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# 2 2
# 4

def rec_sumAB(a, b):
    if b == 0:
        return a
    return 1 + rec_sumAB(a, b - 1)

# x = int(input('A: '))
# y = int(input('B: '))

# x, y = map(int, input('Введите два числа через пробел:\n').split())

# x, y = map(lambda x: int(x), input('Введите два числа через пробел:\n').split())

# array = [int(i) for i in input(f'Введите числа через пробел:\n').split()]
array = [int(input(f'{i+1}/{2} число: ')) for i in range(2)]
x = array[0]
y = array[1]

print('\n', x, y, '\n', rec_sumAB(x, y))