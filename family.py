class FamilyMember:
    def __init__(self, eyecolor, heightin):
        self.eyecolor=eyecolor
        self.heightin=heightin

    def showtraits(self):
        print("Eye color:", self.eyecolor)
        print("Height (in)", self.heightin)
    
class Child(FamilyMember):
    def __init__(self, name, age, eyecolor, heightin):
        self.name=name
        self.age=age
        super().__init__(eyecolor, heightin)

    def showtraits(self):
        print("Name:", self.name)
        print("Age:",self.age)
        super().showtraits()
    def favoritehobby(self, hobby):
        print(self.name, "loves to", hobby)
    def favortiehobby2(self, hobby2):
        print(self.name, "also likes to", hobby2)

kid=Child("Darsh", 10, "black", 54)
kid.showtraits()
kid.favoritehobby("reading")
kid.favortiehobby2("writing")

print("Is Kid a sublcass of FamilyMember?", issubclass(Child,FamilyMember))
        




#Create a class Employee with the following: Attributes: name salary Methods: show_details() to display the employee's name and salary. Create a class Manager that inherits from Employee. Add an additional attribute: department Add a method:show_details() that prints all details. Create an object of Manager and display the employee details along with the department.

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def showdetails(self):
        print(self.name, "has a salary of", self.salary)
    
class Manager(Employee):
    def __init__(self,name, salary, department):
        self.department=department
        super().__init__(name, salary)
    def showdetails(self):
        super().showdetails()
        print(self.name, "works at",self.department)
ob1=Manager("Rahul", 100000, "IT")
ob1.showdetails()
    

       
