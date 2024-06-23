import random

def number_guess_game():
    
                                                                                      # Step 1: Game initialization
    guess_num = random.randint(1, 10)
    attempts_left = 5
    game_won = False
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    print(f"You have {attempts_left} attempts to guess it.")
    
                                                                                         # Step 2: Game loop
    while attempts_left > 0 and not game_won:
        try:
            player_guess = int(input("Enter your guess: "))
            
            if player_guess < 1 or player_guess > 10:
                print("Please enter a number between 1 and 10.")
                continue
            
            if player_guess == guess_num:
                print("Congratulations! You guessed the number correctly!")
                game_won = True
            elif player_guess < guess_num:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            
            attempts_left -= 1
            if attempts_left > 0 and not game_won:
                print(f"You have {attempts_left} attempts left.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
                                                                                                           # Step 3: Game end
    if not game_won:
        print(f"Sorry, you've run out of attempts. The number was {guess_num}. Better luck next time!")

                                                                                                           # Step 4: Run the game
number_guess_game()
