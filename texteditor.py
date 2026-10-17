from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window=Tk()
window.title("The Brand New Text Editor!")
window.title("Now available on the Tkinter App on the New Iphone 18 and in Python in computers!")
window.geometry("700x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)
def openfile():
    """Open saved files to edit."""
    """Unsaved ones cannot be replaced back for editing.Press the 'Save As' button to save your documents for future editing."""
    filepath=askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    with open (filepath,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    window.title(f"Text Editor-{filepath}")

def savefile():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[("Text Files","*.txt"),("All Files", "*.*")],)
    if not filepath:
        return
    with open(filepath,"w") as output_file:
        text=txt_edit.get(1.0,END)
        output_file.write(text)
    window.title(f"Text Editor-{filepath}")

txt_edit=Text(window)
frbuttons=Frame(window,relief=RAISED,bd=10)
buttonopen=Button(frbuttons,text="Open File",command=openfile)
buttonsave=Button(frbuttons,text="Save As",command=savefile)
buttonopen.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
buttonsave.grid(row=1,column=0,stick="ew",padx=5)
frbuttons.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")
window.mainloop()


