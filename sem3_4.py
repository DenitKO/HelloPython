# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(46)
print(a, end='')
b = ''
i = 0
while a / 2 > 0:
    b = b + str(a % 2)
    a = int(a / 2)
print(' в 10-ной = ', end='')
for z in b:
    print(b[-i-1], end='')
    i += 1
print(' в двоичной')