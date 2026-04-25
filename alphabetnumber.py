#Write a Python function that accepts a string and counts the number of upper and lower case letters
ask=input("Enter a string. ")
def upperlower(ask):
    uppercount=0
    lowercount=0
    for i in ask:
        if i.isupper():
            uppercount+=1
        else:
            lowercount+=1

    print("The amount of uppercase letters is", uppercount, "and the amount of lowercase letters is", lowercount)
upperlower(ask)   

        

