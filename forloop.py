#Write a program to calculate the sum of whole numbers
num=int(input("Enter a number till where you want to find the sum: "))
sum=0
for i in range(0,num+1):
    sum=sum+i
    print("The Sum is:", sum)
#Reverse a string
str1=input("Enter a string.:")
str2=""
for i in str1:
    str2=i+str2

print("Original string:", str1)
print("Reversed string:", str2)
#Write a program to print the numbers in reverse order beginning from the number entered by the user.
num2=int(input("Enter a number: "))
for i in range(num2,0-1):
    print(i)
#Write a python program for printing the table of any number (1-10), using the for loop
num3=int(input("Enter a number: "))
for i in range(1,25):
    print(num3,'x',i,'=',num3*i)

