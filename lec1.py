# print ('Hello World')

# # Типы данных и переменная
# # int, float, boolean, str, list, None
# # нельзя инициализировать неявно пустую переменную для дальнейшего использования,
# # необходимо присваивать ей None
# # например
# value = None

# a = 123
# b = 1.23
# s = ('Hello World')
# print(a)
# print(b)
# value = 1234
# print(value)
# # чтобы узнать тип данных пишем
# print(type(a))

# print(s)
# print(a, '-',b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)
# list = [] # Для вывода можно указать пустой
# print(list)

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, ' + ' , b, ' = ', a+b)

# a = 2
# b = 3
# c = round(a*b, 5)
# print(c)

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# Управление констркции
#  if, if-else


# Инвертирование целых чисел
# original = 123456789
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(inverted)

# Управляющие конструкции:
# for

# 1 Стандартный for
# for i in 1,2,3,4,5:
#     print(i**2)

# 2 список в for
# list = [1,2,3,10,5]
# for i in list:
#     print(i)

# 3 range в for
# r = range(10)
# for i in r:
#     print(i)

# 4 или можно укаазать range внутри for
# for i in range(10):
#     print(i)

# 5 можно явно указывать от и до
# for i in range(1, 5):
#     print(i)

# 6 можно явно указывать от 1 до 6 с шагом 2
# for i in range(1, 6, 2):
#     print(i)

# text = "съешь еще этих мягких французских булок"


# help(text.istitle)

# print(len(text))                    # 39
# print('еще' in text)                # True
# print(text.isdigit)                 # False
# print(text.islower)                 # True
# print(text.replace('еще' , 'ЕЩЕ'))  #

# for c in text:
#     print(c)