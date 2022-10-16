# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


digit = (input("Введите число: "))
new_list = []
unrepeatable = {}

for c in digit:
    if unrepeatable.get(c):
        unrepeatable[c] = unrepeatable.get(c) + 1
    else:
        unrepeatable[c] = 1

for c in unrepeatable.keys():
    if unrepeatable.get(c) == 1:
        new_list.append(c)
print(f'Список уникальных эллементов: {new_list}')