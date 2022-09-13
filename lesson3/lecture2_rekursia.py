# РЕКУРСИЯ (функция, вызывающая сама себя)
# главное - указать в какой момент нужно остановиться и перестать себя вызывать

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1,10):
    list.append(fib(e))

print(list)

# КОРТЕЖИ (неизменяемый список)

a, b = 3, 4 # это обычное множественное присваивание (a = 3, b = 4)
a = (3, 4) # это кортеж (может состоять из любого кол-ва элементов - координат, главное - не ОДИН! (либо поставить запятую - это будет кортеж 1 элемента))
print(a)
# можно обращаться к конкретному элементу:
print(a[0]) #3
print(a[-1]) #4

a[0] = 12 # для кортежей присваивание значений элементу - не работает, это неизменяемый список

# можно список превратить в кортеж, можно кортеж в список

# КОРТЕЖИ можно перебирать при помощи циклов

k = (4,7,4,3,2)

for item in k:
    print(item)

# Можно распаковать кортеж в отдельные переменные:

t = tuple(['red', 'green', 'blue']) # переменная была определена на основе списка
red, green, blue = t # операция двойного преобразования: 38 строка: создает список, конвертируем его в кортеж, 39 строка: кортеж распаковываем и превращаем его в 3 независимые переменные
print('r:{} g:{} b:{}'.format(red,green,blue))
