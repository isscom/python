# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.

# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.

# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4 (значения сгенерированы случайным образом)
# 9

import random
N = int(input('Кол-во кустов: '))
a = list(random.randint(0, 10) for i in range(N)) # list comprehension: добавляем рандомное значение (урожайность) в каждый i элемент размером N (в каждый куст)
max_n = []
i = 0
sum = 0

print(f'{N} -> ', end = " ")
print(*a) # список с кол-вом ягод на каждом кусте

while i < N:
    if i == N - 1:
        sum = a[i] + a[i - 1] + a[0]
    else:
        sum = a[i] + a[i - 1] + a[i + 1]
        max_n.append(sum)
        max_n.sort()
    i += 1

print(max_n[-1])