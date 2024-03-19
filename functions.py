import random
def play():
    guess_limit=3
    while guess_limit > 0:
        user= int(input("Enter your guess Number: "))
        computer = random.choice([range(10)])
        if user == computer:
            print(f"Guess Number is {computer}, You won!")
            return
        
        else:
            guess_limit -=1
            print(f"Guess Number is {computer}, You Lose! \nAttempts remains {guess_limit}")
    print("Attempt exceeded. Game over ")

    

