import os

from string import digits
from tkinter import StringVar, Tk, Label, Button, Entry
from tkinter.constants import END, GROOVE, RAISED, SOLID
from typing import NoReturn, Optional

op = ''

def screen(
    master, width: int = 35,
    bd: int = 5, columnspan: int = 3,
    row: int = 0, column: int = 0
    ) -> Entry:
    scrn = Entry(master=master, width=width, bd=bd)
    scrn.grid(row=row, column=column, columnspan=columnspan)
    return scrn

def show(text: str, scrn: object) -> NoReturn:
    global op
    showing = str(scrn.get())
    if showing == '':
        pass
    elif showing[0] == '0':
        scrn.delete(0, 0)
    if text == '.':
        pass
    elif text not in digits:
        op = text
    scrn.delete(0, END)
    scrn.insert(0, showing + text)

def button(
    master: object, text: str, command: object,
    row: int = None, column: int  = None,
    bd: int = 2, relief: Optional[str] = GROOVE, 
    padx: int = 40, pady: int = 20, 
    columnspan: int = 1
    ) -> Button:
    btn = Button(
        master=master, text=text, command=command,
        bd=bd, relief=relief,
        padx=padx, pady=pady, 
        )
    if text in digits:
        if  6 < int(text) < 10:
            btn.grid(row=1, column=(int(text)-7))
        elif 3 < int(text) < 7:
            btn.grid(row=2, column=(int(text)-4))
        elif 0 < int(text) < 4:
            btn.grid(row=3, column=(int(text)-1))
        elif int(text) == 0:
            btn.grid(row=4, column=0, columnspan=2)
    else:
        btn.grid(row=row, column=column)

def equals(scrn):
    global op
    print(op)
    showing = str(scrn.get())
    if op == '':
        scrn.delete(0, END)
        scrn.insert(0, showing)
    elif op == '+':
        showing = showing.split('+')
        print(showing)
        for x in showing:
            index = showing.index(x)
            x = float(x)
            showing[index] = x
        s = sum(showing)
        scrn.delete(0, END)
        scrn.insert(0, s)
    elif op == '-':
        showing = showing.split('-')
        print(showing)
        for x in showing:
            index = showing.index(x)
            x = -float(x)
            showing[index] = x
        s = sum(showing)
        scrn.delete(0, END)
        scrn.insert(0, s)
    elif op == 'x':
        showing = showing.split('x')
        print(showing)
        for x in showing:
            index = showing.index(x)
            x = float(x)
            showing[index] = x
        y = 1
        for x in showing:
            y *= x
        scrn.delete(0, END)
        scrn.insert(0, y)
    elif op == '÷':
        showing = showing.split('÷')
        print(showing)
        for x in showing:
            index = showing.index(x)
            x = float(x)
            showing[index] = x
        x = showing[0]/showing[1]
        scrn.delete(0, END)
        scrn.insert(0, x)

def delete(scrn):
    showing = scrn.get()
    scrn.delete(0, END)
    showing = showing[:-1]
    scrn.insert(0, showing)

def clear(scrn):
    scrn.delete(0, END)

def main():
    master = Tk()

    scrn = screen(master)

    btn_0 = button(master, str(0), lambda: show(str(0), scrn), padx=88, pady=18)
    btn_1 = button(master, str(1), lambda: show(str(1), scrn))
    btn_2 = button(master, str(2), lambda: show(str(2), scrn))
    btn_3 = button(master, str(3), lambda: show(str(3), scrn))
    btn_4 = button(master, str(4), lambda: show(str(4), scrn))
    btn_5 = button(master, str(5), lambda: show(str(5), scrn))
    btn_6 = button(master, str(6), lambda: show(str(6), scrn))
    btn_7 = button(master, str(7), lambda: show(str(7), scrn))
    btn_8 = button(master, str(8), lambda: show(str(8), scrn))
    btn_9 = button(master, str(9), lambda: show(str(9), scrn))
    btn_comma = button(master, '.', lambda: show('.', scrn), 4, 2, padx=20, pady=15)
    btn_equals = button(master, '=', lambda: equals(scrn), 4, 3, padx=30, pady=15)
    btn_plus = button(master, '+', lambda: show('+', scrn), 3, 3, padx=30, pady=15)
    btn_minus = button(master, '-', lambda: show('-', scrn), 3, 4, padx=30, pady=15)
    btn_cross = button(master, 'x', lambda: show('x', scrn), 2, 3, padx=30, pady=15)
    btn_divide = button(master, '÷', lambda: show('÷', scrn), 2, 4, padx=30, pady=15)
    btn_del = button(master, 'DEL', lambda: delete(scrn), 1, 3, padx=20, pady=15)
    btn_ac = button(master, 'AC', lambda: clear(scrn), 1, 4, padx=25, pady=15)

    master.mainloop()

if __name__ == '__main__':
    os.system('clear||cls')
    main()