# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# ВАРИАНТ 1
float_num = input('input float number: ')
print(type(float_num))
sum = 0
for i in float_num:
    if i != '.' and i != '-':
        sum += int(i)
print(f'{float_num} -> {sum}')


# ВАРИАНТ 2
numb = float(input())
summ = 0
if numb < 0:
    numb = -1 * numb
else: numb = numb

for el in str(numb):
        if el != '.':
            summ += int(el)
print(summ)

# ВАРИАНТ 3
n = float(input('Введите число - '))
if n < 0:
    n = -1 * n
else:
    while n % 1 > 0:
        n *= 10
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
print(int(summ))

# ВАРИАНТ 4
s = str(input('Введите число: '))
summ = 0
for i in s:
    if i.isdigit(): #берем только числа (без всего остального)
        summ += int(i)
print(summ)