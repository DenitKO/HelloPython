# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
l = []
sum_of_list = 0.0
n = int(input('введите целое, положительное число '))
if n < 1:
    print('Вы ввели неверное число')
else:
    for i in range(0, n):
        if i == 0:
            l.append(int(1))
        else:
            l.append((1+1/i)**i)
        sum_of_list += l[i]
        print(f'l[{i}] = {l[i]}')
    print(f'сумма = {round(sum_of_list, 5)}')