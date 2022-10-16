# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число: "))

oldNum = number
simpleNumDiv = []
divinder = 2

while number > 2:
    if number%divinder != 0:
        divinder += 1
    else:
        number //= divinder
        simpleNumDiv.append(divinder)

print(f'Cписок простых множителей числа {oldNum}: {simpleNumDiv}')