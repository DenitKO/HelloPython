# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc


def write_file(st, path):
    with open(path, 'w') as data:
        data.write(st)

def read_file(path):
    with open(path, 'r') as data:
        return data.read()


def Arhivate (file):
    toArhiv = {}
    toArhivStr = ''
    for i in file:
        if toArhiv.get(i):
            toArhiv[i] = toArhiv.get(i) + 1
        else:
            toArhiv[i] = 1


    for j in toArhiv.items():
        toArhivStr += str(j[1]) + j[0]
    return toArhivStr


def Unarhivate (file):
    toUnarhivStr = ''
    someString = ''
    for i in file:
        if i.isdigit():
            someString += i
        else:
            toUnarhivStr += int(someString)*i
            someString = ''
    return toUnarhivStr

pathInput = 'file5_4_input.txt'
pathOutput = 'file5_4_output.txt'

write_file('aaaaaaabbbbbbccccccccc', pathInput)
write_file('11a3b7c', pathOutput)

readInput = read_file(pathInput)
readOutpoot = read_file(pathOutput)

print(readInput)
print(Arhivate(readInput))
print(readOutpoot)
print(Unarhivate(readOutpoot))