# Create rock, paper, scissors game against the computer

from random import randint

# moves for the player
moves = ["rock", "paper", "scissors"]

while True:
    computer = moves[randint(0,2)]

    player = input("rock, paper, or scissors? (or 'end' to stop the game) ").lower()
    if player == "end":
        print("The game has ended.")
        break
    elif player == computer:
        print("Tie.")
    elif player == "rock":
        if computer == "paper":
            print("Player chose:", player, "Computer chose:", computer, "-- Papers covers rock. Computer wins.")
        else: # computer had to choose scissors
            print("Player chose:", player, "Computer chose:", computer, "-- Rock crushes scissors. Player wins.")
    elif player == "paper":
        if computer == "rock":
            print("Player chose:", player, "Computer chose:", computer, "-- Papers covers rock. Player wins.")
        else: # computer had to choose scissors
            print("Player chose:", player, "Computer chose:", computer, "-- Scissors cuts paper. Computer wins.")
    elif player == "scissors":
        if computer == "paper":
            print("Player chose:", player, "Computer chose:", computer, "-- Scissors cuts paper. Player wins.")
        else: # computer had to choose rock:
            print("Player chose:", player, "Computer chose:", computer, "-- Rock crushes scissors. Computer wins.")
    else:
        print("Incorrect choice. No spock or lizard allowed ...)")



