# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Решение_1:
def print_operation_table_1(operation, num_rows=6, num_columns=6):
    result = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in result:
        print(*[x for x in i])

# Решение_2:
def print_operation_table_2(operation, num_rows=6, num_columns=6):
    print('\t'.join([str(i) for i in range(1, num_columns + 1)]))
    for i in range(2, num_rows + 1):
        print(i, end = '\t') # \t - чтобы значения вывозились через табуляцию, т.е. друг под другом
        for j in range(2, num_columns + 1):
            print(operation(i, j), end = '\t')
        print()

# Ввод:
print_operation_table_2(lambda x, y: x * y)

# Вывод:
# 1  2  3  4  5  6
# 2  4  6  8 10 12
# 3  6  9 12 15 18
# 4  8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36 

# ПРИМЕЧАНИЕ:
# .split() <-> .join() - две взаимно-обратные функции
# .split() - принимает строку и работает со строкой (разделяет строку по разделителю/символу) => список строк
# .join() - полностью обратная - возвращает строку из списка строк (принимает список строк и соединяет все элементы через указанных соединитель)