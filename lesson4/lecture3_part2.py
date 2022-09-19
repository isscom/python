def f(x):
    return x**2

list = [(i, f(i)) for i in range(1,21) if i % 2 == 0]
print(list)