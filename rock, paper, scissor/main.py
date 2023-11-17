from random import randint

title = "rock, paper, scissor game"
print(title)
print(f"{'=' * len(title)}")

weapon = ("rock", "paper", "scissor")

player = input("choose your weapon (rock|paper|scissor):")
computer = weapon[randint(0,2)]

if player == computer:
    print("player uses", player)
    print("computer uses", computer)
    print("nobody wins!")
elif player == "rock":
    if computer == "paper":
     print("player uses", player)
     print("computer uses", computer)
     print("computer wins!")
    elif computer == "scissor":
     print("player uses", player)
     print("computer uses", computer)
     print("player wins!") 
elif player == "scissor":
    if computer == "paper":
     print("player uses", player)
     print("computer uses", computer)
     print("player wins!")
    elif computer == "rock":
     print("player uses", player)
     print("computer uses", computer)
     print("computer wins!")
elif player == "paper":
    if computer == "scissor":
     print("player uses", player)
     print("computer uses", computer)
     print("computer wins!")
    elif computer == "rock":
     print("player uses", player)
     print("computer uses", computer)
     print("player wins!")
  

