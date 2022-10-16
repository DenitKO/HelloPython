# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001,   π = 3.141
# при d = 0.1,     π = 3.1
# при d = 0.00001, π = 3.14154
#     d от 0.1 до 0.0000000001

from math import pi

def accuracy(digit):
    i = 1
    if digit == 0.1:
        return i
    else:
        i = 1
        while digit != 0.1:
            digit *= 10
            i += 1
        return i

digit =  float(input("Введите число d для заданной точности числа Пи:\n"))
d = accuracy(digit)
print(f'число Пи с заданной точностью {digit} равно {round(pi, d)}')