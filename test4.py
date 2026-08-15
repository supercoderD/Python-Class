class Book:
    isborrowed=False
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.isborrowed=False
    def borrow(self):
        if self.isborrowed==False:
            self.isborrowed=True
            print("This is a confomation message that you have borrowed a book.")
        else:
            print("Sorry, this book has already been borrowed by another user.")
   
    def returnbook(self):
        if self.isborrowed==True:
            self.isborrowed=False
            print(f"'{self.title}' has been returned")
        else:
            print("This book has not been borrowed.")

book1=Book("Harry Potter and the Sorceror's Stone", "J.K Rowling")
book1.borrow() 
book1.returnbook()
book2=Book("The Alien Attack", "Darsh Gandhi")
book2.borrow() 
book2.returnbook()
book3=Book("Middle School: Get me out of here!", "James Patterson")
book3.borrow() 
book3.returnbook()
