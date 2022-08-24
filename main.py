import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
play = True
computer_score = 0
player_score = 0

print("Welcome to the Rock, Paper, Scissors game")

while play == True:
    print("Instrukcja")
    