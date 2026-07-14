import random
user=input("enter your choice :")
b=["rock","paper","scissors"]
computer=random.choice(b)
if user==computer:
    print("DRAW")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("conguration you win")
else:
    print("Computer Wins")