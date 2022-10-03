# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('введите целое, положительное число '))
print()

l = []
# list_from_file = input(C:\GB\HelloPython\file2_4.txt)
for i in range(0, n):
    l.append(-n+i)
l.append(int(0))
for i in range(n+1, 1+n*2):
    l.append(i-n)
for i in range(0, 1+n*2):
    print(f'l[{i}] = {l[i]}')
print()

numbers_from_file = []

path = 'file2_4.txt'
list_from_file = open(path, 'r')
for line in list_from_file:
    print('Из файла: '+line, end='')
    numbers_from_file.append(int(line))
list_from_file.close()
print('\n')

j = 0
product_of_list = 0
if len(numbers_from_file) == 0:
    print('Файл пуст')
else:
    while j != len(numbers_from_file):
        if j == 0:
            product_of_list = l[numbers_from_file[0]]
        else:
            product_of_list = product_of_list * l[numbers_from_file[j]]
        j = j + 1
    print(f'Произведение элементов = {product_of_list}')