#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
from replit import clear


def set_difficulty():
  EASY_LEVEL_TURNS = 10
  HARD_LEVEL_TURNS = 5
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def guess_game():
  print(logo)
  print("Welcome to Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  attempt=set_difficulty()
  number=random.randint(1,101)
  the_end=True
  while not attempt<1 and the_end:
    guess=int(input("Make a Guess: "))
    if guess==number:
      print(f"you got it!.The answer is {guess}")
      the_end=False 
    else:
      if guess>number:
        print("Too High!")
        print("Guess again")
      
      elif guess<number:
        print("Too low")
        print("Guess again")
    attempt=attempt-1
    print(f"you have {attempt} remaining to guess the number")
guess_game()
choise=input("Do you wanna Guess again?Type 'yes' or 'no': ")
if choise=="yes":
  clear()
  guess_game()
else:
  print("come back soon!")

