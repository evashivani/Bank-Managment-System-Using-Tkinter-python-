import re
import mysql.connector as d
from tkinter import *
from tkinter import messagebox
def submit_btn():
    name=Username.get()
    passw=password1.get()
    age=Age.get()
    email=Email.get()
    address=Address.get()
    account=AccountNumber.get()
    contact=ContactNumber.get()
    amount=Amount.get()
    #print(f"The name entered by you is {name} {passw} {age} {email} {address} {account} {contact} {amount}")
    if name=='' or passw=='' or age=='' or email=='' or address=='' or account=='' or contact=='' or amount=='':
        messagebox.showerror('error','All fields required!!')
        validate_password(passw)
        validate_age(age)
        validate_email(email)
        validate_account(account)
        validate_contact(contact)
        validate_amount(amount)
    openacc(name,passw,age,email,address,account,contact,amount)
def validate_password(passw):
    special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']',
                  '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']
    msg=''
    if len(passw)>8:
        msg='password length should not be greater than 8'
    else:
        try:
            if not any(i in special_ch for i in passw):
                msg='should contain any one special character'
            elif not any(i.isdigit() for i in passw):
                msg='should contain atleast one digit'
            elif not any(i.isUpper() for i in passw):
                msg='should contain atleast one upper case letter'
            else:
                msg='success'
        except Exception as es:
            messagebox.showerror('error',es)
    messagebox.showinfo('success',msg)

def validate_age(age):
    if age.isdigit():
        age=Age.get()
    else:
        messagebox.showerror('error','Age must be an integer')

def validate_email(email):
    if re.findall("@",email) and re.findall(".com",email):
        email=Email.get()
    else:
        messagebox.showerror('error','invalid email')
def validate_account(account):
    if account.isdigit():
        account=AccountNumber.get()
    else:
        messagebox.showerror('error', 'AccountNumber must be an integer')
def validate_contact(contact):
    msg=''
    if all(i.isdigit() for i in contact):
        if len(contact) == 10:
           # mob = int(contact)
            msg = 'success'
            messagebox.showinfo('success',msg)
        else:
            messagebox.showerror('error', 'ContactNumber must be an integer')
    # if contact.isdigit():
    #   contact=ContactNumber.get()
def validate_amount(amount):
    if amount.isdigit():
        amount=Amount.get()
    else:
        messagebox.showerror('error', 'Amount must be an integer')
def openacc(name,passw,age,email,address,account,contact,amount):
    con=d.connect(host='localhost', user='root', password='0000', db='mybank')
    cursor=con.cursor()
    query = "insert into datainfo(name,passw,age,email,address,account,contact,amount) values ('{}','{}',{},'{}','{}',{},{},{})".format(name,passw, age, email,address,account,contact,amount)
    cursor.execute(query)
    con.commit()
    print('data entered successfully')
    messagebox.showinfo('success','Data entered successfully')
    Username.delete(0,END)
    password1.delete(0, END)
    Age.delete(0, END)
    Email.delete(0, END)
    Address.delete(0, END)
    AccountNumber.delete(0, END)
    ContactNumber.delete(0, END)
    Amount.delete(0, END)
    Username.focus_set()

def previouspage():
    window.destroy()
    import SignUp
def nextpage():
    window.destroy()
    import Menu
#def reset():
   # Username.set(' ')
window=Tk()
window.title('Open Account')
window.geometry('450x450')
window.configure(bg='black')
l=Label(window,text='Welcome to Bank Management System',fg='black',bg='pink')
l.grid(row=0,column=1,sticky=W,pady=10,padx=10)
l1=Label(window,text='UserName',fg='black')
l1.grid(row=1,column=0,sticky=W,padx=10,pady=10)
l2=Label(window,text='Password',fg='black')
l2.grid(row=2,column=0,sticky=W,padx=10,pady=10)
l3=Label(window,text='Age',fg='black')
l3.grid(row=3,column=0,sticky=W,padx=10,pady=10)
l4=Label(window,text='Email',fg='black')
l4.grid(row=4,column=0,sticky=W,padx=10,pady=10)
l5=Label(window,text='Address',fg='black')
l5.grid(row=5,column=0,sticky=W,padx=10,pady=10)
l6=Label(window,text='AccountNumber',fg='black')
l6.grid(row=6,column=0,sticky=W,padx=10,pady=10)
l7=Label(window,text='ContactNumber',fg='black')
l7.grid(row=7,column=0,sticky=W,padx=10,pady=10)
l8=Label(window,text='Amount',fg='black')
l8.grid(row=8,column=0,sticky=W,padx=10,pady=10)

Username=Entry(window,bg='yellow',fg='green')
Username.grid(row=1,column=1,sticky=W,pady=10,padx=10)
password1=Entry(window,bg='yellow',fg='green',show='*')
password1.grid(row=2,column=1,sticky=W,pady=10,padx=10)
Age=Entry(window,bg='yellow',fg='green')
Age.grid(row=3,column=1,sticky=W,pady=10,padx=10)
Email=Entry(window,bg='yellow',fg='green')
Email.grid(row=4,column=1,sticky=W,pady=10,padx=10)
Address=Entry(window,bg='yellow',fg='green')
Address.grid(row=5,column=1,sticky=W,pady=10,padx=10)
AccountNumber=Entry(window,bg='yellow',fg='green')
AccountNumber.grid(row=6,column=1,sticky=W,pady=10,padx=10)
ContactNumber=Entry(window,bg='yellow',fg='green')
ContactNumber.grid(row=7,column=1,sticky=W,pady=10,padx=10)
Amount=Entry(window,bg='yellow',fg='green')
Amount.grid(row=8,column=1,sticky=W,pady=10,padx=10)

b=Button(window,text='Create Account',bg='White',fg='Blue',command=submit_btn)
b.grid(row=9,column=0,sticky=E,padx=10,pady=10)
b_pp=Button(window,text='Previous Page',bg='White',fg='Blue',command=previouspage)
b_pp.grid(row=9,column=1,sticky=E,padx=10,pady=10)
b_np=Button(window,text='Next Page',bg='White',fg='Blue',command=nextpage)
b_np.grid(row=9,column=2,sticky=E,padx=10,pady=10)
#b_reset=Button(window,text='Reset',bg='White',fg='Blue',command=reset)
#b_reset.grid(row=10,column=0,sticky=W,padx=10,pady=10)

window.mainloop()