# НегаФибоначчи
# Задайте число. Составьте список чисел Фибоначи, в том числе для отрицательных индексов.

nega_fib_1 = list()
a0 = 0
a1 = 1
n = int(input(''))
for i in range(n + 1):
    nega_fib_1.append(a0)
    x = a0 + a1
    a0 = a1
    a1 = x
nega_fib_2 = [nega_fib_1[i] * (-1) ** (i + 1) for i in range(0, len(nega_fib_1))][::-1]

print(nega_fib_2 + nega_fib_1[1:])
#                          кроме 1-го элемента