import string
import random

characters = (string.ascii_letters + string.digits + "!@#$%^&+()")

def generate_password():
    password_length = int(input("Enter the length of your password: "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = "".join(password)
    
    print(password)
    
    
option = input("Do You want to generate a password? Yes/No \n")
if(option == "Yes"):
    generate_password()
elif(option == "No"):
    print("Program terminated")
    quit()
else:
    print("Invalid input\n\nPlease try again!")
    quit()
