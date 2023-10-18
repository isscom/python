def show_data():
    with open('sprav.txt', 'r', encoding='utf-8') as sprav:
        print('Текущие записи:')
        print(sprav.readlines())

def save_data_in_txt():
    with open('sprav.txt', 'a', encoding='utf-8') as sprav:
        sprav.write(input('Введите запись в формате Имя;+77777777;Город\n'))
        print('Запись успешно сохранена!')
        sprav.write('\n')

def find_data():
    what_find = str(input('Введите поисковый запрос: '))
    