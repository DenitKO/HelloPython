# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

from functools import reduce
from random import randint as rI


def write_file(st, path):
    with open(path, 'w') as data:
        data.write(st)


def create_сoef(k):
    new_list = [rI(-100, 101) for i in range(k+1)]
    return new_list


def create_str(k, koef_list):
    count = 0
    dictionary = {}
    str_to_file = ''
    for i in koef_list:
        dictionary[count] = i
        count += 1
    for i in range(k, -1, -1):
        if dictionary.get(i) == 0:
            dictionary.pop(i)
        elif i == k:
            if dictionary.get(i) < 0:
                str_to_file += f'- {(-1)*dictionary.get(i)}x^{i}'
            else:
                str_to_file += f'{dictionary.get(i)}x^{i}'
        elif dictionary.get(i) > 0:
            str_to_file += ' + '

        if i == 0:
            if dictionary.get(i) < 0:
                str_to_file += f' - {(-1)*dictionary.get(i)}'
            else:
                str_to_file += str(dictionary.get(i))

        if i != k and i != 0 and dictionary.get(i) != None:
            if dictionary.get(i) < 0:
                str_to_file += f' - {(-1)*dictionary.get(i)}x^{i}'
            else:
                str_to_file += f'{dictionary.get(i)}x^{i}'
    str_to_file += ' = 0'
    return str_to_file


k = int(input("Введите натуральную степень k = "))
koef_list_1 = create_сoef(k)
koef_list_2 = create_сoef(k)
str_to_file1 = create_str(k, koef_list_1)
str_to_file2 = create_str(k, koef_list_2)
path1 = 'file4_5_1.txt'
path2 = 'file4_5_2.txt'
write_file(str_to_file1, path1)
write_file(str_to_file2, path2)


def read_file(path):
    with open(path, 'r') as data:
        return data.read()


from_file1 = read_file(path1)
from_file2 = read_file(path2)
count = 0
print(from_file1)
print(from_file2)
new_file1 = from_file1.rstrip()
from_file1 =  reduce(lambda x,y: x + y, new_file1)
new_file2 = from_file2.rstrip()
from_file2 =  reduce(lambda x,y: x + y, new_file2)
print(from_file1)
print(from_file2)
from_file1 = from_file1.split('=')
from_file1 = from_file1[0]
from_file2 = from_file2.split('=')
from_file2 = from_file2[0]
print(from_file1)
print(from_file2)
new_file1 = from_file1.rstrip()
from_file1 =  reduce(lambda x,y: x + y, new_file1)
new_file2 = from_file2.rstrip()
from_file2 =  reduce(lambda x,y: x + y, new_file2)
print(from_file1)
print(from_file2)
from_file1 = from_file1.split(' ')
from_file2 = from_file2.split(' ')
print(from_file1)
print(from_file2)