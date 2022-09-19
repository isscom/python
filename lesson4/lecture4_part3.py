def f(x):
    return x**2

data = [1, 2, 3, 5, 8, 15, 23, 38]
# data = open('file2.txt', 'r')
list = [(i, f(i)) for i in data if i % 2 == 0]
print(data)
print(list)
# data.close()