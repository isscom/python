# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

import sum_num as sn
float_number = str(input('Введите вещественное число: '))
print(f'{float_number} -> {sn.sum_num(float_number)}')