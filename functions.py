import random
def play():
    guess_limit=3
    while guess_limit > 0:
        user= int(input("Enter your guess Number: "))
        computer = random.choice(range(10))
        if user == computer:
            print(f"Guess Number is {computer}, You won!")
            return
        
        else:
            guess_limit -=1
            print(f"Guess Number is {computer}, You Lose! \nAttempts remains {guess_limit}")
    print("Attempt exceeded. Game over ")

def about():
    print("This is a simple guessing game where you have to guess a number between 0 and 9. \nYou have 3 attempts to guess the correct number.")

def exit():
    print("Exiting App")    

