#write a program to check whether the given number is positive?
num=int(input("Enter a number : "))
if num >0:
    print(num,"is a positive number")
if num <0:
    print(num, "is a negative number.")
#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?
purchase=int(input("Enter the cost price of the oranges : "))
selling=int(input("Enter the selling price of your bought oranges : "))
if purchase>selling:
    loss=purchase-selling
    print("You have a loss of", loss)
else:
    profit=selling-purchase
    print("You have a profit of", profit)
    


#Write a program to check whether the given number is even or odd?
num2=int(input("Enter a number: "))
if num2 % 2==0:
    print(num2,"is even.") 
else:
    print(num2, " is odd")
