# ФАЙЛЫ
# a  - открыть и добавить, создать и добавить    MAIN a(appen) добавление информации (создается если не существует)
# r  - чтение                                    MAIN r(read)  прочтение данных
# w  - запись (перезапись), создать              MAIN w(write) добавление информации (с учетом удаления всех старых записей) (создается если не существует)
# w+ - запись, чтение, создание
# r+ - открыть и дозаписать

#############################################
# a  - открыть и добавить, создать и добавить

# database = open('data.txt', 'a', encoding='utf-8')
# # database.write('Ivan;Ivanov;+79166666666')
# # database.close()

# # Ivan;Ivanov;+79166666666Ivan;Ivanov;+79166666666Ivan;Ivanov;+79166666666Ivan;Ivanov;+79166666666
# # запустили программу несколько раз
# # не добавили переход на новую строку \n

# database.write('Ivan;Ivanov;+79166666666\n')
# database.close()

#############################################
# w  - запись (перезапись), создать

with open('data.txt', 'w', encoding='utf-8') as database:
    database.write('Petr;Sidorov;+79161112233\n')
# данная конструкция позволяет не закрывать файл
# в результате всё содержимое файла было перезаписано на одну запись

#############################################
database = open('data.txt', 'a', encoding='utf-8')
database.write('Ivan;Ivanov;+79166666666\n')
database.close()
# r  - чтение
with open('data.txt', 'r', encoding='utf-8') as database:
    print(database.readlines())
# ['Petr;Sidorov;+79161112233\n', 'Ivan;Ivanov;+79166666666\n']