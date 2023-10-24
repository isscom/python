# МНОЖЕСТВА
# множестве содержит в себе уникальные элементы (тип - set (type))

colors = {'red', 'green', 'blue'}
print(type(colors)) # тип данных set

colors.add('gray') # добавление элемента в множество
print(colors)

colors.remove('red') # удаление элемента из множества (если элемента нет - ошибка)
print(colors)

colors.discard('red') # удаление, если есть (без ошибки)

colors.clear() # очистка множества

#ЕЩЕ ПРИМЕР

a = {1,2,3,5,8}
b = {2,5,8,13,21}
c = a.copy() #c = {1,2,3,5,8}
u = a.union(b) #u = {1,2,3,5,8,13,21} объединение множеств (исключая дубли)
i = a.intersection(b) #i = {8,2,5} персечение
dl = a.difference(b) #dl = {1,3}
dr = b.difference(a) #dr = {13,21}

s = frozenset(a) # неизменяемое (замороженное) множество