# Задача №27. Общее обсуждение
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells.
# Output: 17

text = "She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."
print(f'Input: {text}')
# print(f'Output: {len(set(text.upper().split()))}')

# РЕШЕНИЕ НА ОТДЕЛЬНЫХ СТРОКАХ:
a = text.upper() # всё большими буквами
# SHE SELLS SEA SHELLS ON THE SEA SHORE; THE SHELLS THAT SHE SELLS ARE SEA SHELLS I'M SURE. SO IF SHE SELLS SEA SHELLS ON THE SEA SHORE, I'M SURE THAT THE SHELLS ARE SEA SHORE SHELLS.
b = a.split() # делаем список из строки
# ['SHE', 'SELLS', 'SEA', 'SHELLS', 'ON', 'THE', 'SEA', 'SHORE;', 'THE', 'SHELLS', 'THAT', 'SHE', 'SELLS', 'ARE', 'SEA', 'SHELLS', "I'M", 'SURE.', 'SO', 'IF', 'SHE', 'SELLS', 'SEA', 'SHELLS', 'ON', 'THE', 'SEA', 'SHORE,', "I'M", 'SURE', 'THAT', 'THE', 'SHELLS', 'ARE', 'SEA', 'SHORE', 'SHELLS.']
c = set(b) # превращаем список в множество (в с - те слова, кот. не повторяются)
# {'SEA', 'SURE', 'THAT', 'SHE', 'SELLS', 'THE', 'SHELLS.', 'SHORE;', 'SHELLS', 'ARE', 'IF', 'SHORE,', "I'M", 'SURE.', 'SHORE', 'ON', 'SO'}
d = len(c) # определяем кол-во элементов множества (явл. решением задачи)
# 17
# И запишем всё в одну строку:
print(f'Output: {len(set(text.upper().split()))}')