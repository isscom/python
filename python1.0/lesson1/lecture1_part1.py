# Переменные. Объявление переменных.
a = 123
b = 1.23
# print(a,b)
print(a)
print(b)

# Переменная с пустым значением
c = None
c = 555
print(c)

# Определить тип данных
print(type(b))

# Строка
s = 'Привет Мир!' # объявление строки
print(type(s), s)

# Переход на новую строку при объявлении строки
ss = 'Привет. Перейдем на новую строку? \nА давай!' # \n
print(ss)

# Вывод значения нескольких переменных через оператор PRINT
print(a,b,c)
print(a,'-',b,'-',c)
print('{} - {} - {}'.format(a,b,c)) # либо так
print(f'{a} - {b} - {c}') # либо так
print('{0} - {1} - {2}'.format(a,b,c)) # либо так (можно менять порядок)

# Логические значения
t = True
f = False
print(t,f)

# Списки (аналог массивов)
list = [1,2,3,4] # объявляем список
print(list)
# Можно миксовать различные типы данных в списки: числа, строки и т.п., но делать этого лучше не стоит

# Считывание данных
q = int(input('Введите q: ')) #int - целое, float - вещественное
w = int(input('Введите w: '))
# q = input('Введите q: ') - по умолчанию считывает в строку
# w = input('Введите w: ')
print(q,',',w)
print('{}, {}'.format(q,w))
print(f'{q}, {w}')

# Математические операции
# сложение, вычитание, деление (работает по умолчанию как для вещественных чисел), // деление в целых числах, ** возведение в степень, % остаток от деления
slogenie = a+b
vichitanie = a-b
delenie = a/b
delenie2 = a//b
stepen = a**b
ost = a%b

operacia_s_okrygleniem = round(a/b, 2)
operacia_s_okrygleniem2 = round(a*b, 3) # округляем операцию, далее указываем до скольки знаков

# Сокращенные операции присваивания
a = a + 5
a += 5 # сокращенная операция

# Логические операции

logic = 1 > 3
print(logic) # получаем Falce, т.к. это не правда

logic2 = 1 > 4 and 5 > 2
print(logic2)

logic3 = 1 != 2 #True
logic4 = 4 == 4 #True

f1 = [1,2,3,4]
print(f1)
print(not 2 in f1) # False
print(2 in f1) # True

# Проверяем чётность

f2 = [1,2,3,4]
is_odd = f2[1] % 2 == 0 # = not f2[1] % 2 (одно и то же)
print(is_odd)

# Логические ветвления и управляющие конструкции
# if else / if elif elif else
# Циклы while и for

list2 = [1,2,3,4,5] # Итерируемый объект, i - счетчик (можно также указать через запятую шаг цикла)
for i in list2:
    print(i**2)

for j in range(10):
    print(j) # Выводит все числа от 0 до 9

for j in range(1, 4):
    print(j) # Выводит все числа от 1 до 3

for j in range(1, 10, 2):
    print(j) # Выводит все числа от 1 до 9 с шагом 2

#Встроенные функции
text = 'Съешь ещё эти мягких французских булок'
print(len(text)) #38 - длина строки
print('ещё' in text) #True - есть ли фрагмент в тексте?
print(text.isdigit()) #False - являются ли числами символы в строке?
print(text.islower()) #False - являются ли символами нижнего регистра?
print(text.replace('ещё', 'ЕЩЁ')) # производится замена