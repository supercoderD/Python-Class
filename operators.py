a=80-70
b=10+35
c=b-a+9

if a and b and c:
    print("All the numbers have a boolean value as True")
else:
    print("At least one number has a boolean value as false.")

d=6
e=-8
f=100
if d > 0 or e > 0:
    print("Either of the number is greater than 0")
else: 
    print("No number is greater than 0")
if e > 0 or f > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

#BMI checker
height= float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kg: "))
BMI= weight / height**2
print("Your BMI is", BMI)
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9: 
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severly overweight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are severly obese.")


    