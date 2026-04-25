def shutdown():
    import turtle
    turtle.Screen().bgcolor('black')
    turtle.done()
ask=input("Do you want to do the shutdown?")
if ask=="yes":
    shutdown()
elif ask=="no":
    print("Okay, the shutdown will be delayed.")
else:
    print("I'm sorry, I couldn't understand that.")
