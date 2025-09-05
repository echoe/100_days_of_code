"""
A game to guess a number. Pick easy or hard to decide between having 10 guesses or 5.
-Print logo ( from https://patorjk.com/software/taag/ )
-Intro game and ask for difficulty. If input is wrong, re-ask for input
-Set number and guesses, go into while loop.
-Ask player for a guess.
-Check if the guess is correct and if not, how it's wrong
-Adjust guesses, inform player, and get additional guesses until either they fail or they win.
"""
import random
logo = r"""
                                                                                                                       
 ,----.                                      ,--.  ,--.                                          ,--.                  
'  .-./   ,--.,--. ,---.  ,---.  ,---.     ,-'  '-.|  ,---.  ,---.     ,--,--, ,--.,--.,--,--,--.|  |-.  ,---. ,--.--. 
|  | .---.|  ||  || .-. :(  .-' (  .-'     '-.  .-'|  .-.  || .-. :    |      \|  ||  ||        || .-. '| .-. :|  .--' 
'  '--'  |'  ''  '\   --..-'  `).-'  `)      |  |  |  | |  |\   --.    |  ||  |'  ''  '|  |  |  || `-' |\   --.|  |    
 `------'  `----'  `----'`----' `----'       `--'  `--' `--' `----'    `--''--' `----' `--`--`--' `---'  `----'`--'    
                                                                                                                       """
def play_again():
    """Asks if we want to play again, and starts the game over again if we do."""
    if input("Press y to play again.").lower() == "y":
        game()
    else:
        print("Thanks for playing!")
        exit()

def game():
    """Runs the game."""
    print(" " * 20)
    print(logo)
    thenumber = random.randint(1, 100)
    lives = 0
    while lives == 0:
        difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n"
                           "Choose a difficulty. Type 'easy' or 'hard':").lower()
        if difficulty == "easy":
            lives = 10
        elif difficulty == "hard":
            lives = 5
        else:
            print("Please type easy or hard!")

    while lives > 0:
        guess = int(input(f"You have {lives} attempts remaining to guess the number.\nMake a guess: "))
        if guess > thenumber:
            lives -= 1
            print("Too high. Guess again.")
        elif guess < thenumber:
            lives -= 1
            print("Too low. Guess again.")
        elif guess == thenumber:
            print("You picked the right number. You win!")
            play_again()
    print("You ran out of guesses. You lose!")
    play_again()

game()