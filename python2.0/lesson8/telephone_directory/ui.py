import commands

def hello():
    print('Добрый день! Вы находитесь в справочнике.')

def start():
    command = int(input('\n1. Показать записи\n2. Сохранить данные в текстовом файле\n3. Поиск записи по характеристике\n4. Выход\n\nДля продолжения работы - введите номер команды:\n'))
    if command == 1:
        commands.show_data()
        start()
    elif command == 2:
        commands.save_data_in_txt()
        start()
    elif command == 3:
        commands.find_data()
        start()
    elif command == 4:
        print('Всего доброго!')
    else:
        print('Ошибка. Такой команды нет.')
        start()