import mysql.connector as d
from tkinter import *
from tkinter import messagebox
def deposit():
    name1 = Username.get()
    updated_amount = UpdateAmount.get()
    amount1=Amount.get()
    if name1=="" or updated_amount=="" or amount1=="":
        messagebox.showerror('error','All fields required!!')
    updated_amount=int(amount1)+int(updated_amount)
    updateacc(name1, amount1,updated_amount)

def updateacc(name1, amount1,updated_amount):
    try:
        con = d.connect(host='localhost', user='root', password='0000', db='mybank')
        cursor = con.cursor()
        query = "update datainfo set updated_amount={} where name='{}' and amount={}".format(updated_amount,name1,amount1)
        messagebox.showinfo('success','Cash Deposited Successfully')
        cursor.execute(query)
        con.commit()

    except Exception as es:
        print(es)
    Username.delete(0,END)
    Amount.delete(0,END)
    UpdateAmount.delete(0,END)
    Username.focus_set()
def previouspage():
    window.destroy()
    import Menu
def nextpage():
    window.destroy()
    import page3

window=Tk()
window.title('Cash Deposit')
window.geometry('480x350')
window.configure(bg='black')
l=Label(window,text='Welcome to Bank Management System',fg='black',bg='pink')
l.grid(row=0,column=1,sticky=E,pady=10,padx=10)
l1=Label(window,text='UserName',fg='black')
l1.grid(row=1,column=0,sticky=W,padx=10,pady=10)
l2=Label(window,text='Amount',fg='black')
l2.grid(row=2,column=0,sticky=W,padx=10,pady=10)
l3=Label(window,text='Update Amount',fg='black')
l3.grid(row=3,column=0,sticky=W,padx=10,pady=10)
Username=Entry(window,bg='yellow',fg='black')
Username.grid(row=1,column=1,sticky=W,pady=10,padx=10)
Amount=Entry(window,bg='yellow',fg='green')
Amount.grid(row=2,column=1,sticky=W,pady=10,padx=10)
UpdateAmount=Entry(window,bg='yellow',fg='green')
UpdateAmount.grid(row=3,column=1,sticky=W,pady=10,padx=10)
b=Button(window,text='Cash Deposit',bg='White',fg='Blue',command=deposit)
b.grid(row=4,column=0,sticky=W,padx=10,pady=10)
b_pp = Button(window,text='Previous Page',bg='White',fg='Blue',command=previouspage)
b_pp.grid(row=4,column=1,sticky=W,padx=10,pady=10)
b_np=Button(window,text='Next Page',bg='White',fg='Blue',command=nextpage)
b_np.grid(row=4,column=2,sticky=W,padx=10,pady=10)
window.mainloop()