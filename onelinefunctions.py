#map function in action

num1=[1,2,3]
num2=[4,5,6]
result=map(lambda x,y: x+y, num1,num2)
print("Addition of the two lists")
print(list(result))

nums=[1,2,3,4,5]
def square(n):
    return n**2
squar=list(map(square,nums))
print("Square of numbers in list")
print(squar)
# zip function in action
s1={8,9,10}
s2={"d","f", "z"}
s3=list(zip(s1, s2))
print(s3,"\n")

list1=[50,60,70,80]
list2=[500,600,700,800]

for x,y in zip(list1, list2[::-1]):
    print(x,y)



stocks=["reliance", "infosys", "tcs"]
prices=["2175", "1127", "2750"]
newdiction={stocks: prices for stocks, prices in zip(stocks,prices)}
print("\n{}".format(newdiction))

for i in range(1,11):
   
    if i==5:
        print(exit)
        exit()
    print(i)

