from tkinter import *
import mysql.connector as d
from tkinter import ttk, messagebox
def GetValue(event):
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    row_id=listbox.selection()[0]
    select=listbox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['stname'])
    e3.insert(0,select['course'])
    e4.insert(0,select['fee'])
def Add():
    stuid=e1.get()
    stuname=e2.get()
    course=e3.get()
    fee=e4.get()
    try:
        con=d.connect(host='localhost',user='root',password='0000',database='record')
        cursor=con.cursor()
        query="insert into table1(stuid,stuname,course,fee) values({},'{}', '{}' ,{})".format(stuid,stuname,course,fee)
        cursor.execute(query)
        con.commit()
       # lastid=cursor.lastrowid
        messagebox.showinfo('info','record inserted successfully')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e1.focus_set()
    except Exception as es:
        print(es)
        #con.rollback()
        con.close()
def show():
    con = d.connect(host='localhost', user='root', password='0000', database='record')
    cursor = con.cursor()
    query = "select * from table1"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)

    for i ,(stuid,stuname,course,fee) in enumerate(data,start=1):
        listbox.insert("","end",values=(stuid,stuname,course,fee))
        con.close()
def Update():
    stuid = e1.get()
    stuname = e2.get()
    course = e3.get()
    fee = e4.get()
    try:
        con = d.connect(host='localhost', user='root', password='0000', database='record')
        cursor = con.cursor()
        query = "update table1 set stuname='{}',course='{}',fee={} where stuid= {}".format(stuname,course,fee,stuid)
        cursor.execute(query)
        con.commit()
       # lastid = cursor.lastrowid
        messagebox.showinfo('info', 'record updated successfully')
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as es:
        print(es)
        #con.rollback()
        con.close()
def Delete():
    stuid = e1.get()
    try:
        con = d.connect(host='localhost', user='root', password='0000', database='record')
        cursor = con.cursor()
        query = "Delete from table1 where stuid= {}".format(stuid)
        cursor.execute(query)
        con.commit()
        #lastid = cursor.lastrowid
        messagebox.showinfo('info', 'record deleted successfully')
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as es:
        print(es)
        #con.rollback()
        con.close()
window=Tk()
window.configure(background='white')
window.geometry('1000x1000')
global e1
global e2
global e3
global e4
l=Label(window,text='Student Registration',font=('12'))
l.place(x=400,y=5)
l1=Label(window,text='student_id')
l1.place(x=10,y=10)
l2=Label(window,text='student_name')
l2.place(x=10,y=40)
l3=Label(window,text='course')
l3.place(x=10,y=70)
l4=Label(window,text='fee')
l4.place(x=10,y=100)

e1=Entry(window)
e1.place(x=140,y=10)
e2=Entry(window)
e2.place(x=140,y=40)
e3=Entry(window)
e3.place(x=140,y=70)
e4=Entry(window)
e4.place(x=140,y=100)

b=Button(window,text='Add',height=3,width=13,command=Add)
b.place(x=30,y=130)
b1=Button(window,text='Update',height=3,width=13,command=Update)
b1.place(x=120,y=130)
b2=Button(window,text='Delete',height=3,width=13,command=Delete)
b2.place(x=250,y=130)

cols=('id','stname','course','fee')
listbox=ttk.Treeview(window,columns=cols,show='headings')

for x in cols:
    listbox.heading(x,text=x)
    listbox.grid(row=1,column=0,columnspan=2)
    listbox.place(x=10,y=200)
show()
listbox.bind('<Double-Button-1>',GetValue)
window.mainloop()