from tkinter import *
import tkinter.filedialog

root = Tk()

# ----------------------------------------------------------------------------

# def Hello(event):
#     print("Yet another hello world")

# btn = Button(root,                  #родительское окно
#              text="Click me",       #надпись на кнопке
#              width=30,height=5,     #ширина и высота
#              bg="white",fg="black") #цвет фона и надписи
# btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
# btn.pack()                          #расположить кнопку на главном окне
# root.mainloop()

# ----------------------------------------------------------------------------

# Button(root, text = '1').pack(side = 'left')
# Button(root, text = '2').pack(side = 'top')
# Button(root, text = '3').pack(side = 'right')
# Button(root, text = '4').pack(side = 'bottom')
# Button(root, text = '5').pack(fill = 'both')
# root.mainloop()

# ----------------------------------------------------------------------------

# grid(). Размещает виджеты на сетке. Основные параметры:
# row/column – строка/столбец в сетке, 
# rowspan/columnspan – сколько строк/столбцов занимает виджет. Пример:

# Button(root, text = '1').grid(row = 1, column = 1)
# Button(root, text = '2').grid(row = 1, column = 2)
# Button(root, text = '__3__').grid(row = 2, column = 1, columnspan = 2)
# root.mainloop()

# ----------------------------------------------------------------------------

# Button(root, text = '1').place(x = 10, y = 10, width = 30)
# Button(root, text = '2').place(x = 45, y = 20, height = 15)
# Button(root, text = '__3__').place(x = 20, y = 40)
# root.mainloop()

# ----------------------------------------------------------------------------



def Quit(ev):
    global root
    root.destroy()
    
def LoadFile(ev): 
    fn = tkinter.filedialog.Open(root, filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end') 
    textbox.insert('1.0', open(fn, 'rt').read())
    
def SaveFile(ev):
    fn = tkinter.filedialog.SaveAs(root, filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn+=".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))

# root = Tk()

panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

loadBtn = Button(panelFrame, text = 'Load')
saveBtn = Button(panelFrame, text = 'Save')
quitBtn = Button(panelFrame, text = 'Quit')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x = 10, y = 10, width = 40, height = 40)
saveBtn.place(x = 60, y = 10, width = 40, height = 40)
quitBtn.place(x = 110, y = 10, width = 40, height = 40)

root.mainloop()