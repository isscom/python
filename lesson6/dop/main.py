# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
# пример - 8 11 0 -23 140 1 => 11 -23
lst = [8, 11, 0, -23, 140, 1]
print(f'{lst} => {list(filter(lambda x: 9<abs(x)<100,lst))}')

# 2. Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')
lst = ['a', 'b', '2', '3' ,'c']
numbr = list(filter(lambda x: x.isdigit(), lst))
word = list(filter(lambda x: x.isalpha(), lst))
print(f'a = {lst}')
print(f'b = {word}')
print(f'c = {numbr}')

# 3. Преобразовать набора списков
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор

# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]

# и потом вернуть в исходное состояние

# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

a,b,c = map(list,zip(users,ids,salary))
print(a,b,c, sep="\n")
a,b,c = map(list,zip(a,b,c))

print(a,b,c, sep="\n")