import smtplib, ssl
import pyautogui as pag
import xlrd
import tkinter as tk

q = 0

def main():
    global q

    choices = sh.col_values(0)
    n = choices.index(var.get())
    receiver_email = sh.col_values(1)[n]
    print(receiver_email)
    print(n)
    

    q = pag.prompt("Enter Quantity")
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "atlvvdavtest@gmail.com"  # Enter your address
    password = pag.password("Type your password and press enter: ")
    message = f"""\
        We Need To Order {q} {var.get()} """



    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

book = xlrd.open_workbook("Stock Room.xls")
sh = book.sheet_by_index(0)



root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (400, 200, 200, 150))
root.title("Select")

var = tk.StringVar(root)
var.set("Select Item")



choices = sh.col_values(0)
option = tk.OptionMenu(root, var, *choices)
option.pack(side='left', padx=10, pady=10)

button = tk.Button(root, text="Order", command = main)
button.pack(side='left', padx=20, pady=10)


root.mainloop()