# def well_wishes(name):
#     print("hello", name)
#     print("how are you")

# well_wishes("Ben")
# well_wishes("Rana")
#Calculator
def add(A,B):
    #This function is used for adding two numbers
    return A+B
def subtract(A,B):
    #This function is used for subtracting two numbers
    return A-B
def multiply(A,B):
    #This function is used for multiplying two numbers
    return A*B
def divide(A,B):
    #This function is used for dividing two numbers
    return A/B
#Now we will take inputs from the user
print("Please select the operation")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
useropearation=input("Select an opearation: ")
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number."))
if useropearation=="a":
    print("The sum of ", num1, "and", num2,"is:", add(num1, num2))
if useropearation=="b":
    print("The difference of ", num1, "and", num2,"is:", subtract(num1, num2))
if useropearation=="c":
    print("The product of ", num1, "and", num2,"is:", multiply(num1, num2))
if useropearation=="d":
    print("The quotient of ", num1, "and", num2,"is:", divide(num1, num2))
if useropearation!="a" or "b" or "c" or "d":
    print("This is an invalid input.")