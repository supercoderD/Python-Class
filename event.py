
window=Tk()
window.title("Event Handler")
window.geometry("100x100")
def handlekeypress(event):
    """Print the character associcated to the key pressed"""
    print(event.char)

window.bind("<Key>", handlekeypress)
def handleclick(event):
    print("\nThe button was clicked!")
button=Button(text="Click me!")
button.pack()
button. bind("<Button>",handleclick)

window.mainloop()
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x400")
def message():
    messagebox.showwarning("Warning", "Do not proceed with commands. This device has been infected with a viral disconnection.")
button=Button(root,text="Scan for Device Infections",command=message)
button.place(x=40,y=80)
root.mainloop
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Login System")
root.geometry("400x300")
tk.Label(root,text="Login System",font=("Drafting Mono",18,"bold")).pack(pady=15)
tk.Label(root,text="Username").pack()
username=tk.Entry(root)
username.pack()
tk.Label(root,text="Password").pack()
password=tk.Entry(root,show="*")
password.pack()
def login():
    if username.get()=="SpainwonFIFA" and password=="772":
        messagebox.showinfo("Success,Login sucessful! Press the x symbol on the top right hand corner to proceed onto the platform!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")
tk.Button(root,text="Login",command=login).pack(pady=15)
root.mainloop()