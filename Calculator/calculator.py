from tkinter import *
import button_func as fnc

root = Tk()
root.title("Calculator")

n = Entry(root, width=40, borderwidth=5, justify="right")
n.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Number buttons
button_1 = Button(root,
                  text="1",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.button_click(n, 1)).grid(row=4, column=0)
button_2 = Button(root,
                  text="2",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.button_click(n, 2)).grid(row=4, column=1)
button_3 = Button(root,
                  text="3",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.button_click(n, 3)).grid(row=4, column=2)

button_4 = Button(root,
                  text="4",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.button_click(n, 4)).grid(row=3, column=0)
button_5 = Button(root,
                  text="5",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.button_click(n, 5)).grid(row=3, column=1)
button_6 = Button(root,
                  text="6",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.button_click(n, 6)).grid(row=3, column=2)

button_7 = Button(root,
                  text="7",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.button_click(n, 7)).grid(row=2, column=0)
button_8 = Button(root,
                  text="8",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.button_click(n, 8)).grid(row=2, column=1)
button_9 = Button(root,
                  text="9",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.button_click(n, 9)).grid(row=2, column=2)

button_0 = Button(root,
                  text="0",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.button_click(n, 0)).grid(row=5, column=0)

# operators and signs
sign = Button(root,
              text="±",
              padx=20,
              pady=20,
              command=lambda: fnc.operations(n, "±")).grid(row=2, column=3)

ans = Button(root,
             text="ans",
             padx=16,
             pady=20,
             command=lambda: fnc.button_click(n, ans)).grid(row=5, column=2)

plus = Button(root,
              text="+",
              padx=19,
              pady=20,
              command=lambda: fnc.operations(n, "+")).grid(row=4, column=3)

subtract = Button(root,
                  text="-",
                  padx=19,
                  pady=20,
                  command=lambda: fnc.operations(n, "-")).grid(row=4, column=4)
multiply = Button(root,
                  text="×",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.operations(n, "*")).grid(row=3, column=3)
divide = Button(root,
                text="÷",
                padx=19,
                pady=20,
                command=lambda: fnc.operations(n, "/")).grid(row=3, column=4)

equal = Button(root, text="=", padx=50, pady=20,
               command=lambda: fnc.result(n)).grid(row=5,
                                                   column=3,
                                                   columnspan=2)

percent = Button(root,
                 text="%",
                 padx=19,
                 pady=20,
                 command=lambda: fnc.operations(n, '%')).grid(row=2, column=4)

decimal = Button(root,
                 text=".",
                 padx=21,
                 pady=20,
                 command=lambda: fnc.button_click(n, ".")).grid(row=5,
                                                                column=1)
exponent = Button(root,
                  text="^",
                  padx=20,
                  pady=20,
                  command=lambda: fnc.operations(n, "^")).grid(row=1, column=2)

n_root = Button(root,
                text="√",
                padx=20,
                pady=20,
                command=lambda: fnc.operations(n, "√")).grid(row=1, column=1)

# Delete and clear buttons
clear = Button(root,
               text="AC",
               padx=15,
               pady=20,
               command=lambda: fnc.button_clear(n, "AC")).grid(row=1, column=0)

bt_del = Button(root,
                text="DEL",
                padx=15,
                pady=20,
                command=lambda: fnc.button_clear(n, "DEL")).grid(row=1,
                                                                 column=3)
root.mainloop()
