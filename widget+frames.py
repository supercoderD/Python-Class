# from tkinter import *
# root=Tk()
# root.title("Login App")
# root.geometry("400x400")
# frame=Frame(master=root, height=200, width=360,bg="#F0FD04")
# label1=Label(frame, text="Full Name", bg="#f74504",fg="white", width=12)
# label2=Label(frame,text="Email Address", bg="#03fc03",fg="white",width=12)
# label3=Label(frame,text="Enter Password", bg="#03daf7",fg="white",width=12)
# nameentry=Entry(frame)
# emailentry=Entry(frame)
# passentry=Entry(frame,show="*")
# def display():
#     name=nameentry.get()
#     greet="Hello"+name
#     message= "\nCongratulations on your new account! We will send you all the details needed for your new account @", emailentry
#     textbox.insert(END,greet)
#     textbox.insert(END,message)

# textbox=Text(bg="#063BFD")
# button1=Button(text="Create Account",command=display,bg="red")
# frame.place(x=20,y=0)
# label1.place(x=20,y=20)
# nameentry.place(x=150,y=20)
# label2.place(x=20,y=80)
# emailentry.place(x=150,y=80)
# label3.place(x=20,y=140)
# passentry.place(x=150,y=140)
# button1.place(x=130,y=210)
# textbox.place(y=250)

# root.mainloop()

from tkinter import *
root=Tk()
root.title("Number Pad")
root.geometry("250x250")
nums=[[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
for i in range(4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        frame=Frame(master=root,relief=SUNKEN,borderwidth=1)
        frame.grid(row=i,column=j)
        label=Label(master=frame,text=nums[i][j],bg="#04c9fa")
        label.pack(padx=3,pady=3)

root.mainloop()
