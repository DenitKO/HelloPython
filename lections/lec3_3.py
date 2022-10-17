# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа)
# Пример:
# 1 2 3 5 8 15 23 38
# получить:
# [(2, 4), (8, 64), (38, 1444)]

# чтение из файла

def write_file(st):
    with open('file4_4.txt', 'w') as data:
        data.write(st)

path = ('lections/file3_3.txt')
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    print(space_pos)
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e,e **2))
print(out)

# как я сделал

old_list = [1, 2, 3, 5, 8, 15, 23, 38]

x = lambda i: i**2

def calc (op, f):
    return op(f)
    
list = [(i, x(i)) for i in old_list if i%2 == 0]
print(list)

# как у них сделано

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data2 = '1 2 3 5 8 15 23 38'.split()
res = select(int, data2)
res = where(lambda e: not e % 2, res)
res = select(lambda e: (e, e**2), res)
print(res)