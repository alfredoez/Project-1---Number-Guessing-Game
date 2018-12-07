"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

#Meets Expectations grade

import random

print("W e l c o m e")
print("-----------------")
print("The Gessing Game!")
print("-----------------")

#I use this variables inside the function as global. I google it in StackOverflow and solve my problem.
best_score = 1000



def start_game():
    num = random.randint(1,10)
    global best_score
    score = 0

        
    while True:
        guess_num = int(input("Enter a number between 1-10 "))
        try:
            guess_num = int(guess_num)
            if guess_num not in range (1,10):
                raise ValueError("Please enter a number between 1-10")
        except ValueError as err:
            raise ValueError(f"Something happened! {err}. Please, Try again" )
        else:
            score += 1
            print(score)    
            if guess_num != num:
                if guess_num < num:
                    print("Higher")
                else:
                    print("Lower")
            elif guess_num == num:
                print(f"You Win! \n You made {score} attempts")
                break
    if score < best_score:
        best_score = score
        print("-----------------------")
        print (f"Your best score is: {best_score}")
        print("-----------------------")
    else:
        print("-----------------------")
        print (f"Your best score is: {best_score}")
        print("-----------------------")


#This is the main menu. If you want to play, an if statement call the start_game function.
while True:
    start = input("Do you want to start a new game?(y/n) ")
    if start.lower() == "y":
        if best_score != 1000:
            print("-----------------------")
            print (f"The score you have to beat: {best_score}")
            print("-----------------------")
        start_game()

    elif start.lower() == "n":
        print("See you soon!")
        break
    else:
        print("Please enter a valid input. 'y' for yes, 'n' for no.")
