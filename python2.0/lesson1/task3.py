# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

q_1desk = 2
q_pup1 = int(input("Введите кол-во учащихся в 1-м классе: "))
q_pup2 = int(input("Введите кол-во учащихся в 2-м классе: "))
q_pup3 = int(input("Введите кол-во учащихся в 3-м классе: "))
print("\nЗадача №3. Решение в группах. В некоторой школе решили набрать три новых\nматематических класса и оборудовать кабинеты для\nних новыми партами. За каждой партой может сидеть\nдва учащихся. Известно количество учащихся в\n каждом из трех классов. Выведите наименьшее\nчисло парт, которое нужно приобрести для них.")
print(f'Input: {q_pup1} {q_pup2} {q_pup3} (ввод чисел НЕ в одну строку)')
print(f'Output: {(q_pup1 + 1) // q_1desk + (q_pup2 + 1) // q_1desk + (q_pup3 + 1) // q_1desk}')
print(f'Output: {q_pup1 // q_1desk + q_pup1 % q_1desk + q_pup2 // q_1desk + q_pup2 % q_1desk + q_pup3 // q_1desk + q_pup3 % q_1desk}')