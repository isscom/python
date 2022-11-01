# 1. НОД двух чисел
a = 12
b = 16
if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b

print(a)

# 2. Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr".
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.
contains = lambda s, sample='plr': sample in s
s = input()
print(contains(s))


# 3. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
with open('text.txt', 'r') as n:
    lst = [int(i) for i in n.readline().split()]
    for i in range(1,len(lst)):
        if lst[i] - lst[i-1] > 1:
            print(lst[i] - 1)



def find_num(lst):
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] > 1:
            return i, lst[i] - 1
    return -1, -1

with open("data.txt", "r") as fin:
    lst = [int(i) for i in fin.readline().split()]
    print(lst)
    pos, num = find_num(lst)
    print(pos,num)
    if (pos != -1):
        lst.insert(pos, num)
    print(lst)