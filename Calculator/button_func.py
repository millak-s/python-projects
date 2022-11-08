from tkinter import *


def button_click(n, number):
    if number == "(-)":
        n.insert(0, number)
    current = n.get()
    if errors(n):
        return
    button_clear(n, "AC")
    n.insert(0, f"{current}{number}")


def button_clear(n, str):
    if str == "AC":
        n.delete(0, END)
    else:
        if errors(n):
            return
        n.delete(len(n.get()) - 1)


def errors(n):
    errors = ["Math Error", "SyntaxError"]
    return n.get() in errors


def operations(n, symbol):
    global f_num
    global operator
    operator = symbol
    if errors(n):
        return
    if len(n.get()) == 0 and symbol in "√":
        f_num = symbol
        n.insert(0, symbol)
        return
    try:
        f_num = float(n.get()) if "." in n.get() else int(n.get())
    except ValueError:
        n.insert(0, "SyntaxError")
    button_clear(n, "AC")


def result(n):
    if errors(n):
        return
    if "√" not in n.get():
        second_number = float(n.get()) if "." in n.get() else int(n.get())
    else:
        second_number = float(n.get()[1:]) if "." in n.get()[1:] else int(
            n.get()[1:])
    button_clear(n, "AC")
    global ans
    if operator == "+":
        ans = f_num + second_number
    elif operator == "-":
        ans = f_num - second_number
    elif operator == "*":
        ans = f_num * second_number
    elif operator == "^":
        ans = f_num**second_number
    elif operator == "√":
        ans = second_number**(1 / 2)
    elif operator == "%":
        ans = f_num / 100
    else:
        try:
            ans = f_num / second_number
        except ZeroDivisionError:
            n.insert(0, "Math Error")
            return

    ans = int(ans) if (ans - int(ans)) == 0 else ans
    n.insert(0, f"{ans}")
