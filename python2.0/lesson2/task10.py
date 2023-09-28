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