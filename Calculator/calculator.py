from tkinter import *
import button_func as fnc

root = Tk()
root.title("Calculator")
root.iconbitmap("E:/Downloads/Images/Calculator.ico")

n = Entry(width=40, borderwidth=5, justify="right")
n.grid(row=0, column=0, columnspan=5)


def buttons(str, x, y, cmd, tup):
    btn = Button(root, text=str, padx=x, pady=y, command=cmd)
    btn.grid(row=tup[0], column=tup[1])
    if str == "=":
        btn.grid(columnspan=2)
    return btn


# Number buttons and ans
button_1 = buttons("1", 20, 20, lambda: fnc.button_click(n, 1), (4, 0))
button_2 = buttons("2", 20, 20, lambda: fnc.button_click(n, 2), (4, 1))
button_3 = buttons("3", 20, 20, lambda: fnc.button_click(n, 3), (4, 2))
button_4 = buttons("4", 20, 20, lambda: fnc.button_click(n, 4), (3, 0))
button_5 = buttons("5", 20, 20, lambda: fnc.button_click(n, 5), (3, 1))
button_6 = buttons("6", 20, 20, lambda: fnc.button_click(n, 6), (3, 2))
button_7 = buttons("7", 20, 20, lambda: fnc.button_click(n, 7), (2, 0))
button_8 = buttons("8", 20, 20, lambda: fnc.button_click(n, 8), (2, 1))
button_9 = buttons("9", 20, 20, lambda: fnc.button_click(n, 9), (2, 2))
button_0 = buttons("0", 20, 20, lambda: fnc.button_click(n, 0), (5, 0))
decimal = buttons(".", 22, 20, lambda: fnc.button_click(n, "."), (5, 1))
ans = buttons("ans", 14, 20, lambda: fnc.button_click(n, fnc.ans), (5, 2))

# operators and sign
equal = buttons("=", 49, 20, lambda: fnc.result(n), (5, 3))
signs = buttons("±", 20, 20, lambda: fnc.sign(n), (2, 3))
plus = buttons("+", 20, 20, lambda: fnc.operators(n, "+"), (4, 3))
subtract = buttons("-", 22, 20, lambda: fnc.operators(n, "-"), (4, 4))
multiply = buttons("×", 20, 20, lambda: fnc.operators(n, "*"), (3, 3))
divide = buttons("÷", 21, 20, lambda: fnc.operators(n, "/"), (3, 4))
percent = buttons("%", 20, 20, lambda: fnc.operators(n, '%'), (2, 4))
exponent = buttons("^", 19, 20, lambda: fnc.operators(n, "^"), (1, 2))
sqr_root = buttons("√", 19, 20, lambda: fnc.operators(n, "√"), (1, 1))

# others
off = buttons("OFF", 14, 20, root.quit, (1, 4))
clear = buttons("AC", 15, 20, lambda: fnc.button_clear(n, "AC"), (1, 0))
bt_del = buttons("DEL", 14, 20, lambda: fnc.button_clear(n, "DEL"), (1, 3))

root.mainloop()
