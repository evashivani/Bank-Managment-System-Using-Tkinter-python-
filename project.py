import mysql.connector as d
from tkinter import *

con=d.connect(host='localhost',user='root',password='0000',database='bankdata')
cursor=con.cursor()


if con.is_connected():
    print('connected successfully')
cursor = con.cursor()
print('Welcome to python bank')
print('Enter the choice')
while True:
    choice=input('1.Open Account \n 2.Cash Deposit\n 3.Cash Withdrawl\n 4.Account Details\n 5.Account close\n 6.exit')
    if choice == '1':
        name=input('Enter the Name')
        age=int(input('Enter the age'))
        amount=int(input('Enter the amount'))
        contact=int(input('Enter the Mobile Number'))
        query="insert into account values ('{}',{},{},{})".format(name,age,amount,contact)
        cursor.execute(query)
        con.commit()
        print('data entered successfully')
    elif choice=='2':
        name=input('Enter the name')
        amount=int(input('Enter the amount'))
        query="update account set amount={} where name='{}'".format(amount,name)
        cursor.execute(query)
        con.commit()
        print('data updated successfully')
    elif choice == '3':
        cash=int(input('Enter the cash to withdrawl'))
        amount=int(input('Enter the amount'))
        name=input('Enter the name')
        amount=amount-cash
        query="update account set name='{}' where amount={} ".format(name,amount)
        print(amount)
        cursor.execute(query)
        con.commit()

    elif choice=='4':
        name = input('Enter the name')
        query = "select name='{}' from account".format(name)
        cursor.execute(query)
        data1=cursor.fetchone()
        print(data1)

    elif choice=='5':
        name = input('Enter the name')
        query = "delete from account where name='{}'".format(name)
        if cursor.rowcount>0:
            print('Account deleted successfully')
        else:
            print('invalid input')
        cursor.execute(query)
        con.commit()

    elif choice=='6':
        print('Exit')
        break
window=Tk()
window.title('Bank Management System')
window.geometry('400x400')
window.configure(background='aqua')
l=Label(window,text='Bank Management System',bg='yellow',fg='blue',font='ariel 12 bold').grid(row=0,column=0,sticky=W)
window.mainloop()

------------------------------------------------------------

password validation
special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']

def validation():
    password = pwd.get()
    msg = "Turn off validation".

    if len(password) == 0:
        msg = 'Password can\'t be empty'
    else:
        try:
            if not any(ch in special_ch for ch in password):
                msg = 'Atleast 1 special character required!'
            elif not any(ch.isupper() for ch in password):
                msg = 'Atleast 1 uppercase character required!'
            elif not any(ch.islower() for ch in password):
                msg = 'Atleast 1 lowercase character required!'
            elif not any(ch.isdigit() for ch in password):
                msg = 'Atleast 1 number required!'
            elif len(password) < 8:
                msg = 'Password must be minimum of 8 characters!'
            else:
                msg = 'Success!'
        except Exception as ep:
            messagebox.showerror('error', ep)
    messagebox.showinfo('message', msg)


==============================================================

def mob_email_validation():
    special_ch = ['@', '.']
    msg = ''
    me = mob_email.get()
    if me == '':
        msg = 'provide Mobile num or Email'
    else:
        try:
            if any(ch.isdigit() for ch in me):
                if len(me) == 10:
                    mob = int(me)
                    msg = 'success'
                else:
                    msg = 'incorrect mobile number!'
            else:
                if not any(ch in special_ch for ch in me):
                    msg = 'incorrect email!'
                else:
                    msg = 'success!'
        except Exception as ep:
            msg = ep
    messagebox.showinfo('message', msg)






