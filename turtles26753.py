# import turtle
# turtle.Screen().bgcolor('green')
# turtle.Screen().setup(400,300)
# t=turtle.Turtle()


# sides=3
# length=80
# angle=360/sides
# # if sides>2:
# #     length=int(input("Enter the length of 'sides'"))
# #     angle=360/sides
# # else:
# #     print("Enter a different amount of sides(greater than 3)")
# t.fillcolor('red')
# t.begin_fill()
# for i in range(sides):
#     t.forward(length)
#     t.left(angle)
# t.end_fill()
# t.penup()
# t.goto(0,40)
# t.pendown()
# t.begin_fill()
# for i in range(sides):
#     t.forward(length)
#     t.right(angle)

# t.end_fill()

# turtle.done()

import turtle
turtle.Screen().bgcolor('green')
turtle.Screen().setup(400,300)
t=turtle.Turtle()
#Square Spiral Pattern

t.speed(5)
len=20
t.width(2)
for i in range(50):
    t.forward(len)
    t.right(144)
    len+=5
turtle.done()

















