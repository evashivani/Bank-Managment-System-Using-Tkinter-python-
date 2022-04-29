import mysql.connector as d
from tkinter import *
from tkinter import messagebox
def withdrawl():
    name=Name.get()
    amount=Amount.get()
    withdrawl=WithdrawlAmount.get()
    if (name == '') or (amount == '') or (withdrawl == ''):
        messagebox.showerror('error','All fields required!!')
    withdrawl=int(amount)-int(withdrawl)
    updateacc(name, amount, withdrawl)
def updateacc(name,amount,withdrawl):
    con=d.connect(host='localhost',user='root',password='0000',database='mybank')
    cur=con.cursor()
    cur.execute("update datainfo set updated_amount={} where name='{}' and amount={}".format(withdrawl,name,amount))
    con.commit()
    messagebox.showinfo('success', 'Cash Withdrawl Successfully')
    Name.delete(0,END)
    Amount.delete(0,END)
    WithdrawlAmount.delete(0,END)
    Name.focus_set()
def previouspage():
    window.destroy()
    import Menu
def nextpage():
    window.destroy()
    import page5

window=Tk()
window.title('Cash Withdrawl')
window.geometry('480x350')
window.configure(bg='black')
l=Label(window,text='Welcome to Bank Management System',fg='black',bg='pink')
l.grid(row=0,column=0,sticky=W,pady=10,padx=10)
l1=Label(window,text='Name',fg='black')
l1.grid(row=1,column=0,pady=10,padx=10,sticky=W)
l2=Label(window,text="Amount",fg='black')
l2.grid(row=2,column=0,sticky=W,pady=10,padx=10)
l3=Label(window,text="Withdrawl Amount",fg='black')
l3.grid(row=3,column=0,sticky=W,pady=10,padx=10)
Name=Entry(window,fg='green',bg='yellow')
Name.grid(row=1,column=1,sticky=W,padx=10,pady=10)
Amount=Entry(window,fg='green',bg='yellow')
Amount.grid(row=2,column=1,sticky=W,padx=10,pady=10)
WithdrawlAmount=Entry(window,fg='green',bg='yellow')
WithdrawlAmount.grid(row=3,column=1,sticky=W,padx=10,pady=10)
b=Button(window,text='Cash Withdrawl',bg='White',fg='Blue',command=withdrawl)
b.grid(row=4,column=0,sticky=E,padx=10,pady=10)
b_pp = Button(window,text='Previous Page',bg='White',fg='Blue',command=previouspage)
b_pp.grid(row=4,column=1,sticky=E,padx=10,pady=10)
b_np = Button(window,text='Next Page',bg='White',fg='Blue',command=nextpage)
b_np.grid(row=4,column=2,sticky=E,padx=10,pady=10)
window.mainloop()