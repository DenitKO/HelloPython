# 2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint as rI

inTotal = 150
botMinus = 0
whatGamer = True
bot = True
if input('Хотите играть против бота? yes or no: ')=='yes':
    while inTotal > 0:
        if whatGamer:
            whatGamer = False
            print()
            print(['Ходит первый игрок'])
            print(f'Осталось {inTotal} конфет')
            inTotal = inTotal - int(input('сколько нужно вычесть от 0 до 28? \n'))

        else:
            whatGamer = True
            print()
            print(['Ходит бот'])
            print(f'Осталось {inTotal} конфет')
            if 29 < inTotal < 57:
                botMinus = inTotal - 29
            elif inTotal < 29:
                botMinus = inTotal
            else:
                botMinus = rI(0,28)
            inTotal = inTotal - botMinus
            print(f'Бот забрал {botMinus} конфет')
else:
    bot=False
    while inTotal > 0:
        if whatGamer:
            whatGamer = False
            print()
            print(['Ходит первый игрок'])
            print(f'Осталось {inTotal} конфет')
            inTotal = inTotal - int(input('сколько нужно вычесть от 0 до 28? \n'))

        else:
            whatGamer = True
            print()
            print(['Ходит второй игрок'])
            print(f'Осталось {inTotal} конфет')
            inTotal = inTotal - int(input('сколько нужно вычесть от 0 до 28? \n'))
print()
if whatGamer:
    if bot:
        print('Победил Бот')
    else:
        print('Победил второй игрок')
else:
    if bot:
        print('Победил игрок')
    else:
        print('Победил первый игрок')