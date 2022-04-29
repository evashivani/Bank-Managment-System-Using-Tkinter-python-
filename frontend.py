from tkinter import *
import tkinter.messagebox
window = Tk()
window.title('myfirst_GUI')
window.configure(background='orange')
window.geometry('350x250')
define = StringVar()
my_dict={
    'Aparna':'IT','Sam':'Mechanical','pradum':'Computer Science','Richa':'Electrical'
}
def click():
    enter_text=t.get()
    #print(enter_text)
    output1.delete(0.0, END)
    try:
        define=my_dict[enter_text]
    except:
        define='Info Not Available'
    output1.insert(END,define)

def clr():
    define.set(' ')

def myfunc():
    print('hi hwkko')

#for menu without dropdown
my_menu=Menu(window)
my_menu.add_command(label='File',command=myfunc)
my_menu.add_command(label='Exit',command=quit)
window.config(menu=my_menu)

#for menu with dropdown
my_menu=Menu(window)

l1=Label(window,text = "Name",bg="White",fg="black",font='Ariel 12 bold')
l1.grid(row=0,column=0,sticky=W)
t=Entry(window,width=20,bg='white',fg='black')
t.grid(row=0,column=1,sticky=W)
b=Button(window,text='Submit',width='10',command=lambda:click(),bg='blue',fg='white')
b.grid(row=3,column=0,sticky=W,pady=10)
c=Button(window,text='Clear',width='10',command=clr,bg='green',fg='white')
c.grid(row=3,column=1,sticky=W,pady=10)
l2=Label(window,text='Definition',fg='black',font='none 12 bold')
l2.grid(row=4,column=0,sticky=W)
output1=Text(window,width=20,height=10,bg='grey',fg='black')
output1.grid(row=5,column=0,sticky=W)
#b.bind('<BUTTON-1>',click
window.mainloop()