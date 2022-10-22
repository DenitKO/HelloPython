# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc


def write_file(st, path):
    with open(path, 'w') as data:
        data.write(st)


def read_file(path):
    with open(path, 'r') as data:
        return data.read()


def Archive(file):
    toArchiveDict = {}
    toArchivStr = ''

    for i in file:
        if toArchiveDict.get(i):
            toArchiveDict[i] = toArchiveDict.get(i) + 1
        else:
            toArchiveDict[i] = 1

    for j in toArchiveDict.items():
        toArchivStr += str(j[1]) + j[0]
    return toArchivStr


def Unarchive(file):
    toUnacrhiveStr = ''
    tempString = ''
    for i in file:
        if i.isdigit():
            tempString += i
        else:
            toUnacrhiveStr += int(tempString)*i
            tempString = ''
    return toUnacrhiveStr


pathInput = 'file5_4_input.txt'
pathOutput = 'file5_4_output.txt'

write_file('aaaaaaabbbbbbccccccccc', pathInput)
write_file('11a3b7c', pathOutput)

readInput = read_file(pathInput)
readOutpoot = read_file(pathOutput)

print(readInput)
print(Archive(readInput))
print(readOutpoot)
print(Unarchive(readOutpoot))