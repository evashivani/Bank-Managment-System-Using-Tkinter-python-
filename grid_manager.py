from tkinter import *
window=Tk()
window.geometry('350x200')
L1=Label(window,text='FirstName:',fg='red').grid(row=0,column=0,sticky=W)
L2=Label(window,text='SecondName:',fg='red').grid(row=1,column=0,sticky=W)
E1=Entry(window,fg='red',bg='yellow').grid(row=0,column=1,sticky=E,pady=2)
E2=Entry(window,fg='red',bg='yellow').grid(row=1,column=1,sticky=E,pady=2)
c=Checkbutton(window,bg='yellow',fg='blue',text='Click Me!!').grid(row=2,column=0,sticky=W)
B1=Button(window,bg='blue',fg='white',text='ZoomIn').grid(row=2,column=1,sticky=E)
B2=Button(window,bg='blue',fg='white',text='ZoomOut').grid(row=2,column=2,sticky=E)

window.mainloop()
