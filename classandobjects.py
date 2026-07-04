# class student:
#     grade=10
#     print("Hi I am a student of grade", grade)

# object=student()

class Vehicle:

    def __init__(self, maxspeed, mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage

modelx=Vehicle(240,10)
modely=Vehicle(370, 0)
print("Model Max Speed: ", modelx.maxspeed)
print("Model Mileage: ", modelx.mileage)
print("Model Y Max Speed", modely.maxspeed)

#Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well

class Parrot:
    species="bird"
    def __init__(self, name, age):
        self.name=name
        self.age=age

p1=Parrot("Chirp", 7)
p2=Parrot("Talkative", 9)

print("Parrot is a", p1.species)
print("I have a parrot named",p1.name,"and his age is", p1.age )
        

    


    