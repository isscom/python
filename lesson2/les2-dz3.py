# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# ВАРИАНТ 1
n = int(input('N = '))
sum = 0
for i in range(1, n+1):
    sum = sum+round((1+1/n)**n, 2)
print(round(sum))

# ВАРИАНТ 2
n = int(input('N =  '))

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

print(sequence(n))
print(f'Сумма последовательности =', round(sum(sequence(n))))