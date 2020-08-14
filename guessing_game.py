"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

scores = []
def start_game():
    attempts = 0
    
    print("\nWelcome to the number guessing game!")
    if scores:
      print("\nThe current highscore is {}".format(min(scores)))
    ownRange = input("\nWould you like to choose your own range? Y/N  ")
    if ownRange.lower() == "y" or ownRange.lower() == "yes":
      lowest = int(input("Please choose the lowest number  "))
      highest = int(input("Please choose the higest number  "))
    else:
      lowest = 1
      highest = 10
      
    answer = random.randint(lowest, highest)
    print("Answer", answer)
          
    while True:
        try:
            guess = input("\nPlease choose a number between {} and {}   ".format(lowest, highest))
            if guess.isnumeric():
                guess = int(guess)
                if guess == answer:
                    break
                else:
                    if guess > answer and guess <= highest:
                        print("\nIt's Lower")
                        attempts += 1
                        continue
                    elif guess < answer and guess >= lowest:
                        print("\nIt's higher")
                        attempts += 1
                        continue
                    else:
                        print("\nYour guess is out of range, it still counts though :)")
                        attempts += 1
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
      print("\nWooop!! you just hit a new HIGHSCORE!!!")
    play_again()
      
      
def play_again():
  again = input("\nWould you like to play again? Y/N   ")
  if again.lower() == "y" or again.lower() == "yes":
    start_game()

start_game()

























