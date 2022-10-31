# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3] # задаем список
print(sum(my_list[1::2])) # печатаем сумму списка начиная с индекса 1 с шагом 2


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list2 = [2, 3, 5, 6]
i = 0
m = 1
while i < ((len(my_list2) / 2)):
    result = my_list2[i] * my_list2[(len(my_list2) - m)]
    print(result,end=' ')
    i += 1
    m += 1

my_list3 = [2, 3, 4, 5, 6]
result_list = []
for i in range((len(my_list3) + 1) // 2): # делаем деление в целых числах на 2
    result_list.append(my_list3[i] * my_list3[len(my_list3) - 1 - i]) # добавляем в список произведение i числа и зеркального с конца
print(result_list)


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math
list1 = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []
for i in range(len(list1)):
    a = round(list1[i]*10 % 10, 2)
    if a > 0:
        list2.append(a)
b = round(float((max(list2)-min(list2))*10/100), 2)
print(b) # 0.19

from unittest import result
my_list = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in my_list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)
print('%.2f' % (max-min)) # 0.20


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

N = int(input('Введите число в десятичной СИ: '))
D = ''
while N > 0:
    D = str(N%2) + D
    N = N // 2
print(D)


a=int(input('Введите число: '))
b=bin(a)
print(b[2:])


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

a = int(input('Enter the number: '))
print(a)
negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,a):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list_nego = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list_nego)

negofibonacci.reverse()
negofibonacci.append(0)

print(f' for a = {a} =>{negofibonacci+fibonacci}')