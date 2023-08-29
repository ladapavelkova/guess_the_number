#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print ( "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
guessed_number = random.randint(1,100)
print ( f"Pssst, the correct answer is {guessed_number}")

difficulty = input ( "Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  attempts = 10
  print ( f"You have {attempts} attempts remaining to guess the number." )
  guess = int ( input ( "Make a guess: "))
  end_of_game = False
  while guess != guessed_number and end_of_game == False:
    attempts -= 1
    if guess > guessed_number :
      print ( "Too high.")
    else:
      print ( "Too low.")
    if attempts == 0:
      end_of_game = True
      print ( f"You ran out of lives, you lose! The answer wa {guessed_number}")
    else:
      print ( f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")
      guess = int ( input ( "Make a guess: "))  
  if guess == guessed_number:
    print ( f"You won ! The answer was {guessed_number}")
elif difficulty == "hard":
  attempts = 5
  print ( f"You have {attempts} attempts remaining to guess the number." )
  guess = int ( input ( "Make a guess: "))
  end_of_game = False
  while guess != guessed_number and end_of_game == False:
    attempts -= 1
    if guess > guessed_number :
      print ( "Too high.")
    else:
      print ( "Too low.")
    if attempts == 0:
      end_of_game = True
      print ( f"You ran out of lives, you lose! The answer wa {guessed_number}")
    else:
      print ( f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")
      guess = int ( input ( "Make a guess: "))  
  if guess == guessed_number:
    print ( f"You won ! The answer was {guessed_number}")
    
