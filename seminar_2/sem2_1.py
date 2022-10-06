# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def fractional (num):
    x = num.split(".") 
    a = int(x[0])
    b = int(x[1])
    mult = 1
    while (a != 0):
        mult = mult * (a % 10)
        a = a // 10
    while (b != 0):
        mult = mult * (b % 10)
        b = b // 10
    print("Произведение цифр равно:", mult)

digit = float(input('Введите число: '))

x = str(digit)

fractional(x)