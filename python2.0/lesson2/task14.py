# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

coin = int(input('Введите кол-во монеток: '))
count_1 = 0
count_0 = 0
input_list_coin = []
flip_over = 0
for i in range(coin):
    coin_side = int(input(f'Введите сторону {i+1} монетки (0 - орёл, 1 - герб): '))
    input_list_coin.append(coin_side)
    if coin_side == 0:
        count_0 += 1
    if coin_side == 1:
        count_1 += 1
if count_0 > count_1:
    flip_over = count_1
else:
    flip_over = count_0
input_str_coin = [str(s) for s in input_list_coin]
print()
print(f'{coin} -> {" ".join(input_str_coin)}')
print(flip_over)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
S = int(input('Введите подсказку S: '))
P = int(input('Введите подсказку P: '))
X = int(((S **2)/2 - P) ** (0.5))
Y = int(S - X)
print()
print(f'{S} {P} -> {X} {Y}')




# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Введите число N: '))
output_list_num = []
num = 2
for i in range(n):
    if num ** i <= n:
        output_list_num.append(num ** i)
    else:
        break
output_str_num = [str(s) for s in output_list_num]
print()
print(f'{n} -> {" ".join(output_str_num)}')