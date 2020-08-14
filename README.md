# Treehouse Python Techdegree - project 1

## Command-line programme guessing game. 

**How to use this programme:**
- Run with:
  - $python3 guessing_game.py
- Follow prompts in the terminal to play the game. 

**Rules of the game**
- Choose wether you want to choose your own range. (The random number will be chosen within this range)
  - y, yes, Y, YES are all accepted for yes, all other characters are accepted for no.
- If you don't choose your own range it will default to a number between 1 and 10.
- Type in your guess
  - This should be a numerical character. If it's not, a custom error will display
  - This should be within the specified range. If not, you will receive a warning that it is out of range, but the attempt will still count. (Please see code comments for changes to make it not count)
  - After each guess it will notify you whether the answer is lower or higher
  - Continue guessing until you get it right.
- When you guess the answer correctly
  - You are congratulated
  - If you made the new high score of this round you will be notified
  - Choose whether you want to play another round.
    - y, yes, Y, YES are all accepted for yes, all other characters are accepted for no.
  - If you do, a new game will start and the current high score displayed
  - If you don't the game will end. 
