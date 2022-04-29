from tkinter import *
window=Tk()
window.geometry('300x300')
L1=Label(window,text='write whats in ur mind!!!',fg='blue').place(anchor=NW)
B1=Button(window,text='',bg='green').pack(fill=X,expand=True,pady=2)
B2=Button(window,text='clickme!',fg='green',bg='yellow').place(in_=B1,relx=0.5,rely=0.5,anchor=CENTER)

window.mainloop()