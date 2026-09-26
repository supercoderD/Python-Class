from tkinter import *
from datetime import date
root=Tk()
root.title("Getting started with Widgets")
root.geometry("400x300")
Label1=Label(text="Hey, New User!", fg="white", bg="cyan", height=1,width=300, font=("Times",18))
Namelabel=Label(text="Please enter your full name",bg="#6AFF00",font=("Times,16"))
Nameentry=Entry(font=("Times,16"))
def display():
    name=Nameentry.get()
    global message
    message="Welcome to the Tkinter Application! Widgets are available now! \nToday's date is:"
    greet="Hello,"+name+"\n"
    textbox.insert(END,greet)
    textbox.insert(END,message)
    textbox.insert(END,date.today())

textbox=Text(height=3,font=("Times",18))
Button1=Button(text="Proceed",command=display,height=1,bg="#1532B3")
Label1.pack()
Namelabel.pack()
Nameentry.pack()
Button1.pack()
textbox.pack()
root.mainloop()

