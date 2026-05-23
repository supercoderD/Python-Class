#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple
t1=(7, "char", 8, 8.0002093804, "boing")
t2=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2)
t3=(9,)
t4=(t2+t3)
print(t4)
print(t2[3:6+1])
print(t2.count(1))

def palindrome(r):
    e=len(r)-1
    s=0
    while(s<e):
        if (r[s]!=r[e]):
              return False
            
      
        s+=1
        e-=1
    return True

r=(1,2,3,2,1)
if(palindrome(r)):
    print("The Tuple is Flip-Flop")
else:
    print("The Tuple is not Flip-Flop")

