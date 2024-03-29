# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

# Решение:
def same_by(characteristic, objects):
    return len(list(filter(characteristic, objects))) == 0  # возвращаем утверждение, что кол-во элементов
                                                            # при применении функции characteristic к objects равно нулю

# Ввод:
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values): # по умолчанию условие выглядит так - x % 2 == True (или == 1)
    print('same')
else:
    print('different')
      
# Вывод:
# same

# map() - применяет фукнцию ко всем элементам и выдает результат
# [0, 0, 0, 0]

# filter() - фильтрует элементы и выдает те, кот. удовлетворили условию
# []

print(same_by(lambda x: x % 2, values))
# len(filter()) == 0
# True