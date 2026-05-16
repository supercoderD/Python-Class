l1=[]
print()
numerals=[1,2,3,4,5,6,7,8,9,10]
print(numerals)
triplets=[1,2,3,4,5,6]*3
print(triplets)
l2=[100,200,300,400,500,600,700,800,900,1000]
l2=l2[::-1]
print(l2, "\n")

#function to check whether first and last character of words match
def matchwords(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)


    print("List of words with first and last character same\n", lst)
    return ctr

count=matchwords(["abc", "cfc", "erioulgh", "xyxyxyxyxyxyxyxyx","6xy*2"])
print("Number of words having first and last character same",  count)




l3=[4,5,1,2,9,7,10,8]
print("Orginal List", l3)
sum=0
for i in l3:
    sum+=i
print("The sum of the list is", sum)
average=sum/len(l3)
print(average)

x=max(l3)
y=min(l3)
print(x,y)
l3.sort(reverse=True)
print(l3)