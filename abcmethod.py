from abc import ABC, abstractmethod
class abstract(ABC):
    def print(self, printer):
        print("The passed value is:", printer)

    @abstractmethod

    def task(self):
        print("We are inside the abstract task")

class testclass(abstract):
    def task(self):
        print("We are inside testclass task")
#working

testobject=testclass()
testobject.task()
testobject.print(150)

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can slither")

class Dog(Animal):
    def move(self):
        print("I can walk on four legs")

class Lion(Animal):
    def move(self):
        print("I can walk like a dog")

ob=Human()
ob.move()
ob2=Snake()
ob2.move()
ob3=Dog()
ob3.move()
ob4=Lion()
ob4.move()

class India:
    def capital(self):
        print("The capital of India is New Delhi")

    def language(self):
        print("India has a lot of languages, like Gujarati and Hindi")

    def type(self):
        print("India is a Southasian country")

class USA:
    def capital(self):
        print("The capital of the US is Washington D.C.")
    def language(self):
        print("The US's official language is English")
    def type(self):
        print("The US is a North American country")

ob5=India()
ob6=USA()
for i in (ob5, ob6):
    i.capital()
    i.language()
    i.type()







