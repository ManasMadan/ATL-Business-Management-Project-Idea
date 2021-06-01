import tkinter as tk
import numpy as np
import xlrd
import pyautogui as pag

book = xlrd.open_workbook("Stock Room.xls")
sh = book.sheet_by_index(0)

def sumar(a):
    sum = 0
    for i in a:
        sum += i
    return sum

def select():
    itms = sh.col_values(0)
    n = itms.index(var.get())

    x = sh.row_values(n)
    print(x)
    x.pop(0)
    x.pop(0)
    st = x[0]
    x.pop(0)
    ord = False
    left = st - sumar(x)
    if(left <= 5):
        ord = True

    txt = ""
    if(ord == True):
        txt = "You Should Consider Ordering"
    else:
        txt = "Ordering Not Needed"

    ch = pag.alert(f"You Have {left} {var.get()} left. {txt}")

    



root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (430, 80, 200, 150))
root.title("Select")

var = tk.StringVar(root)
var.set("Select Item")

choices = sh.col_values(0)
option = tk.OptionMenu(root, var, *choices)
option.pack(side='left', padx=10, pady=10)

button = tk.Button(root, text="Check Stock For", command=select)
button.pack(side='left', padx=20, pady=10)

root.mainloop()
