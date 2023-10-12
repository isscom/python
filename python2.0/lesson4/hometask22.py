# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Кол-во элементов 1 набора: '))
m = int(input('Кол-во элементов 2 набора: '))

# n, m = [int(i) for i in input(f'Кол-во элементов {i+1} набора: ').split()] пока не получается

lot_1 = [int(input(f'{element_lot_1+1}/{n} элемент 1 набора: ')) for element_lot_1 in range(n)]
# for element_lot_1 in range(n):
#     lot_1.append(int(input(f'{element_lot_1+1}/{n} элемент 1 набора: ')))

lot_2 = [int(input(f'{element_lot_2+1}/{m} элемент 2 набора: ')) for element_lot_2 in range(m)]
# for element_lot_2 in range(m):
#     lot_2.append(int(input(f'{element_lot_2+1}/{m} элемент 2 набора: ')))

# if n > m:
#     result = [element_lot_1 for element_lot_1 in lot_1 if element_lot_1 in lot_2] - действие 1 (добавляем элементы из lot_1 если они есть в lot_2)
# # for element_lot_1 in lot_1: # цикл for расписан выше через list comprehension
# #     if element_lot_1 in lot_2:
# #         result.append(element_lot_1)
# else:
#     result = [element_lot_2 for element_lot_2 in lot_2 if element_lot_2 in lot_1] - действие 2 (добавляем элементы из lot_2 если они есть в lot_1)
# # for element_lot_2 in lot_2: # цикл for расписан выше через list comprehension
# #     if element_lot_2 in lot_1:
# #         result.append(element_lot_2)

result = sorted(set([element_lot_1 for element_lot_1 in lot_1 if element_lot_1 in lot_2] + [element_lot_2 for element_lot_2 in lot_2 if element_lot_2 in lot_1]))
#                          действие 1                                                                  действие 2

# print(result) # для проверки [6, 12, 6]
# result = sorted(set(result))

print("\n", n, m,"\n", *lot_1,"\n", *lot_2,"\n", *result)