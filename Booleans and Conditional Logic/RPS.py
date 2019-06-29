import random

player_wins = 0
computer_wins = 0
winning_score = 3
while player_wins != winning_score and computer_wins != winning_score:

	print(f"Player wins: {player_wins}")
	print(f"Computer wins: {computer_wins}")
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

	if player == computer:
	    print("It's a tie!")
	elif player == "rock": 
	    if computer == "scissors":
		    print("player1 wins!")
		    player_wins += 1 
	    else:
		    print("computer wins!")
		    computer_wins += 1
	elif player == "paper":
	    if computer == "rock":
		    print("player1 wins!")
		    player_wins += 1 
	    else:
		    print("computer wins!")
		    computer_wins += 1
	elif player == "scissors": 
	    if computer == "paper":
		    print("player1 wins!")
		    player_wins += 1 
	    else:
		    print("computer wins!")
		    computer_wins += 1
	else:
	    print("something went wrong")
		
if player_wins > computer_wins:
	print("CONGRATS, YOU WON!")
else:
	print("You suck lol")
