# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

list_input = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# min_number = int(input('min_number: '))
# max_number = int(input('max_number: '))
min_number, max_number = map(int, input('Задайте диапазон через пробел:\n').split())
print('Ввод:', list_input, '\nВывод:', end = " ")

# for i in range(len(list_input)):
#     if min_number <= list_input[i] <= max_number:
#         print(i, end = " ")
print([i for i in range(len(list_input)) if min_number <= list_input[i] <= max_number]) # тоже самое, что и выше, только через генератор списков