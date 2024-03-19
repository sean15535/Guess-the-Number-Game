from functions import play, about, exit
print("Welocme to Guess the Number Game")
while True:
    print("1. Play Game \n2. About Game \n3. Exit")
    response = int(input(">>> "))
    if response == 1:
        play()
    elif response == 2:
        about()
    elif response == 3:
        exit()
        break
    else:
        print("invalid input")