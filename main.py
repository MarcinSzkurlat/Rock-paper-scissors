import random
import string

choices = ["rock", "paper", "scissors"]

play = True
computer_score = 0
player_score = 0

print("Welcome to the Rock, Paper, Scissors game")

while play == True:
    print("Instrukcja")
    computer_guess = random.choice(choices)
    print(computer_guess)
    
    player_guess = input()
    
    if computer_guess == player_guess:
        print("Computer chose", computer_guess, "It's a draw!")

    elif player_guess == "rock":
        if computer_guess == "paper":
            computer_score += 1
            print("You lose!")
        elif computer_guess == "scissors":
            player_score += 1
            print("You win!")
    elif player_guess == "paper":
        if computer_guess == "rock":
            player_score += 1
            print("You win!")
        elif computer_guess == "scissors":
            computer_score += 1
            print("You lose!")
    elif player_guess == "scissors":
        if computer_guess == "paper":
            player_score += 1
            print("You win!")
        elif computer_guess == "rock":
            computer_score += 1
            print("You lose!")