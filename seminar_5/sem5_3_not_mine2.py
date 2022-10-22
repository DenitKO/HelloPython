from tkinter import *
import random as rI


def win(n):
   global game
   if \
      (game[0] == n and game[1] == n and game[2] == n) or \
      (game[3] == n and game[4] == n and game[5] == n) or \
      (game[6] == n and game[7] == n and game[8] == n) or \
      (game[0] == n and game[3] == n and game[6] == n) or \
      (game[1] == n and game[4] == n and game[7] == n) or \
      (game[2] == n and game[5] == n and game[8] == n) or \
      (game[0] == n and game[4] == n and game[8] == n) or \
      (game[2] == n and game[4] == n and game[6] == n):
      return True

def stop_game():
   global game_left
   for item in game_left:
      buttons[item].config(bg="white", state="disabled")

def push(b):
   global game
   global game_left
   global turn
   game[b] = 'X'
   buttons[b].config(text='X', bg="white", state="disabled")
   game_left.remove(b)
   if b == 4 and turn == 0:
      t = rI.choice(game_left)
   elif b != 4 and turn == 0:
      t = 4
   if turn > 0:
      t = 8 - b
   if t not in game_left:
      try:
         t = rI.choice(game_left)
      except IndexError:
         label['text'] = 'Игра окончена'
         stop_game()

   game[t] = 'O'
   buttons[t].config(text='O', bg="white", state="disabled")
   if win('X'):
      label['text'] = 'Вы победили!'
      stop_game()
   elif win('O'):
      label['text'] = 'Вы проиграли!'
      stop_game()
   else:
      if (len(game_left) > 1):
         game_left.remove(t)
      else:
         label['text'] = 'Игра окончена!'
         stop_game()
      print(game_left)
      turn += 1


game = [None] * 9
game_left = list(range(9))
turn = 0

root = Tk()
label = Label(width=20, text="Игра крестики-нолики", font=('Arial', 20, 'bold'))
buttons = [Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="green", command=lambda x=i: push(x)) for i in range(9)]

label.grid(row=0, column=0, columnspan=3)
some_row = 1
some_col = 0
for i in range(9):
   buttons[i].grid(row=some_row, column=some_col)
   some_col += 1
   if some_col == 3:
      some_row += 1
      some_col = 0


root.mainloop()
