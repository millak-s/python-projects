from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.iconbitmap("tkinter/image viewer/pictures 2.ico")
n = 0
path = "tkinter/image viewer"
extensions = [
    "jpeg", "tif", "tiff", "gif", "jpeg", "jpg", "jif", "jfif", "jp2", "jpx",
    "j2k", "j2c", "fpx", "pcd", "png", "webp", "ico", "stl", "bmp"
]


# Determines files to be viewed from directory
def check_file(source, categories, lst):
    list = os.listdir(source)
    for item in list:
        item_path = os.path.join(source, item)
        if not os.path.isfile(item_path):
            check_file(item_path, categories, lst)
        else:
            extension = item.split(".")[1]
            if extension in categories:
                lst.append((item_path, item))


# Opens images so they can be placed on the GUI
def img(num):
    global lst
    lst = []
    global m_img
    check_file(path, extensions, lst)
    m_img = ImageTk.PhotoImage(Image.open(lst[num][0]))
    return m_img


def show(n):
    m_lbl = Label(image=img(n))
    m_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    num_img = lst.index(lst[n]) + 1
    lbl = Label(text=f"Image {num_img} of {len(lst)}",
                bd=1,
                relief=SUNKEN,
                anchor=E)
    lbl.grid(row=2, column=0, columnspan=3, sticky=W + E)

    root.title(lst[n][1])


# Moves to next or previous image
def change(num, direction):
    global m_lbl
    global lbl
    global n
    if direction == ">":
        n = num + 1 if (num + 1) < len(lst) else 0
    else:
        n = num - 1 if num > 0 else len(lst) - 1

    show(n)


def buttons(str, cmd, tup):
    btn = Button(root, text=str, command=cmd)
    btn.grid(row=tup[0], column=tup[1], pady=10)
    return btn


back = buttons("<<<", lambda: change(n, "<"), (1, 0))
forward = buttons(">>>", lambda: change(n, ">"), (1, 2))
off = buttons("Exit", root.quit, (1, 1))

show(0)
root.mainloop()
