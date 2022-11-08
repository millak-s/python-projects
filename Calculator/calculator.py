from tkinter import *

root = Tk()
root.title("Calculator")

n = Entry(root, width=40, borderwidth=5, justify="right")
n.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def button_click(number):
    current = n.get()
    n.delete(0, END)
    n.insert(0, f"{current}{number}")


def button_clear():
    n.delete(0, END)


def addition():
    first_number = n.get()
    global f_num
    global operator
    operator = "+"
    f_num = float(first_number) if "." in first_number else int(first_number)
    n.delete(0, END)


def result():
    second_number = float(n.get()) if "." in n.get() else int(n.get())
    n.delete(0, END)
    global ans
    if operator == "+":
        ans = f_num + second_number
    elif operator == "-":
        ans = f_num - second_number
    elif operator == "*":
        ans = f_num * second_number
    else:
        ans = f_num / second_number

    ans = int(ans) if (ans - int(ans)) == 0 else ans
    n.insert(0, f"{ans}")


def subtraction():
    first_number = n.get()
    global f_num
    global operator
    operator = "-"
    f_num = float(first_number) if "." in first_number else int(first_number)
    n.delete(0, END)


def multiplication():
    first_number = n.get()
    global f_num
    global operator
    operator = "*"
    f_num = float(first_number) if "." in first_number else int(first_number)
    n.delete(0, END)


def button_divide():
    first_number = n.get()
    global f_num
    global operator
    operator = "/"
    f_num = float(first_number) if "." in first_number else int(first_number)
    n.delete(0, END)


button_1 = Button(root,
                  text="1",
                  padx=20,
                  pady=20,
                  command=lambda: button_click(1)).grid(row=3, column=0)
button_2 = Button(root,
                  text="2",
                  padx=20,
                  pady=20,
                  command=lambda: button_click(2)).grid(row=3, column=1)
button_3 = Button(root,
                  text="3",
                  padx=20,
                  pady=20,
                  command=lambda: button_click(3)).grid(row=3, column=2)

button_4 = Button(root,
                  text="4",
                  padx=20,
                  pady=20,
                  command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = Button(root,
                  text="5",
                  padx=20,
                  pady=20,
                  command=lambda: button_click(5)).grid(row=2, column=1)
button_6 = Button(root,
                  text="6",
                  padx=20,
                  pady=20,
                  command=lambda: button_click(6)).grid(row=2, column=2)

button_7 = Button(root,
                  text="7",
                  padx=20,
                  pady=20,
                  command=lambda: button_click(7)).grid(row=1, column=0)
button_8 = Button(root,
                  text="8",
                  padx=20,
                  pady=20,
                  command=lambda: button_click(8)).grid(row=1, column=1)
button_9 = Button(root,
                  text="9",
                  padx=20,
                  pady=20,
                  command=lambda: button_click(9)).grid(row=1, column=2)

button_0 = Button(root,
                  text="0",
                  padx=20,
                  pady=20,
                  command=lambda: button_click(0)).grid(row=4, column=0)

decimal = Button(root,
                 text=".",
                 padx=21,
                 pady=20,
                 command=lambda: button_click(".")).grid(row=4, column=1)

ans = Button(root,
             text="ans",
             padx=16,
             pady=20,
             command=lambda: button_click(ans)).grid(row=4, column=3)

plus = Button(root, text="+", padx=19, pady=20,
              command=addition).grid(row=3, column=3)

subtract = Button(root, text="-", padx=19, pady=20,
                  command=subtraction).grid(row=3, column=4)
multiply = Button(root, text="*", padx=20, pady=20,
                  command=multiplication).grid(row=2, column=3)
divide = Button(root, text="/", padx=19, pady=20,
                command=button_divide).grid(row=2, column=4)

clear = Button(root, text="del", padx=37, pady=20,
               command=button_clear).grid(row=1, column=3, columnspan=2)

equal = Button(root, text="=", padx=19, pady=20, command=result).grid(row=4,
                                                                      column=4)

root.mainloop()
