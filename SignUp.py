from tkinter import *
#from PIL import ImageTk
import mysql.connector as d
from tkinter import messagebox

def GetVal(event):
    messagebox.showinfo('info', 'enter registered username and password')
def visit():
     if user.get() == "admin" and passw.get() == "12345":
        messagebox.showinfo('success', 'welcome admin')
        window.destroy()
        import page4
def login():
    if user.get()=="" or passw.get()=="":
        messagebox.showerror('error','All fields are required!!',parent=window)
    else:
        try:
            con=d.connect(host='localhost',user='root',password='0000',database='mybank')
            cur=con.cursor()
            cur.execute("select * from datainfo where name=%s and passw=%s",(user.get(),passw.get()))
            row=cur.fetchone()
            if row==None:
               messagebox.showerror('error', 'Invalid Username and Password', parent=window)
            else:
                messagebox.showinfo('success', 'Welcome', parent=window)
                window.destroy()
                import Menu

        except Exception as es:
            messagebox.showerror("error", f"Error due to {str(es)}", parent=window)
            con.commit()
def nextpage():
    window.destroy()
    import login_page
def newpage():
    window.destroy()
    import newpage
window=Tk()
window.configure(bg='Black')
window.title('Home Page')
#window.geometry('1199x600+100+50')
window.geometry('350x350')
#window.resizable(false,false)
#bg=ImageTk.PhotoImage(file="C:/Users/punee/Pictures/Abstract1.jpg")
#bg_image=Label(window,image=bg).place(x=0,y=0,relheight=1,relwidth=1)
l=Label(window,text='Welcome to Bank Management System',fg='black',bg='pink')
l.grid(row=0,column=1,sticky=W,pady=10,padx=10)
l1=Label(window,text='UserName',fg='black',bg='pink')
l1.grid(row=1,column=0,sticky=W,pady=10,padx=10)
l2=Label(window,text='Password',fg='black',bg='pink')
l2.grid(row=2,column=0,sticky=W,pady=10,padx=10)

user=Entry(window,fg="black",bg="yellow")
user.grid(row=1,column=1,sticky=W,pady=10,padx=10)
passw=Entry(window,fg="black",bg="yellow")
passw.grid(row=2,column=1,sticky=W,pady=10,padx=10)

# Create button, it will change label text
b1=Button(window, text="Login", background='yellow',command=login)
b1.grid(row=3,column=0,sticky=W,padx=10,pady=10)
b2=Button(window, text="NewUser?? Create an account", background='yellow',command=nextpage)
b2.grid(row=3,column=1,sticky=W,padx=10,pady=10)
b3=Button(window,text='forget possword??',background='blue',fg='white',command=newpage)
b3.grid(row=4,column=1,sticky=E)
b4=Button(window,text='for admin only',background='orange',fg='white',command=visit)
b4.grid(row=5,column=0,sticky=W)
b4.bind('<Double-Button>',GetVal)

window.mainloop()