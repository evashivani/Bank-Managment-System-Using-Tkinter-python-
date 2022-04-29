from tkinter import *
import mysql.connector as d
from tkinter import messagebox
def reset():
    if user.get() == "":
        messagebox.showerror('error','All fields are required!!')
    else:
        try:
            con=d.connect(host='localhost',user='root',password='0000',database='mybank')
            cur=con.cursor()
            cur.execute("select * from datainfo where name=%s",(user.get(),))
            data=cur.fetchone()
            print(data)
            if data == None:
                messagebox.showerror('error','plz enter valid username')

            else:
                cur.execute("update datainfo set passw=%s where name=%s",(newpass.get(),user.get()))
                messagebox.showinfo('success','Password has been reset..now login with new password!!')
                con.commit()
                window.destroy()
                import SignUp
        except Exception as es:
            messagebox.showerror('error',f'Invalid {str(es)}',parent=window)


window=Tk()
window.configure(bg='Black')
window.title('Home Page')
window.geometry('350x350')

l=Label(window,text='Welcome to Bank Management System',fg='black',bg='pink')
l.grid(row=0,column=1,sticky=W,pady=10,padx=10)
l1=Label(window,text='UserName',fg='black',bg='pink')
l1.grid(row=1,column=0,sticky=W,pady=10,padx=10)
l2=Label(window,text='New Password',fg='black')
l2.grid(row=2,column=0,sticky=W,pady=10,padx=10)
user=Entry(window,fg="black",bg="yellow")
user.grid(row=1,column=1,sticky=W,pady=10,padx=10)
newpass=Entry(window,fg="black",bg="yellow")
newpass.grid(row=2,column=1,sticky=W,pady=10,padx=10)


# Create button, it will change label text
b1=Button(window, text="Reset", background='yellow',command=reset)
b1.grid(row=3,column=0,sticky=W,padx=10,pady=10)


window.mainloop()