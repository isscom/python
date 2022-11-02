# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = 'Что мне абв снег? Что мне зной? Когда мои друзья со мной'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# БОТ
from random import randint

a = int(input('Введите количество конфет'))
hod = 0
wins = {0: 'Игрок', 1: 'Бот'}
while a > 0:
    if a <= 28:
        print(f'Выиграл {wins[hod]}')
        break
    if hod % 2 == 0:
        print('Ход Игрока')
        d = int(input('Введите количество конфет, которое хотите взять'))
        a -= d
        print(f'Осталось конфет: {a}')
    else:
        print('Ход Бота')
        d = a % 29
        a -= d
        print(f'Осталось конфет: {a}')
    hod = (hod + 1) % 2

# 3. Создайте программу для игры в ""Крестики-нолики"".

doska = list(range(1,10))

def draw_board(board):
    for i in range(3):
        print ("|", doska[0+i*3], "|", doska[1+i*3], "|",doska[2+i*3], "|")

def stavim_hod(hod):
    valid = False
    while not valid:
        otvet = input("Введите номер клетки куда поставить значение " + hod+"? ")
        otv = int(otvet)
        if otv >= 1 and otv <= 9:
            if (str(doska[otv-1]) not in "XO"):
                doska[otv-1] = hod
                valid = True
            else:
                print ("Эта клетка занята")

def kto_viigral(doska):
    pobeda = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for x in pobeda:
        if doska[x[0]] == doska[x[1]] == doska[x[2]]:
            return doska[x[0]]
        return False

def igra(doska):
    count = 0
    win = False
    while not win:
        draw_board(doska)
        if count % 2 == 0:
            stavim_hod("X")
        else:
            stavim_hod("O")
        count += 1
        if count > 4:
            m = kto_viigral(doska)
            if m:
                print (m, "Победил!")
                win = True
                break
        if count == 9:
            print ("Победила дружба!")
            break

draw_board(doska)

igra(doska)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file_encode.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rle_encode(decoded_string))
print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')


# Вариант решения задачи 2
file5 = open('file5.txt', 'w')
ex5 = 'AdddLLkkKKfffffffKKDDnnRR'
file5.write(ex5)
file5.close()


def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
    else:
        res = res + str(count) + txt[i]
        count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    num = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            num += txt[i]
        else:
            res = res + txt[i] * int(num)
            num = ''
    return res

pol6 = open('file6.txt', 'w')
coding (ex5)
pol6.write(coding(ex5))

print(coding(ex5))
print(decoding(coding(ex5)))
pol6.close()