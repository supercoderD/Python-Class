class myClass:
    __privateVar=27
    def __privMath(self):
        print("Hi, today we are going to find privateVar")
    def hello(self):
       print(myClass.__privateVar)

foo=myClass()
foo.hello()
# foo.__privMath()

class add:
    def __init__(self,value):
        self.value=value
    def __add__(self, other):
        return self.value+other.value
    def __eq__(self, other):
         return self.value==other.value
        
a=add(100)
b=add(100)
print(a+b)
print(a==b)