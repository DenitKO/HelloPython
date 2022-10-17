from tkinter import Tk, Label, Button


def win(n):
    global game
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if game[each[0]] == n and game[each[1]] == n and game[each[2]] == n:
            return True


def stop_game():
   global game_left
   for item in game_left:
        buttons[item].config(bg="white", state="disabled")


def push(b):
    global game
    global game_left
    global turn
    if turn%2 == 0:
        label['text'] = 'Сходил первый игрок(X)'
        game[b] = 'X'
        buttons[b].config(text='X', bg="white", state="disabled")
        game_left.remove(b)
    else:
        label['text'] = 'Сходил второй игрок(O)'
        game[b] = 'O'
        buttons[b].config(text='O', bg="white", state="disabled")
        game_left.remove(b)
    turn += 1
    if turn > 4:
        if win('X'):
            label['text'] = 'Первый игрок(X) победил!'
            stop_game()
        elif win('O'):
            label['text'] = 'Второй игрок(O) победил!'
            stop_game()
        elif turn == 9:
            label['text'] = 'Ничья!'
            stop_game()


game = [None] * 9
game_left = list(range(9))
turn = 0

root = Tk()
label = Label(width=21, text="Игра крестики-нолики", font=('Arial', 20, 'bold'))
buttons = [Button(width=5, height=2, font=('Arial', 40, 'bold'), bg="green", command=lambda x=i: push(x)) for i in range(9)]

label.grid(row=0, column=0, columnspan=3)
row1 = 1
col = 0
for i in range(9):
    buttons[i].grid(row=row1, column=col)
    col += 1
    if col == 3:
        row1 += 1
        col = 0

root.mainloop()