### NOT IN GITHUB - TESTING OUT PYTHON STUFF FROM BOOK PROJECTS

import random
import sys

#Start game is the intro to the game
def start_game():
    #This is where we will take character input from the user
    #They will either choose one or two to do an action
    print('Press "1" to play guessing game')
    print("----------------------------")
    print('Press "2" to play multiple guessing games')
    print("----------------------------")
    print('Press "3" to quit')
    print("----------------------------\n")
    
    #This will give the value that the user has given us
    intro = "Please select what you would like to do: "
    introInput = input(intro)
    
    #numberOfGuess is the number of guesses it has taken 
    numberOfGuess = 0
    
    #If the input is 1 we will display this and go to the next definition (oneGame(numberOfGuess))
    if int(introInput) == 1:
        oneGame(numberOfGuess)
        
    #If the input is 2 we will display this and go to the next definition (multiplesGames(numberOfGame, 0))
    if int(introInput) == 2:
        multipleGames(numberOfGuess, 0)
    
    #If the input is 3 it will display this and exit 
    elif int(introInput) == 3:
        print("\n----------------------------")
        print("Exiting")
        print("----------------------------\n")
        sys.exit()
    
    #If it is higher or lower to what we want it will say try again and start over
    elif int(introInput) > 2 | int(introInput) < 1:
        print("Try Again")
        start_game()
    
    #If it is anything else - then start over
    else:
        print("I said a number!")
        start_game()
        

#This will be everything the game will do for one game
def oneGame(numberOfGuess):
    
    #picks a random number from 0 to 100
    randomNumber = random.randint(0, 100)
    #Flag to get out of loops
    flag = False

    #Question asked so they enter in a value
    guess = "Enter a value to guess a number: "

    #loop is flag is false
    while flag == False:
        
        #This is the user guess
        userInput = int(input(guess))
        
        #If they are right
        if userInput == randomNumber:
            #Show that they are correct and how many guesses it took, Our flag is now true to stop the loop
            #Start over to the main menu
            print("Correct!")
            print("Number of guesses is: " + str(numberOfGuess + 1) + "\n")
            flag = True
            start_game()

        #Users guess is too low
        elif userInput < randomNumber:
            print("Too low!")
            numberOfGuess += 1
            
        #Users guess is not in range
        elif userInput < 0 | userInput > 100:
            print("Your guess has to be 0-100!")
        
        #Users guess is too high
        else:
            print("Too high!")
            numberOfGuess += 1

#This definition is for multiple games, also gives an average by how many guesses is takes    
def multipleGames(numberOfGuess, numberOfGames):
    
    #Random number 0-100
    randomNumber = random.randint(0, 100)
    #Flag to get out of a loop
    flag = False
    
    #if the number of games is 0 (Which it is when called)
    if numberOfGames == 0:
        #Deciding how many games we will play
        games = "How many games would you like to play: "
        
        #User input for the number of games we are playing
        numberOfGames = int(input(games))
        
        #Shows the user how games will be played and starting
        print("\n")
        print("You will now play " + str(numberOfGames) + "!")
        print("----------------------------------------")
        print("Your game will start now...")
        print("----------------------------------------\n")
        
        #User guess
        guess = "Enter a value to guess a number: "

    #While the flag is false
    while flag == False:
        
        #Variables for making a array and a marker to see how games we've played
        values = []
        index = 0
        
        #looping until our index marker equals the players wanted amount of games
        while index != numberOfGames:
            
            #user guess
            userInput = int(input(guess))
            
            #If user guess equals the random number
            if userInput == randomNumber:
                
                #Then they are correct
                print("Correct!")
                
                #Show the number of guesses it took
                print("Number of guesses is: " + str(numberOfGuess + 1) + "\n")
                
                #add the number of guesses into the values array
                values.append(numberOfGuess + 1)
                
                #number of guesses get reset because of playing multiple games
                numberOfGuess = 0
                
                #give another random number
                randomNumber = random.randint(0, 100)
                
                #index gets incremented
                index = index + 1

            #users guess is less than the random number
            elif userInput < randomNumber:
                #Guess was too low
                print("Too low!")
                #Guess increments
                numberOfGuess += 1
                
            #User input is less than 0 and greater than 100
            #No guess penalty 
            elif userInput < 0 | userInput > 100:
                print("Your guess has to be 0-100!")
                
            #Otherwise must be greater than random number
            else:
                print("Too high!")
                #Number of increments
                numberOfGuess += 1
                
        #Average guess of the values array
        #Value array - found the average by summing up all the values and dividing it by the length of the array
        averageGuess = (sum(values)/len(values))
        
        #Show the average amount for guessing
        print("Your average amount of guesses is: " + str(averageGuess) + "\n")
        
        #Flag is true to get us out of the loop
        flag = True
    
    #Reset to the main menu
    start_game()

#To Start the whole game - just calling the function
start_game()