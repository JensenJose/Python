import random

#FUNCTION FOR USER BATTING
def batting(name):
    print("\nBATTING: ", name)
    print("BOWLING: COMPUTER")
    user_score = 0
    while(1):
        run = int(input("Enter a number between 1 and 6: "))
        pc_val = random.randint(1, 6)
        print("Computer: ", pc_val)
        if run>6 or run<=0:
            print("Please enter a valid number!")
        elif run == pc_val:
            print("OUT!")
            break
        else:
            user_score += run
            print("YOUR SCORE: ", user_score)
    print("\n***********************")
    print("YOUR FINAL SCORE IS ", user_score)
    return user_score

#FUNCTION FOR USER BOWLING    
def bowling(name):
    print("\nBOWLING: ", name)
    print("BATTING: COMPUTER")
    pc_score = 0
    while(1):
        ball = int(input("Enter a number between 1 and 6: "))
        pc_run = random.randint(1, 6)
        if ball>6 or ball<=0:
            print("Please enter a valid number!")
        elif ball == pc_run:
            print("OUT!")
            break
        else:
            print("COMPUTER RUN: ", pc_run)
            pc_score += pc_run
    print("\n***********************")
    print("PC's FINAL SCORE IS ", pc_score)
    return pc_score

#FUNCTION FOR TOSS
def toss(name):
    user_choice = input("ODD/EVEN: ").lower()
    user_toss = int(input("Enter a number between 1 and 6: "))
    pc_toss = random.randint(1, 6)
    print("You entered: ", user_toss)
    print("PC entered: ", pc_toss)
    if user_choice == 'odd' and ((user_toss + pc_toss) % 2 != 0):
        print(name, " has won the toss!")
        return 1
    elif user_choice == 'even' and ((user_toss + pc_toss) % 2 == 0):
        print(name, " has won the toss!")
        return 1
    else:
        print("PC has won the toss!\n")
        return 0

#MAIN FUNCTION
print("WELCOME TO HANDCRICKET!!")
name = input("Enter your name: ")
print("LET THE GAMES BEGIN!!")
val = toss(name)
user_runs = 0
pc_runs = 0
if val == 1:
    choice = input("BATTING/BOWLING: ").lower()
    if choice == 'batting':
        user_runs = batting(name)
        pc_runs = bowling(name)
    elif choice == 'bowling':
        pc_runs = bowling(name)
        user_runs = batting(name)
    else:
        print("Invalid input!")    
else:
    val = random.randint(0, 1)
    if val == 1: 
        #PC is batting
        pc_runs = bowling(name)
        user_runs = batting(name)
    else:
        #PC is bowling
        user_runs = batting(name)
        pc_runs = bowling(name)
if user_runs > pc_runs:
    print("\n", name, " HAS WON THE GAME!!!")
elif user_runs == pc_runs:
    print("DRAW!!!")
else:
    print("OOPS! YOU've LOST THE GAME!:(")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    