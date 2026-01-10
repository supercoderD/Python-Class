#There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper. Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?
h1=98
h2=94
h3=41
h4=96
h5=11
sum=(h1+h2+h3+h4+h5)
average=(sum/5)
print("The average of the heights is",average)


#Write a program to calculate the number of notes in the given amount?
amt=int(input("Enter the amount for withdraw. : "))

note=amt//200
note1=(amt%200)//100
note2=((amt%200)%100)//50
note3=(((amt%200)%100)%50)//10

print("Notes of 200 :", note)
print("Notes of 100 :", note1)
print("Notes of 50 :", note2)
print("Notes of 10 :", note3)