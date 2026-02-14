#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
medicalcause=input("Do you have a medical cause: ")
attendence=int(input("What is your attendance?"))
if medicalcause=="yes" or medicalcause=="y":
    print("Allowed")
else:
    
    if attendence>75:
        print("You are allowed into the test")
    else:
        print("You are not allowed in the test.")



units=int(input("Enter the amount of units: "))
if units<50:
    amount=units*2.6
    tax=25
elif units<=100:
    amount=3.25*(50*2.6)+(units-50)
elif units<=200:
    amount=(50*2.6)+(units-50)*5.26
    tax=45
else:
    amount=(50*2.6)+(50*3.25)+(100*5.26)+(units-200)*8.45
    tax=75


totalbill=amount+tax
print("The total bill is", totalbill)






