# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5 - (число N)
# 1 2 3 4 5 - (массив А)
# 3 - (число Х)
# -> 1 (раз)

n = int(input('N: '))
a = [i for i in range(1, n+1)]
print(a)
x = int(input('Х: '))
print(f'-> {sum([1 for element in a if element == x])}')