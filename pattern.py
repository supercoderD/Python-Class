#Take input
print("Half Pyramid pattern of Stars (*):  ")
n=int(input("Enter the number of rows: "))
#outer loop to handle number of rows
for i in range(n,0, -1):
    #inner loop to handle number of columns
    for j in range(i+1,1, -1):
        #display result
        print("* ", end="")
    print()



#Take Input
print("Floyd's Traingle Pyramid: ")
num=1
n=int(input("Enter the number of rows: "))
#outer loop to handle the number of rows
for i in range(1,n+1):
    #inner loop to handle number of columns
    for j in range(i):
        #display result
        print(num, end=" ")
        num+=1
    print()

#take input from user
rowSize=int(input("Enter the number of rows. "))
if rowSize%2==0: #conditions
    halfDiamRow=int(rowSize/2)
else:
    halfDiamRow=int(rowSize/2)+1
space=halfDiamRow-1
#loop for upper part
for i in range(1,halfDiamRow+1): #loop for rows
    for j in range(1, space+1): #loop for columns
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
    #incrementing number at each column
        num=num+1
    print()
space=1
#loop for lower part
for i in range(1, halfDiamRow): #loop for rows
    for j in range(1, space+1): #loop for columns
        print(end=" ")
    space=space+1
    num=1
    for j in range(1, 2*(halfDiamRow-i)):
        print(end=str(num))
    #incrementing number at each column 
        num=num+1
    print()  
    
    

