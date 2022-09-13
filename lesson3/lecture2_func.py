# ФУНКЦИИ И МОДУЛИ
# Чтобы не было 1000+ строк кода, мы можем определить некоторое кол-во файлов, куда будем складывать функционал (функции хранить)
# и далее из 1 файла использовать функционал другого

import lecture1_part2

print(lecture1_part2.f(1))

# или

import lecture1_part2 as h # создаём аллиас

print(h.f(1))

# таким образом можно разделять свою программу на некоторое кол-во файлов

def new_string(symbol, count):
    return symmol * count
print(new_string('!',5)) #!!!!!
print(new_string('!',)) #Type Error

# можно count задать сразу

def new2_string(symbol, count = 3):
    return symbol * count
print(new2_string('!')) #!!!
print(new2_string(4)) #12 (3*4)

# у функции можно указать любое кол-во аргументов. Для этого перед указанием аргументов ставим *

def concatenatio(*params):
    res: str = '' # тип данных стринг явно прописывается таким образом (для работы с int указание типа не обязательно)
    for item in params:
        res += item
    return res

print(concatenatio('a','q','gg')) #aqgg