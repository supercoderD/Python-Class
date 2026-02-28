# number=int(input("Enter a number: "))
# sum=0
# i=1
# while i<=number:
#     sum=sum+i
#     i=i+1

# print("\nSum=", sum)

# i=0
# while i<=0:
#     print("I WILL RUN FOREVER")

number2=int(input("Enter a three-digit number.: "))
#decide if a user-input number is an armstrong number or not
sum2=0
temp=number2
while temp > 0:
    digit=temp%10
    sum2+= digit**3
    temp//=10
if number2==sum2:
    print(number2,"is an armstrong number")
else:
    print(number2,"is not a armstrong number")