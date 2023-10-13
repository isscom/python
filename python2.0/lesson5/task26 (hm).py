# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def rec_ApowB(a, b):
    if b == 0:
        return 1
    return a * rec_ApowB(a, b - 1)

# A = int(input('A: '))
# B = int(input('B: '))

# A, B = map(int, input('Введите два числа через пробел:\n').split())

# A, B = map(lambda x: int(x), input('Введите два числа через пробел:\n').split())

# array = [int(i) for i in input(f'Введите числа через пробел:\n').split()]

array = [int(input(f'{i+1}/{2} число: ')) for i in range(2)]

print(f'A = {array[0]}; B = {array[1]} -> {rec_ApowB(array[0], array[1])}')