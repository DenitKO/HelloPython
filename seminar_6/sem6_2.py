# Просмотреть свои предыдущие ДЗ и попробовать применить к ним 
# lambda, filter, map, zip, enumerate, list comprehension, там где это возможно.

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# n = int(input('\nвведите целое, положительное число '))
# print()

# new_list = []
# for i in range(-n, n+1):
#     new_list.append(i)
# for i in range(0, n*2+1):
#     print(f'{new_list[i]},', end=' ')
# print('\n')

# numbers_from_file = []
# path = 'file2_4.txt'
# list_from_file = open(path, 'r')
# for line in list_from_file:
#     print('Из файла: '+line, end='')
#     numbers_from_file.append(int(line))
# list_from_file.close()
# print('\n')

# j = 0
# product_of_list = 0
# if len(numbers_from_file) == 0:
#     print('Файл пуст')
# else:
#     while j != len(numbers_from_file):
#         if j == 0:
#             product_of_list = new_list[numbers_from_file[0]]
#         else:
#             product_of_list = product_of_list * new_list[numbers_from_file[j]]
#         j = j + 1
#     print(f'Произведение элементов = {product_of_list}\n')

from functools import reduce

def write_file(st, path):
    with open(path, 'w') as data:
        data.write(st)

def read_file(path):
    with open(path, 'r') as data:
        return data.read()

n = int(input('\nвведите целое, положительное число '))

path = "file6_2.txt"
write_file('1 4 11', path)
digits = list(map(int, read_file(path).split()))
new_list = [i for i in range(-n, n+1)]
new_list = list(enumerate(new_list))

finish_list = [i[1] for j in digits for i in new_list if i[0] == j]
print(f'произведение элементов с указанных позиций =', reduce(lambda x,y: x*y, finish_list))