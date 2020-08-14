"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

scores = []
def start_game():
    attempts = 0
    
    print("Welcome to the number guessing game!")
    if scores:
      print("The current highscore is {}".format(min(scores)))
    ownRange = input("Would you like to choose your own range? Y/N  ")
    if ownRange.lower() == "y" or ownRange.lower() == "yes":
      lowest = int(input("Please choose the lowest number  "))
      highest = int(input("Please choose the higest number   "))
    else:
      lowest = 1
      highest = 10
      
    answer = random.randint(lowest, highest)
    print("Answer", answer)
    
    while True:
      try:
        guess = int(input("Please choose a number between {} and {}   ".format(lowest, highest)))
        if guess:
          print("true")
          guessInt = int(guess)
          attempts += 1
          break
        else:
          print("false")
          raise ValueError("Woops, that's not a valid number")          
        
      except ValueError:
        print("Woops, that's not a number")
      
      except ValueError as err:
        print("{}".format(err))
        continue
          
        
#    while guess != answer:
#      try:
    while True:
      if guess == answer:
        break
      else:
        try:
          if guess:
            
            if guess > answer and guess <= highest:
              print("It's Lower")
              guess = int(input("Please choose a number between {} and {}   ".format(lowest, highest)))
              attempts += 1
              continue
            elif guess < answer and guess >= lowest:
              print("It's higher")
              guess = int(input("Please choose a number between {} and {}   ".format(lowest, highest)))
              attempts += 1
              continue
            else:
              print("Your guess is out of range, it still counts though :)")
              guess = int(input("Please choose a number between {} and {}   ".format(lowest, highest)))
              attempts += 1
              continue
            
          else:
            raise ValueError("Woops, that's not a valid number")
            continue
        
        except ValueError:
          print("Woops, that's not a valid number, please try again")
          guess = int(input("Please choose a number between {} and {}   ".format(lowest, highest)))
          continue
          
          
        except ValueError as err:
          print("{}".format(err))
          guess = int(input("Please choose a number between {} and {}   ".format(lowest, highest)))
          continue
        
#      except ValueError:
#        print("Woops, that's not a valid value")
#        guess = int(input("Please choose a number between {} and {}   ".format(lowest, highest)))
        
    print(
      """\nCongratulations, you WIN!!!
It only took you {} attempts""".format(attempts))
    scores.append(attempts)
    if attempts == min(scores):
      print("\nWooop!! you just hit a new HIGHSCORE!!!")
    play_again()
      
      
def play_again():
  again = input("\nWould you like to play again? Y/N   ")
  if again.lower() == "y" or again.lower() == "yes":
    start_game()

start_game()

























