#added guessing limit
word = "cat"
count = 0
underscore = len(word) * "_ "

guess = ""
while word != guess and count != 3:
    
    underscores = underscore
    
    print(f"Hint : {underscores}")
    
    guess = input("What is your guess ? ")

    count = count + 1


    
    if word == guess:
        print("Congratulations! You guessed it")
        print(f"You took {count} guesses")
    else:
        if len(word) == len(guess):
            i = 0
        else:
            print("Sorry, guess word should be the same length as secret word")

        #print(f"It took {count} guesses")


