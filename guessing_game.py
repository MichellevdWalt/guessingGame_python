"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

#Empty scores array to store scores for high score purposes
scores = []

#Function to control the game flow
def start_game():
    attempts = 0
    
    print("\nWelcome to the number guessing game!")
    if scores:
      print("\nThe current high score is {}".format(min(scores)))
    while True:
      ownRange = input("\nWould you like to choose your own range? Y/N  ")
      if ownRange.lower() == "y" or ownRange.lower() == "yes":
        lowest = int(input("Please choose the lowest number  "))
        highest = int(input("Please choose the higest number  "))
        break
      elif ownRange.lower() == "no" or ownRange.lower() == "n":
        lowest = 1
        highest = 10
        break
      else:  
        print("\nPlease answer with either yes or no")
        continue
      
      
    answer = random.randint(lowest, highest)
          
    while True:
        try:
            guess = input("\nPlease choose a number between {} and {}   ".format(lowest, highest))
            attempts += 1
            if guess.isnumeric():
                guess = int(guess)
                if guess == answer:
                    break
                else:
                    if guess > answer and guess <= highest:
                        print("\nIt's Lower")
                        continue
                    elif guess < answer and guess >= lowest:
                        print("\nIt's higher")
                        continue
                    else:
                        print("\nYour guess is out of range, it still counts though :)")
                        #If you don't want this to count uncomment the next line and edit above
                        # attempts -= 1
                        continue
            else:
                raise ValueError("\nWoops, that's not a number") 
        
        except ValueError:
            print("\nWoops, that's not a number")
            continue

        except ValueError as err:
            print("{}".format(err))
            continue      

    print(
      """\nCongratulations, you WIN!!!
It only took you {} attempts""".format(attempts))
    scores.append(attempts)
    if attempts == min(scores):
      print("\nWooop!! you just hit a new HIGH SCORE!!!")
    play_again()
      
# Function to prompt and control what happens when a player wants to play again or not      
def play_again():
  while True:
    again = input("\nWould you like to play again? Y/N   ")
    if again.lower() == "y" or again.lower() == "yes":
      start_game()
      break
    elif again.lower() == "n" or again.lower() == "no":
      print("Thanks for playing")
      break
    else:
      print("\nPlease answer with either yes or no")
      continue

start_game()

























