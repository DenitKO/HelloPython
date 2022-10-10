# СЛОВАРИ
# Это неупорядочинные коллекции произвольных объектов с доступом по ключу

from turtle import left


dictionary = {} # присваеваем пустой словарь <class 'dict'>
                # обратный слеш \ позволяет не писать всё в одну строчку
dictionary = \
    {
        'up': '↑',  
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary) #     {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left']) # ←
# типы ключей могут отличатся
print()
for k in dictionary.keys():
    print({k})
print()
for v in dictionary.keys():
    print(dictionary[v])
print()
dictionary['left'] = '←'
print(dictionary['left'])
print()
del dictionary['left']

for item in dictionary: #for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))