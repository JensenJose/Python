import random

user_points = 0
computer_points  = 0
name = input("Enter your name: ")

while True:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose Rock/Paper/Scissors or Exit: ").lower()
    if user_input not in options and user_input != "exit":
        print("Invalid input! Please try again!!")
        continue
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game Over")
        break
    
    print("Your input: ", user_input)
    print("Computer's choice: ", computer_input)
    
    if user_input == "rock":
        if computer_input == "rock":
            print("It is a tie!")
        elif computer_input == "paper":
            print("Computer Wons!!")
            computer_points += 1
        elif computer_input == "scissors":
            print("User Won!")
            user_points += 1
    
    elif user_input == "paper":
        if computer_input == "rock":
            print("User Won!")
            user_points += 1
        elif computer_input == "paper":
            print("It is a tie!")
        elif computer_input == "scissors":
            print("Computer Won!")
            computer_points += 1
            
    elif user_input == "scissors":
        if computer_input == "rock":
            print("Computer Won!!")
            computer_points += 1
        elif computer_input == "paper":
            print("User Won!")
            user_points += 1
        elif computer_input == "scissors":
            print("It is a tie!")
            
    print("\n***************")
    print(name, " points: ", user_points)
    print("Computer points: ", computer_points)
    print("***************\n")

