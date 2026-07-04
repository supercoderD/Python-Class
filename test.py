# #Student Grade Book
# Build a grade book that stores student names and scores in a dictionary. Your program calculates the class average, finds the top and bottom scorer, and lets the user look up any student's grade.

# What you need to use
# ------------------------------------------------------------------------
# 1.  dictionary      →  store at least 5 student name-score pairs
# 2.  for loop        →  to calculate the class average
# 3.  max() min()     →  to find the top and bottom scorer
# 4.  .get()          →  to look up a student by name
# 5.  input()         →  to let the user search for a student
# ------------------------------------------------------------------------
data={"Jai": 94, "Vani": 92, "Karan": 95, "Darsh": 97, "Riya": 94}
total=0
for score in data.values():
    total+=score
average=total/len(data)
print(average)
top=max(data,key=data.get)
bottom=min(data,key=data.get)
print("The highest scorer is:", top, "and the bottom scorer is", bottom)
student=input("Enter the student name: ")
if student in data:
    print(student, "score is", data[student])
else: 
    print("The student is not found.")  
#add a new item
name=input("Enter a new student name")
grade=int(input("Enter the new student's score."))
data[name]=grade
print(data)
for names in data:
    if data[names] >=95:
        print(names , "-", data[names])
        

