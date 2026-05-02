# import random

# while True:
#     useraction=input("Enter a choice(rock, paper, scissors):")
#     possibleactions=["rock", "paper", "scissors"]
#     computeraction=random.choice(possibleactions)
#     print(f"\nYou chose {useraction}, computer chose {computeraction}.\n")

#     if useraction==computeraction:
#         print(f"Both players selected {useraction}. It's a tie!")
#     elif useraction=="rock":
#         print("Rock smashes scissors! You win!")
#         if computeraction=="scissors":
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif useraction=="paper":
#         if computeraction=="rock":
#             print("Paper covers rock! You lose!")
#         else:
#             print("Scissor cuts paper! You lose.")
#     elif useraction=="scissors":
#         if computeraction=="paper":
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")
#     playagain=input("Do you want to play again? (y/n)")
#     if playagain!="y":
#         break



import math
print(math.ceil(23.56))
print(math.floor(23.56))
x=10
y=x-25
print("The value of x after copying the sign from y is: " + str(math.copysign(x,y)))

print(math.fabs(-96))
print(math.fabs(56))

print(math.gcd(39, 39))
print(math.sqrt(309))
print(math.factorial(67))
print(math.pow(10, 3))







































































































