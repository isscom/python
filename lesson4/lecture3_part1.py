
# Описание функции
def sum(x,y):
    return x + y

# Лямбда
sum = lambda x, y: x + y

# Тот же самый результат получается, т.е. описание фукнции = лямбда


# Можно избежать присваивание переменной

def calc(op, a, b):
    print(op(a, b))

calc(lambda x, y: x * y, 5, 6)