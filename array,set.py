# Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]
set1={1,2,3,4,5,6}
set2={"aowirghu",3967}
set3={1,2,3,4,3,2,4}
set4=set([1,2,3,2])
set4.pop()
print(set1,set2,set3,set4)
set5={10,20,30}
set6=(30,50,59,60)
s1=set5.union(set6)
s2=set5.intersection(set6)
s3=set5.difference(set6)
print(s1,s2,s3)


import array as arr
arraynum=arr.array("i", [1,3,5,3,7,9,3])
print("The orginal array was"+str(arraynum))
print("Number of occurences of the the said array:"+str(arraynum.count(3)))
arraynum.reverse()
print("Reverse of the order of the items:")
print(str(arraynum))
arraynum2=arr.array("i", [6,7,8,9,1,2,3,34,89])
a1=arr.array("i")
a1=arraynum+arraynum2
print(a1)