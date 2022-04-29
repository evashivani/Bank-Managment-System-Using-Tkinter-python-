from tkinter import *
from tkinter import messagebox
window=Tk()
window.configure(bg='Black')
window.title('Home Page')
window.geometry('350x350')
def show():

    if clicked.get()=="Cash Deposit":
        CashDeposit()
    elif clicked.get()=="Cash Withdrawl":
        CashWith()
    elif clicked.get()=="Account Details":
        AccDetail()
    elif clicked.get()=="Account Close":
        AccClose()
    elif clicked.get()=="Exit":
        Exit()
    #messagebox.showinfo('showinfo', 'Select option and then click me!!!')

def CashDeposit():
    window.destroy()
    import page2
def CashWith():
    window.destroy()
    import page3
#def AccDetail():
    #window.destroy()
    #import page4
def AccClose():
    window.destroy()
    import page5
def Exit():
    window.destroy()
    import page6
def doubleclick(event):
    messagebox.showinfo('showinfo', 'Select option and then click me!!!')
# Dropdown menu options
options = [
    "Cash Deposit",
    "Cash Withdrawl",
    "Account Details",
    "Account Close",
    "Exit"
]
clicked=StringVar(window) #variable which store datatype of menu

clicked.set("HOME")

# Create Dropdown menu
drop = OptionMenu(window, clicked, *options)
drop.grid(row=2,column=1,sticky=W)

l1=Label(window,text='Welcome to Bank Management System',fg='black',bg='pink')
l1.grid(row=0,column=2,sticky=W,pady=10,padx=10)

b=Button(window, text="Click Me", background='yellow',command=show)
b.grid(row=3,column=1,sticky=W,padx=10,pady=10)
b.bind('<Double-Button-1>',doubleclick)

window.mainloop()