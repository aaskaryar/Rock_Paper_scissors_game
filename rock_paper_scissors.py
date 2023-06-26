from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    num = 'rock'
elif num == 2:
    num = 'paper'
elif num == 3:
    num = 'scissors'  
else:
    print("error") 

# Ask a user to enter their move
move = input("rock, paper, or scissors?")
move = move.lower()
if not( move == "rock" or move == "paper" or move == "scissors"):
    input("Wrong input! rock, paper, or scissors?")
# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if move == 'rock':
    print(rock)
elif move == 'paper':
    print(paper)
else:
    print(scissors)
# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
if num == 'rock':
    print(rock)
elif num == 'paper':
    print(paper)
else:
    print(scissors)

# Figure out who wins and print the result!
rock > scissors
scissors > paper
paper > rock

if (move == 'rock' and num == 'scissors') or (move == 'scissors' and num == 'paper') or (move == 'paper' and num == 'rock'):
    print("you win")
elif (num == 'rock' and move == 'scissors') or (num == 'scissors' and move == 'paper') or (num == 'paper' and move == 'rock'):
    print("you lose")
else:
    print("Tie")
