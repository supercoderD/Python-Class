# #Write to check a number is divisible by another number.
# numerator=int(input("Enter a numerator: "))
# denominator=int(input("Enter a denominator: "))
# fraction=numerator % denominator 
# if fraction==0:
#     print( numerator, "is divisible by", denominator)
# else:
#     print( numerator, "is not divisible by", denominator)



#Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?
a=10
b=20
c=30
d=3
average=(a+b+c)//d
if a<average and b<average and c<average:
    print("All three cyclists are driving below average speed.")
elif a<average and b<average:
    print("Cyclists a and b are riding below average")
elif b<average and c<average:
    print("Cyclists b and c are riding below average")
elif a<average and c<average:
    print("Cyclists a and c are riding below average")
elif a<average:
    print("Cyclist a is riding below average")
elif b<average: 
    print("Cyclists b is riding below average")
elif c<average:
    print("Cyclist c is riding below average")
else: 
    print("All three cyclists are on or above average")



