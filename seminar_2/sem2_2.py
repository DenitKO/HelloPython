# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

digit = int(input('Введите положительное целое число: '))
g = 1
i = 0
if digit < 1:
    print('Вы ввели неверное число')
elif digit == 1:
    print('1')
else:
    while i != digit:
        g = g*(i+1)
        i = i + 1
        print(g, end=' ')