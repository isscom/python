# 35. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i - 1].
# Найдите это число.

# Input: [1, 2, 3, 4, 5, 7, 8, 9, 10]
# Output: 6

# функция, кот. будет искать потерянное число
def search_number(arr):
    for i in range(1, len(arr)):
        if arr[i] - 1 != arr[i - 1]:
            return i + 1
    return 'Последовательность верна'

with open('1.txt', 'r', encoding='utf-8') as file: # открываем файл (r-чтение) и называем это переменной
    # print(file.read()) # выводится строка
    # print(file.read().split()) # выводится список
    # ['1', '2', '3', '4', '5', '7', '8', '9', '10']
    lot = [int(i) for i in file.read().split()] # закинули в список генератором списков
    # print(lot)
    # [1, 2, 3, 4, 5, 7, 8, 9, 10]
    print('Input:', *lot)
    # далее вызываем функцию поиска потерянного числа:
    print(f'Output: {search_number(lot)}') # выведем потерянное число на экран

    # r  - чтение файла
    # w  - удаление предыдущего содержимого и запись нового
    # a  - добавление нового содержимого в конец
    # a+ - позволяет создать файл, если его вообще не было