#Списки
ran = range(1, 6) #задали range (еще не явл. списком)
print(type(ran)) #тип range

numbers = list(ran) #приводим тип range к типу list
print(type(numbers)) #тип list - это уже список

print(numbers)

for i in numbers:
    i *= 2
    print(i)

colors = ['red', 'green', 'blue']

for e in colors:
    print(e) #red green blue

for e in colors:
    print(e*2) #redred greengreen blueblue

colors.append('gray') #добавить в конец

colors.remove('red') #del colors[0] #удалить элемент

#Функции
def f(x): # def название функции(аргумент)
    if x == 1: #тело функции, какие-то действия
        return 'Целое'
    elif x == 2.3:
        return '23'
    else:
        return

argument = 1
print(f(argument))