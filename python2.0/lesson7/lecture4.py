# ЗАДАЧА 1
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
print([(i, i**2) for i in list_1 if i % 2 == 0])

# ФАЙЛЫ
# a  - открыть и добавить, создать и добавить
# r  - чтение
# w  - запись (перезапись), создать
# w+ - запись, чтение, создание
# r+ - открыть и дозаписать

# colors = ['red', 'green', 'blue']
# data = open('test_file.txt', 'w', encoding='utf-8')
# data.writelines(colors)
# data.close()

# файла не было
# создался файл txt и в него были записаны значения

# постоянно открывать / закрывать файл не удобно
# =>

# with open('test_file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# Режим чтения:
# path = 'test_file.txt'
# data = open(path, 'r')
# for line in data: # проходим по файлу и печатаем его в консоль
#     print(line)
# data.close()

