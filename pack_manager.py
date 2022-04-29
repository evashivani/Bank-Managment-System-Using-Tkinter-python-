from tkinter import *
window=Tk()
pane = Frame(window)
def onclick(args):
    if args==1:
        print('Button 1 clicked')
    elif args==2:
        print('Button2 clicked')
pane.pack(fill = BOTH, expand = True)
l1=Text(pane,bg='yellow',fg='green').pack(fill=Y,expand=True)
b1=Button(pane,bg='blue',fg='yellow',text='SUBMIT',command=lambda:onclick(1)).pack(fill=BOTH,expand=True)
b2=Button(pane,bg='blue',fg='yellow',text='SUBMIT',command=lambda:onclick(2)).pack(fill=BOTH,expand=True)
pane.mainloop()