from tkinter import *
window=Tk()
window.configure(background='grey')
window.geometry('250x250')
def clickMe():
    box=text_box.get("1.0")
    print(box)
text_box=Text(window,bg='white',fg='green')
text_box.place(anchor=NW,relx=0.5,rely=0.5)
button=Button(window,bg='yellow',fg='blue',command=lambda:clickMe())
button.pack(fill=X,expand=True)
window.mainloop()