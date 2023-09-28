# Задача №15.
# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# 1 <= масса <= 1000 (условие от препода)
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

count_melon = int(input('Введите кол-во арбузов: '))
input_mass_list = []
max_mass_melon = 0
min_mass_melon = 1001
for i in range(count_melon):
    mass_melon = int(input(f'Сколько весит арбуз №{i+1}? '))
    input_mass_list.append(mass_melon)
    if mass_melon > max_mass_melon:
        max_mass_melon = mass_melon
    if mass_melon < min_mass_melon:
        min_mass_melon = mass_melon
input_mass_str = [str(s) for s in input_mass_list]
print()
print(f'Input: {count_melon} -> {" ".join(input_mass_str)}')
print(f'Output: {min_mass_melon} {max_mass_melon}')
