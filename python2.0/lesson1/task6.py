# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
Num = int(input('Введите шестизначный номер билета: '))
if Num//100000 + Num//10000%10 + Num//1000%10 == Num//100%10 + Num//10%10 + Num%10:
    print(f'{Num} -> yes')
else:
    print(f'{Num} -> no')