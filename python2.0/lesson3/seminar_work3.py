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

#[] - список

###################################################
#ВЛОЖЕННОСТЬ СПИСКА В СПИСОК
# data = [[1, -1.575], ['Hello', True], [15, -7]]
#           0              1              2
# Внутри списка есть три списка
# Чтобы получить число 15 (2 список, первый элемент)
# print(data[2][0])

###################################################
# СЛОВАРИ
# data = {"Ivan": 27, "Alex": 36, "Kosta": {'age': 21, 'hobby': ['tennis', 'football']}}
# #key: value (внутри словаря - пара (ключ и значение). Одинаковых ключей не может быть)
# #для того, чтобы вывести слово tennis на экран:
# print(data["Kosta"]['hobby'][0]) #обращаемся к вложенному словарю Костя, затем к вложенному списку под ключом Хобби, нам нужно 0 индекс (первый элемент)
# #Внутри словарей - обращаемся к ключам, а не индексам
# # .values() возвращает объект своего списка
# # .keys()
# print(data.values())
# print(data.keys())
# print(list(data.values())) #преобразуем в список и выводим
# #вложенный список также является вложением (values)
# print(list(data.keys()))
# #все ключи словаря
# for k, v in data.items(): #функция разбивает словать на ключ-зачение (кортежи, либо список кортежей, если добавить list())
#     print(k, v)
# ###################################################