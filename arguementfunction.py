#Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
# def totalcalc(billamount,tipperc=15):
#     #define functiont to calcuate the tip on bill
#     tip=billamount*(tipperc/100)
#     total=billamount+tip
#     print(f"Please pay ${total}")


# #specify only bill amount and defualt value of tip percentage is used
# bill=float(input("Enter bill amount: "))
# totalcalc(bill)
# #define funcgtion to calculate cube
# def cube(number):
#     return number**3


# #define a function which will exectue cube function if the user entered number is divisible by three
# def bythree(number):
#     if number %3==0:
#         return cube(number)
#     else:
#         return False
# #display result
# print(bythree(9))


def factorial(x):
    '''this is a recursive functin to find the factorial of an integer'''
    
    if x==0 or x==1:
        return 1
    else:
        #calling function inside a function
        return x*factorial(x-1)
#display result
print(factorial.__doc__)
factorialuserinput=int(input("Enter the amount for the factorial: "))
print("The factorial of", factorialuserinput, "is", factorial(factorialuserinput))