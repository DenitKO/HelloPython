# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0


from random import randint as rI

def write_file(st, path):
    with open(path, 'w') as data:
        data.write(st)

def read_file(path):
    with open(path, 'r') as data:
        return data.read()

def createCoef():
    coef = {}
    degree = int(input("Введите максимальную степень: "))
    for i in range(degree, -1, -1):
        coef[i] = rI(-20,20)

    return coef


def createEquation(coef_list: dict):
    equation = ''
    first = True

    for i in coef_list.items():
        if first:
            first = False
            if i[1] < 0:
                equation += ' -' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += str(abs(i[1])) + 'x^' + str(i[0])
        else:
            if i[1] < 0:
                equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])

    return equation + ' = 0'


def parseEquation(equation: str):
    
    equation = equation.replace(' + ', ' +').replace(' - ', ' -').replace(' = 0', '')
    equation = equation.split()

    dictEquation = {}
    for i in range(len(equation)):
        equation[i] = equation[i].replace('+','').split('x^')
        dictEquation[int(equation[i][1])] = int(equation[i][0])
    return dictEquation

path1 = 'file4_5_1.txt'
path2 = 'file4_5_2.txt'
write_file(createEquation(createCoef()), path1)
write_file(createEquation(createCoef()), path2)

parEq1 = parseEquation(read_file(path1))
parEq2 = parseEquation(read_file(path2))

def sumOfDictionaries (parEq1, parEq2):
    resEquation = {}
    for i in range(max(len(parEq1), len(parEq2)), -1, -1):
        first = parEq1.get(i)
        second = parEq2.get(i)
        if first != None or second != None:
            resEquation[i] = (first if first != None else 0) + (second if second != None else 0)
    return resEquation

# print(read_file(path1))
# print(read_file(path2))
# print(createEquation(parEq1))
# print(createEquation(parEq2))
print(createEquation(sumOfDictionaries(parEq1,parEq2)).replace('x^1', 'x').replace('x^0', ''))