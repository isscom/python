# data = input() #принимается строка или число?
# print(type(data)) #class 'str' (т.е. строка)

# data = input("Введите числа: ") #это строковый тип данных всё равно
# print(data)
#строка с введенными числами

# data = input("Введите числа: ").split() #функция сплит разделяет строку по разделителю, который указан внутри круглых скобок (если пусто, то 1 знак пробела)
# print(data)
# #['число', 'число' и т.д.] - получился список, который состоит из строк

# data = input("Input: ").split()
# for i in data:
#     print(i)
# #введенные числа выводятся с новой строки, но по-прежнему в виде строки

# data = input("Input: ").split()
# for i in data:
#     print(int(i) - 1)
# #введенные данные выводятся с новой строки, но теперь мы их циклом переводим в числа
# #видим, что вычитаемая 1 вычитается, т.к. это числа

#ЕСТЬ СОКРАЩЕННАЯ ЗАПИСЬ, КОТОРАЯ ПОЗВОЛЯЕТ РАБОТАТЬ НАМНОГО УДОБНЕЕ

#1. data = [input("Input: ").split()] #указываем, что мы в нём сохраняем (в list comprehentions)
#2. сохранять мы будем i => data = [int(i) for i in input("Input: ").split()] по списку строк

#################################################
#в переменную сохраняем число(!) элемент, каждый элемент из введенной строки с разделением пробелом (split)
# data = [int(i) for i in input("Input: ").split()]
# print(data)
#выводится список чисел
# Input: 10 20 30 40 50
# [10, 20, 30, 40, 50]
#################################################

# set_test = {8, 10, 16, 23}
# set_test.add(42)
# print(*set_test)