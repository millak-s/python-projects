from tkinter import *

# TODO: make the ans button delete anything that appears before it is pressed


def button_click(n, number):
    if errors(n):
        return
    if number == "-":
        n.insert(0, number)
    current = n.get()
    button_clear(n, "AC")
    n.insert(0, f"{current}{number}")


# converts from from converts numbers to appropriate type
def int_float(n, num):
    if errors(n):
        return
    if type(num) is str:
        try:
            return float(num) if "." in num else int(num)
        except ValueError:
            return num
    else:
        return int(num) if num - int(num) == 0 else float(num)


#  Changes integer from positive to negative and vice-versa
def sign(n):
    current = n.get()
    current = float(current)
    n.delete(0, END)
    current /= -1
    current = int_float(n, current)
    n.insert(0, f"{current}")


# Deletes entry from end or clears the whole entry
def button_clear(n, str):
    if str == "AC":
        n.delete(0, END)
    else:
        if errors(n):
            return
        n.delete(len(n.get()) - 1)


#  checks for errors
def errors(n):
    errors = ["Math Error", "SyntaxError", "None"]
    if any([i in n.get() for i in errors]):
        return True
    return False


def operators(n, symbol):
    global operator
    operator = symbol
    global f_num

    if errors(n):
        return

    if len(n.get()) == 0 and symbol in "√":
        f_num = symbol
        n.insert(0, symbol)
        return

    f_num = int_float(n, n.get())
    button_clear(n, "AC")


def operations(n):
    if errors(n):
        return

    if "√" in n.get():
        second_number = int_float(n, n.get()[1])
    else:
        second_number = int_float(n, n.get())

    button_clear(n, "AC")
    global ans

    if operator == "+":
        return f_num + second_number
    elif operator == "-":
        return f_num - second_number
    elif operator == "*":
        return f_num * second_number
    elif operator == "^":
        return f_num**second_number
    elif operator == "√":
        return second_number**(1 / 2)
    elif operator == "%":
        return f_num / 100
    elif operator == "/":
        try:
            return f_num / second_number
        except ZeroDivisionError:
            return "Math Error"


def result(n):
    result = operations(n)
    int_float(n, result)
    n.insert(0, f"{result}")
