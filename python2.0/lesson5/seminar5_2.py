# a, b = map(int, input().split()) # функция map принимает какой-то список и принимает функцию
# получается, что к каждому вводимому input() числу, который входит к список split() - мы применяем функцию int (из строки в число)
# функция map отличается от функции filter тем, что map применяет функцию ко всем элементам, а filter фильтрует список по условию

# a, b = map(lambda x: int(x), input().split())
# lambda ф-ия: указываем что принимает (x) и что возвращает (int(x))

# array = [int(i) for i in input().split()]
# проходим по списку введенных значений (через пробел = split()) и переводим в число

# # enumerate
# array_2 = [-10, -20, -30, -40, -50]
# for i in enumerate(array_2):
#     print(i)
# # содали кортежи и пронумеровали элементы
# # (0, -10)
# # (1, -20)
# # (2, -30)
# # (3, -40)
# # (4, -50)

# # либо:
# print(tuple(enumerate(array_2)))
# # ((0, -10), (1, -20), (2, -30), (3, -40), (4, -50))