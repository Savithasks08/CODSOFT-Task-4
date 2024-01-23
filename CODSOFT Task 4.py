#Python code for a rock paper scissors game

#Import the random module
import random

#Create a list of options
options_List = ["rock", "paper", "scissors"]

#Initialize users_scores and computers_score with zero
users_score = 0
computers_score = 0

#Set the number of rounds
rounds_list = 3

#Define a function game() for rock,paper,scissors game 
def game(users_score,computers_score,rounds_list):
    #Loop through the rounds
    for i in range(rounds_list):
        #Print the current round and scores
        print("\nRound :",i+1)

        #Get the input from the user
        users_choice = input("Choose rock or paper or scissors: ")
        
        #Check the user's input is in the options_List or not using while loop
        while users_choice not in options_List:
            print("Invalid choice. Please try again.")
            users_choice = input("Choose rock or paper or scissors: ")
        
        #Generate a random option for the computer
        computers_choice = random.choice(options_List)
        
        #Print the user and computer choices
        print("\nYou choice: ",users_choice)
        print("\nComputer choice: ",computers_choice) 
            
        #Condition for checking the winner
        if users_choice == computers_choice:

            print("\nIt is a tie!")

        elif users_choice == "rock" and computers_choice == "scissors":

            print("\nYou win!")
            users_score += 1

        elif users_choice == "paper" and computers_choice == "rock":

            print("\nYou win!")
            users_score += 1

        elif users_choice == "scissors" and computers_choice == "paper":

            print("\nYou win!")
            users_score += 1
        
        else:

            print("\nComputer wins")
            computers_score += 1
            print("\n\tFinal scores")
            print("\nUser score is : ",users_score)
            print("\nComputer score is : ",computers_score)
        #End of condition
            
    #The If statement to dispaly the winner
    if users_score > computers_score:

        print("\n\tYou are the winner")

    elif users_score < computers_score:

        print("\n\tComputer is the winner")

    else:

        print("\n\tIt is a Draw")  
    #End of if statement
    
    print("\n\tFinal scores")
    print("\nUser score is : ",users_score)
    print("\nComputer score is : ",computers_score)
    #End of loop
#End of game() function
   
#Calling the function game() for the starting the program
game(0,0,3)