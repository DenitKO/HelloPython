# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint as rI 


def write_file(st):
    with open('file4_4.txt', 'w') as data:
        data.write(st)


def create_сoef(k):
    new_list = [rI(-100,101) for i in range(k+1)]
    return new_list


def create_str(k, koef_list):
    count = 0
    dictionary = {}
    str_to_file = ''
    for i in koef_list:
        dictionary[count] = i
        count += 1
    for i in range(k, -1, -1):
        if dictionary.get(i)==0:
            dictionary.pop(i)
        elif i==k:
            if dictionary.get(i)<0:
                str_to_file += f' - {(-1)*dictionary.get(i)}x^{i}'
            else:
                str_to_file += f'{dictionary.get(i)}x^{i}'
        elif dictionary.get(i)>0:
            str_to_file += ' + '

        if i==0:
            if dictionary.get(i)<0:
                str_to_file += f' - {(-1)*dictionary.get(i)}'
            else:
                str_to_file += str(dictionary.get(i))

        if i!=k and i!=0 and dictionary.get(i)!=None:
            if dictionary.get(i)<0:
                str_to_file += f' - {(-1)*dictionary.get(i)}x^{i}'
            else:
                str_to_file += f'{dictionary.get(i)}x^{i}'
    str_to_file += ' = 0'
    return str_to_file

k = int(input("Введите натуральную степень k = "))
koef_list = create_сoef(k)
str_to_file = create_str(k, koef_list)
write_file(str_to_file)