# Знакомство с языком Python (лекции)
# Урок 2. Данные, функции и модули в Python

# a – открытие для добавления данных (если добавть данные в несуществующий файл, он будет добавлен)
# r – открытие для чтения данных
# w – открытие для записи данных (перезапись)
# w+ - открывать для записи и читать из него(если файла не существует, он будет создан)
# r+ - открывать для чтения и записывать в него(если файла не существует, нас ждёт ошибка)

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
# нет необходимости разорвать соединение файловой переменной с файлом на диске

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()
# необходимо разорвать соединение файловой переменной с файлом на диске
# для избежания утечек памяти

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

exit()
# 