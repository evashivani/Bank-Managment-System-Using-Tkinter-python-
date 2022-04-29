from tkinter import *
from tkinter import messagebox
def Exit():
    a=messagebox.askyesno("show_warning","Are you sure you want to exit!!")
    if a==True:
        window.destroy()
        import SignUp
def previouspage():
    window.destroy()
    import page5
window=Tk()
window.title('Exit')
window.geometry('350x350')
window.configure(bg='black')
l=Label(window,text='Welcome to Bank Management System',fg='black',bg='pink')
l.grid(row=0,column=0,sticky=W,pady=10,padx=10)
l1=Label(window,text='Thanks for your concern!!!',fg='black',bg='yellow')
l1.grid(row=1,column=0,sticky=W,padx=10,pady=10)

b=Button(window,text='Exit',bg='White',fg='Blue',command=Exit)
b.grid(row=2,column=0,sticky=E,padx=10,pady=10)
b_pp = Button(window,text='Previous Page',bg='White',fg='Blue',command=previouspage)
b_pp.grid(row=2,column=1,sticky=E,padx=10,pady=10)

window.mainloop()