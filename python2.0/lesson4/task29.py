# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Примечание: Программные коды ниже

n = int(input()) # запрашиваем число n
max_number = n # максимальное число не 1000 и не -1 (как у Вани и Пети), а n (первое введенное число)
while n != 0: # проверяем, что n не равно 0 (цикл продолжается до первого встретившегося нуля)
    n = int(input()) # в случае выполнения условия - вводим следующее n
    if max_number < n: # а если сохраненное число в переменную max_n меньше введенного n
        max_number = n # то запоминаем его в эту переменную (max_n)
print(max_number) # когда встретился n = 0 => выводим max_n которая была сохранена

# Ваня:
# n = int(input())
# max_number = 1000 ------------ строчка не верна, т.к. возникает вероятность несрабатывания цикла (исправляем на n)
# while n != 0:
#  n = int(input())
#  if max_number > n: ------------ проверяем на минимум, а не на максимум
#  max_number = n
# print(max_number)
 
# Петя:
# n = int(input())
# max_number = -1
# while n < 0: ------------ цикл завершается сразу после встречи положительного числа
#  n = int(input())
#  if max_number < n:
#  n = max_number ------------ нельзя записывать во введенное число max_number (наоборот)
# print(n) ------------ выводим не максимальное число, а введенное n (почему-то)