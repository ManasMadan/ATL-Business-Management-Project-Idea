import tkinter as tk
import xlrd
import matplotlib.pyplot as plt
import numpy as np

book = xlrd.open_workbook("Stock Room.xls")
sh = book.sheet_by_index(0)


def select():
    itms = sh.col_values(0)
    n = itms.index(var.get())

    x = sh.row_values(n)
    x.pop(0)
    x.pop(0)
    x.pop(0)
    print(x)
    xpoints = np.array([1,2,3,4,5,6,7])
    ypoints = np.array(x)
    plt.plot(xpoints, ypoints,linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
    plt.show()


root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
root.title("Select")

var = tk.StringVar(root)
var.set("Select Item")

choices = sh.col_values(0)
option = tk.OptionMenu(root, var, *choices)
option.pack(side='left', padx=10, pady=10)

button = tk.Button(root, text="Open Graph For", command=select)
button.pack(side='left', padx=20, pady=10)

root.mainloop()
