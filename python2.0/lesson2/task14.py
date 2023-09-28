# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Введите число N: '))
output_list_num = []
num = 2
for i in range(n):
    if num ** i <= n:
        output_list_num.append(num ** i)
    else:
        break
output_str_num = [str(s) for s in output_list_num]
print()
print(f'{n} -> {" ".join(output_str_num)}')