# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

l = []
n = int(input('введите целое, положительное число '))

for i in range(0, n):
    l.append(-n+i)
l.append(int(0))
for i in range(n+1, 1+n*2):
    l.append(i-n)
for i in range(0, 1+n*2):
    print(f'l[{i}] = {l[i]}')
# print(f'сумма = {round(sum_of_list, 5)}')