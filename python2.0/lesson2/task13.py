# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2
n = int(input('Введите кол-во дней: '))
input_temp_list = []
count_ot = 0 # кол-во дней с температурой > 0
max_ot = 0 # макс. кол-во дней оттепели, которые идут подряд
for i in range(n):
    temp = int(input(f'Введите температуру дня {i + 1}: ')) #спрашиваем температуру каждого дня
    input_temp_list.append(temp) #добавляем эту температуру в список введенных значений
    if temp > 0: #если температура введенного дня больше 0 (оттепель)
        count_ot +=1 #добавляем к счётчику дней оттепели +1
    else:
        count_ot = 0 #иначе (если температура отрицательная) - обнуляем счётчик
    if max_ot < count_ot: #если искомая переменная (кол-во дней оттепели подряд) меньше насчитанных и необнулённых в цикле дней оттепели
        max_ot = count_ot #то кладём в эту переменную (кол-во дней подряд) значение необнулённого счётчика (наш искомый ответ)
input_temp_str = [str(s) for s in input_temp_list] #переменная, которая будет показывать строку из введённого списка (для вывода как в условии)
print()
print(f'Input: {n} -> {" ".join(input_temp_str)}')
print(f'Output: {max_ot}')