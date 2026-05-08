import random

guessing = True

while guessing == True:
    
    guess_number = random.randint(1,100)
    
    guess = -1

    guess_count = 0


    while  guess_number != guess:

        guess_count = guess_count + 1    

        guess = float(input("What is your guess ? "))

        if guess < guess_number:
            print("Lower")
        elif guess > guess_number:
            print("Higher")
        elif guess == guess_number:
            print("You guessed it!")
    
    print(f"It took {guess_count} guesses")

keep_playing = input("Play again ? (yes/ no ) ")
    