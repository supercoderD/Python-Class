studentdata={
    "id1": {"name": "Sara", "class": "V", "subject_integration": "english,math,science"},
"id2":{"name":"David", "class": "V", "subject_integration": "english, math, science"},
 "id3": {"name": "Sara", "class": "V", "subject_integration": "english,math,science"},
"id4": {"name": "Surya", "class": "V", "subject_integration": "english,math,science"}}

result={}
seenkeys=[]
for studentid, details in studentdata.items():
    uniquekey=(details["name"], details["class"], details["subject_integration"])

    if uniquekey not in seenkeys:
        seenkeys.append(uniquekey)
        result[studentid]=details


for k, v in result.items():
    print(k, ":", v)





testdictionary={"Codingal": 2, "is" : 2, "for": 2, "Coding":1}
print("The original dictionary:" + str(testdictionary))
k=2
res=0
for key in testdictionary:
    if testdictionary[key]==k:
        res+=1

print("Frequency of k is:" + str(res))



d1={'name':"darsh",'address':{'hno':50,'code':141}}
print(d1["address"]["code"])

d2={"age":10}
d3={"height":1.31}
d2.update(d3)
print(d2)
