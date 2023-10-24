# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('')
print('2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')
print('')
print('Решение:')

# ПЕРВЫЙ ВАРИАНТ
# def logical_statement(x, y, z):
#     print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
#     return (not (x or y or z)) == (not x and not y and not z)
# if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
# logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
# logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
#     print("Истинно")
# else:
#     print("Ложно")


# ВТОРОЙ ВАРИАНТ
# def check(x,y,z):
#     print()
#     return ()
# if check(0,0,0) and check(0,0,1) and check(0,1,0) and check(0,1,1) and check(1,0,0) and check(1,0,1) and check(1,1,0) and check(1,1,1):
#     print(True)
# else:
#     print(False)

# ТРЕТИЙ ВАРИАНТ
for x in range(2):
    for y in range(2):
        for z in range(2): # циклами перебираем 0 и 1 для каждого x,y,z
            print(not (x or y or z) == (not x and not y and not z)) # перевели утверждение в форму, понятную компьютеру