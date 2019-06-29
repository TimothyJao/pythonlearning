import random

rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print("Rock...")
print("Paper...")
print("Scissors...")
player = input("Player, make your move: ").lower()
print("The computer choose: " + computer)
# print("***NO CHEATING! \n\n" * 20)
# p2 = input("Player 2, make your move: ")

if player == computer:
    print("It's a tie!")
elif player == "rock": 
    if computer == "scissors":
        print("player1 wins!")
    else:
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("player1 wins!")
    else:
        print("computer wins!")
elif player == "scissors": 
    if computer == "paper":
        print("player1 wins!")
    else:
        print("computer wins!")
else:
    print("something went wrong")