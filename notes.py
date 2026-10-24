from tkinter import *
from tkinter import messagebox
# from PIL import Image, ImageTk
root=Tk()
root.title("Denominaton Counter")
root.configure(bg="light blue")
root.geometry("600x400")
label=Label(root,text="Hey, User! Welcome to the Brand-New Denomination Counter Application, where any amounts of currency are broken down for you.")
bg="light blue"
label.place(relx=0.5, y=340,anchor=CENTER)
def message():
    Messagebox=messagebox.showinfo("Alert", "Would you like to proceed to the denomination counter application? Private information may be have to be given in order to calcualte an amount.")
    if Messagebox=="ok":
        topwin()

button=Button(root,text="Proceed.",command=message,bg="red",fg="white")
button.place(x=260,y=360)
def topwin():
    top=Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light brown")
    top.geometry("600x350+50+50")
    label2=Label(top,text="Enter total amount", bg="light brown")
    entry=Entry(top)
    lbl=Label(top,text="Here are the number of notes for each denomination.",bg="light brown")
    
    l1=Label(top,text="100",bg="light brown")
    l2=Label(top,text="50",bg="light brown")
    l3=Label(top,text="20",bg="light brown")
    l4=Label(top,text="10",bg="light brown")
    l5=Label(top,text="5",bg="light brown")
    l6=Label(top,text="2",bg="light brown")
    l7=Label(top,text="1",bg="light brown")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    t4=Entry(top)
    t5=Entry(top)
    t6=Entry(top)
    t7=Entry(top)
    def calculator():
        try:
            amount=int(entry.get())
            note100=amount//100
            amount%=100
            note50=amount//50
            amount%=50
            note20=amount//20
            amount%=20
            note10=amount//10
            amount%=10
            note5=amount//5
            mount%=5
            note2=amount//2
            amount%=2
            note1=amount//1
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)
            t5.delete(0,END)
            t6.delete(0,END)
            t7.delete(0,END)
            t1.insert(END,str(note100))
            t2.insert(END,str(note50))
            t3.insert(END,str(note20))
            t4.insert(END,str(note10))
            t5.insert(END,str(note5))
            t6.insert(END,str(note2))
            t7.insert(END,str(note1))
        except ValueError:
            messagebox.showerror("Error","Invalid character(s) have been inserted into this response. Remove all invalid character(s) and replace with valid ones.")
        button2=Button(top,text="Calculate",command=calculator,bg="gray",fg="white")
        label2.place(x=230,y=50)
        entry.place(x=200,y=80)
        button2.place(x=240,y=120)
        lbl.place(x=140,y=170)
        l1.place(x=180,y=200)
        l2.place(x=180,y=230)
        l3.place(x=180,y=260)
        l4.place(x=180,y=290)
        l5.place(x=180,y=320)
        l6.place(x=180,y=350)
        l7.place(x=180,y=380)
        t1.place(x=270,y=200)
        t2.place(x=270,y=230)
        t3.place(x=270,y=260)
        t4.place(x=270,y=290)
        t5.place(x=270,y=320)
        t6.place(x=270,y=350)
        t7.place(x=270,y=380)
        top.mainloop()

root.mainloop()
           


            
