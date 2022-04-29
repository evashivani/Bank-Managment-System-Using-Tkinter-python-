import mysql.connector as d
from tkinter import *
from tkinter import ttk, messagebox
def GetValue(event):
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0,END)
    e6.delete(0, END)
    e7.delete(0, END)

    row_id=listbox.selection()[0]
    select=listbox.set(row_id)
    e1.insert(0,select['UserName'])
    e2.insert(0, select['Password'])
    e3.insert(0, select['Age'])
    e4.insert(0,select['Email'])
    e5.insert(0, select['Address'])
    e6.insert(0, select['Account'])
   # e7.insert(0, select['Contact'])

def Add():
    user=e1.get()
    passw=e2.get()
    age=e3.get()
    email=e4.get()
    address=e5.get()
    account=e6.get()
    contact=e7.get()
    amount=e8.get()

    try:
        con = d.connect(host='localhost',user="root",password='0000',database='mybank')
        cursor = con.cursor()
        query = "insert into datainfo(name,passw,age,email,address,account,contact,amount) values('{}','{}',{},'{}','{}',{},{},{})".format(user,passw,age,email,address,account,contact,amount)
        cursor.execute(query)
        con.commit()
        messagebox.showinfo('info','record inserted successfully')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0,END)
        e1.focus_set()

    except Exception as es:
        print(es)

def Show():
    con = d.connect(host='localhost', user='root', password='0000', database='mybank')
    cursor = con.cursor()
    cursor.execute("select name,passw,age,email,address,account from datainfo")
    data1 = cursor.fetchall()
    print(data1)

    for i,(name,passw,age,email,address,account) in enumerate(data1,start=1):
        listbox.insert("", "end", values=(name,passw,age,email,address,account))

def Update():
    user = e1.get()
    passw = e2.get()
    age = e3.get()
    email = e4.get()
    address = e5.get()
    account = e6.get()
    contact = e7.get()
    amount = e8.get()

    try:
        con = d.connect(host='localhost', user="root", password='0000', database='mybank')
        cursor = con.cursor()
        query1 ="update datainfo set passw='{}',age={},email='{}',address='{}',account={} where name='{}'".format(passw,age,email,address,account,user)
        cursor.execute(query1)
        con.commit()
        messagebox.showinfo('info', 'record updated successfully')
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e1.focus_set()

    except Exception as es:
        print(es)


def Delete():
    user=e1.get()
    try:
        con = d.connect(host='localhost', user='root', password='0000', database='mybank')
        cursor = con.cursor()
        query = "Delete from datainfo where name= '{}'".format(user)
        cursor.execute(query)
        con.commit()
        #lastid = cursor.lastrowid
        messagebox.showinfo('info', 'record deleted successfully')
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)

        e1.focus_set()
    except Exception as es:
        print(es)
        #con.rollback()
        #con.close()

def nextpage():
    window.destroy()
    import SignUp

window=Tk()
window.title('Account details')
window.geometry('2000x1000')
window.configure(bg='black')
global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8
l=Label(window,text='Welcome to Bank Management System',fg='black',bg='pink')
l.place(x=400,y=5)
l1=Label(window,text='UserName',fg='black')
l1.place(x=10,y=10)
l2=Label(window,text='Password',fg='black')
l2.place(x=10,y=40)
l3=Label(window,text='Age',fg='black')
l3.place(x=10,y=70)
l4=Label(window,text='Email',fg='black')
l4.place(x=10,y=100)
l5=Label(window,text='Address',fg='black')
l5.place(x=10,y=130)
l6=Label(window,text='AccountNumber',fg='black')
l6.place(x=10,y=160)
l7=Label(window,text='ContactNumber',fg='black')
l7.place(x=10,y=190)
l8=Label(window,text='Amount',fg='black')
l8.place(x=10,y=220)


e1=Entry(window,bg='yellow',fg='green')
e1.place(x=140,y=10)
e2=Entry(window,bg='yellow',fg='green',show='*')
e2.place(x=140,y=40)
e3=Entry(window,bg='yellow',fg='green')
e3.place(x=140,y=70)
e4=Entry(window,bg='yellow',fg='green')
e4.place(x=140,y=100)
e5=Entry(window,bg='yellow',fg='green')
e5.place(x=140,y=130)
e6=Entry(window,bg='yellow',fg='green')
e6.place(x=140,y=160)
e7=Entry(window,bg='yellow',fg='green')
e7.place(x=140,y=190)
e8=Entry(window,bg='yellow',fg='green')
e8.place(x=140,y=220)

b=Button(window,text='Add',bg='White',fg='Blue',command=Add)
b.place(x=30,y=250)
b1=Button(window,text='update',bg='White',fg='Blue',command=Update)
b1.place(x=90,y=250)
b2=Button(window,text='Delete',bg='White',fg='Blue',command=Delete)
b2.place(x=160,y=250)
b_np=Button(window,text='Back',bg='White',fg='Blue',command=nextpage)
b_np.place(x=220,y=250)

cols=('UserName','Password','Age','Email','Address','Account')
listbox=ttk.Treeview(window,columns=cols,show='headings')
for x in cols:
    listbox.heading(x,text=x)
    listbox.place(x=40,y=350)
Show()
listbox.bind('<Double-Button-1>',GetValue)
window.mainloop()