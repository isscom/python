# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

# РЕШЕНИЕ 1
# input_string = [i for i in input("Input: ").split()] # генератором списков задаем список (строку)
# output_string = set(input_string)
# for i in output_string:
#     count = 0
#     for j in range(len(input_string)):
#         if i == input_string[j]:
#             if count > 0: input_string[j] = f'{input_string[j]}_{count}'
#             count += 1
# print('Output:', end = " ")
# print(*input_string)
##################################################

#РЕШЕНИЕ 2 (со словарём)
input_string = [i for i in input("Input: ").split()] # вводим строку и создаём из нее список
print('Output:', end = " ") # end = " " это в конце принта - не переход на новую строку, а просто пробел (то что в кавычках)
letters = {} # создаем словарь
for i in input_string: # проходим по списку
    if i in letters.keys(): # сравниваем каждый элемент с ключами
        print(i + "_" + str(letters[i]), end = " ") # если ключ есть - добавляем ключ + нижнее подчеркивание + номер (сколько раз оно встретилось на текущий момент)
        letters[i] += 1 # увеличиваем кол-во раз на единицу
    else:
        print(i, end = " ") # если ключа не нашлось, то просто выводим букву ниже
        letters[i] = 1
##################################################

# # РЕШЕНИЕ 3
# input_string = input("Input: ").split(' ') # ввод строки (input) и разбиваем строку в список (split) по разделителю пробел (' ')
# output_string = ''.strip() # задаём строку, которая будет результирующей, а strip() это что?
# for i in input_string:
#     c = output_string.count(i)
#     if output_string.count(i) == 0:
#         output_string += i + ' '
#     else:
#         output_string += i + '_' + str(c) + ' '
# print(f'Output: {output_string}')
##################################################