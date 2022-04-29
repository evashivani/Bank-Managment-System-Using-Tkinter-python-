import mysql.connector as d
from tkinter import *
from tkinter import messagebox
def AccClose():
    age=Age.get()
    close(age)
def close(age):
    con=d.connect(host='localhost',user='root',password='0000',database='mybank')
    cursor=con.cursor()
    query="delete from datainfo where age={}".format(age)
    cursor.execute(query)
    con.commit()
    messagebox.showinfo('info','Account deleted successfully')
    Age.delete(0,END)
    Age.focus_set()
def previouspage():
    window.destroy()
    import Menu
def nextpage():
    window.destroy()
    import page6

window=Tk()
window.title('Account Close')
window.geometry('350x200')
window.configure(bg='black')
l=Label(window,text='Welcome to Bank Management System',fg='black',bg='pink')
l.grid(row=0,column=1,sticky=W,pady=10,padx=10)
l1=Label(window,text='Age',fg='black')
l1.grid(row=1,column=0,sticky=W,padx=10,pady=10)
Age=Entry(window,bg='yellow',fg='green')
Age.grid(row=1,column=1,sticky=W,pady=10,padx=10)

b=Button(window,text='Account Close',bg='White',fg='Blue',command=AccClose)
b.grid(row=2,column=0,sticky=E,padx=10,pady=10)
b_pp = Button(window,text='Previous Page',bg='White',fg='Blue',command=previouspage)
b_pp.grid(row=2,column=1,sticky=E,padx=10,pady=10)
b_np = Button(window,text='Next Page',bg='White',fg='Blue',command=nextpage)
b_np.grid(row=2,column=2,sticky=E,padx=10,pady=10)
window.mainloop()