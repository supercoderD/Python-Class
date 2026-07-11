#Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.
class IOString():

    def __init__(self):
        self.str1=""


    def getstring(self):
        self.str1=input("Enter a string: ")


    def printstring(self):
        print("Result is:", self.str1.upper())


str1=IOString()

str1.getstring()
str1.printstring()

class Employee:

    def __init__(self):
        print("Employee created")
    

    def __del__(self):
        print("Destructor called")


def CREATEOBJ():
    print("Making object...")
    obj=Employee()
    print("Function end...")
    return obj

print("Calling CREATEOBJ() function...")
obj=CREATEOBJ()
print("Program End...") 

class pair():
    def twoSum(self, nums, target):
        lookup={}

        for i, num in enumerate(nums):
            if target-num in lookup:
                return (lookup[target-num], i)
            lookup[num]=i


value=int(input("Enter sum for which you want to amke this search:"))
print("index1=%d, index2=%d"%pair().twoSum((100,200,300,400,500,600,700), value))

      
