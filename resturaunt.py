import tkinter as tk
from tkinter import ttk, messagebox
class RestaurantOrderManagement:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Management App")
        self.menuitems={
        "French Fries All Saucy Meal(includes 2x as much as the ones with the pizza meal)":10,
        "All You Can Eat Buffet(varies as your preference)": 20.99,
        "Creamy, Delicious Burger(4 burgers of your choice)": 15.99,
        "Pizza Meal(includes French Fries and ketchup as a side)": 27.99,
        "Saucy, Creamy Garlic Pasta(includes creamy pesto and marinara,topped with cheese and garlic)": 21.99,
        "Drinks(includes all sodas and lemonade; free refills)": 1}

        self.exchangerate=94
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,
                  text="Resaurant Order Management",
                  font=("Times",20,"extra-bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menulabels={}
        self.menuquantities={}
        for i,(item,price) in enumerate(self.menuitems.items(),start=1):
            label=ttk.label(frame,text=f"{item}(${price}):",font=("Times",12))
            label.grid(row=1,column=0,padx=10,pady=5)
            self.menulabels[item]=label
            quantityentry=ttk.Entry(frame,width=5)
            quantityentry.grid(row=1,column=1,padx=10,pady=5)
            self.menuquantities[item]=quantityentry
        self.currencyvar=tk.StringVar()
        ttk.Label(frame,text="Currency:",font=("Times",12)).grid(row=len(self.menuitems)+1,column=0,padx=10,pady=5)
        currencydropdown=ttk.Combobox(frame,textvariable=self.currencyvar,state="readonly",width=18,values=("USD","INR"))
        currencydropdown.grid(row=len(self.menuitems)+1,column=1,padx=10,pady=5)
        currencydropdown.current(0)
        self.currencyvar.trace("w",self.updatemenuprices)
        orderbutton=ttk.Button(frame,text="Place Order",command=self.placeorder)
        orderbutton.grid(row=len(self.menuitems)+2,columnspan=3,padx=10,pady=10)
    def updatemenuprices(self,*args):
        currency=self.currencyvar.get()
        symbol="₹" if currency =="INR" else "$"
        rate=self.exchangerate if currency=="INR" else 1
        for item, label in self.menulabels.items():
            price=self.menuitems[item]*rate
            label.config(text=f"{item}({symbol}{price}):")
    def placeorder(self):
        totalcost=0
       
        
