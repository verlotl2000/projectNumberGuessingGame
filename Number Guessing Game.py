import random
import time
import json



def game (): 
    print()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("The number of guessing chances will be determined by the difficulty level.")

    print()
    with open ("highscore.json") as infile:
        highscore = json.load(infile)
    
    print("Highscores:")
    print("Easy: " + highscore["easy"])
    print("Medium: " + highscore["medium"])
    print("Hard: " + highscore["hard"])
    
    print()
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print()
    print("Enter your choice: ")
    

    while True:
        difficulty = input()
        if difficulty == "1":
            print()
            print("Great, you have selected the Easy difficulty level!")
            chances = 10
            difficulty = "easy"
            break
        elif difficulty == "2":
            print ()
            print("Great, you have selected the Medium difficulty!")
            chances = 5
            difficulty = "medium"
            break
        elif difficulty == "3":
            print()
            print("Great, you have selected the Hard difficulty!")
            chances = 3
            difficulty = "hard"
            break
        else:
            print("Please enter 1 (easy), 2(medium), or 3(hard).")    

    print()
    input("Press any key to start the game and the timer: ")
    start = time.time()

    randomNumber = random.randrange(1, 100)

    while True:
        try:
            guess = int( input("Enter your guess:"))
            tries = 1
            break
        except ValueError:
            print("Please enter a numerical value.")

    numberGuessed = False  

    while numberGuessed == False: 
        while tries < chances:
            if guess == randomNumber:
                numberGuessed = True
                break
            elif guess > randomNumber:
                print("Incorrect! The number is less than " + str(guess))
                tries += 1
                while True:
                    try:
                        guess = int( input("Enter your guess:"))
                        break
                    except ValueError:
                        print("Please enter a numerical value.")
            else:
                print("Incorrect! The number is greater than " + str(guess))
                tries += 1
                while True:
                    try:
                        guess = int( input("Enter your guess:"))
                        break
                    except ValueError:
                        print("Please enter a numerical value.")
        else:
            print("Game over! You have ran out of chances!")
            break
    else:
        print()
        end = time.time()
        elapsedTime = int(end - start)
        print("Congratulations! you guessed the right number in " + str(tries) + " attempts and " + str(elapsedTime) + " seconds!")
        if tries < int(highscore[difficulty]):
            highscore[difficulty] = str(tries)
            jsonDump = json.dumps(highscore)
            with open ("highscore.json", "w") as outfile:
                outfile.write(jsonDump)
            
    keepPlaying = ""

    while True:
        print()
        keepPlaying = input("Would you like to play another round (Y/N)?: ")
        if keepPlaying == "Y" or keepPlaying == "y" or keepPlaying == "N" or keepPlaying == "n":
            if keepPlaying == "Y" or keepPlaying == "y":
                keepPlaying = True
            else:
                keepPlaying = False
            break
        else:
            print("Please enter Y or N.")

    if keepPlaying == True:
        game()
    else:
        exit()

game()    



    