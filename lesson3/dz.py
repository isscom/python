# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

numbers = [2,3,5,9,3]
print(f'{numbers} -> на нечётных позициях элементы {numbers[1::2]}, ответ: {sum(numbers[1::2])}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers = [2,3,4,5,6]
result = []
for i in range((len(numbers)+1)//2):
    result.append(numbers[i]*numbers[len(numbers)-1-i])
print(f'{numbers} => {result}')


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in numbers:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)
print(f'{numbers} => {round((max-min),3)}')

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число в десятичной системе исчисления: '))
number = n
result = ''
while number > 0:
    result = str(number % 2) + result
    number = number // 2
print(f'{n} -> {result}')


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
user_number = int(input('Задайте число: '))
for e in range(1, user_number + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(f'Для k = {user_number} список будет выглядеть так: {list}')