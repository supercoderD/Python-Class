#Write a program to check how many times a character is repeated in a word?
#Take input of a word
string=input("Please enter your own word: ")
#take input of a character
char=input("Please enter your own character to check how many times it occurs in your word: ")
i=0
count=0
#loop will to find the occurence of character
while(i<len(string)): #string operation

    if (string[i]==char): #condition 1
        count=count+1
    i=i+1


#Display the result
print("The total number of times", char, " has occured is ", count)

#Write a program to calculate the product of the middle digits of a number?
#Input a number
num=int(input("Enter the number: "))
t=num
numLen=0
#iterate the loop
while t>0:
    numLen=numLen+1
    t=int(t/10)

if numLen>=4: #condition 1
    numLen=int(numLen/2)
    chk=0
    while num>0: #iterate loop
        rem=num%10
        if chk==numLen: #nested condition
            midOne=rem
        elif chk==(numLen-1):
            midTwo=rem
        num=int(num/10)
        chk=chk+1
    prod=midOne*midTwo
    #display the result
    print("\nProduct of Mid Digits("+str(midOne)+ "*" +str(midTwo)+")=", prod)
else:
    print("\nIt's not a 4 or more than a 4-digit number!")

