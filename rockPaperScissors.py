import random

weapons = ["r","p","s"]

while True:
    computerChose = random.choice(weapons)
    humanChose = input("Rock Paper Scissors...[r/p/s]")

    if computerChose == humanChose:
        print("Tie!")
    elif computerChose == "r" and humanChose == "p":
        print("You win! i was Rock")
    elif computerChose == "r" and humanChose == "s":
        print("Im win! i was Rock")
    elif computerChose == "s" and humanChose == "p":
        print("Im win!! i was Scissors")
    elif computerChose == "s" and humanChose == "r":
        print("You win! i was Scissors")
    elif computerChose == "p" and humanChose == "s":
        print("You win!! i was Paper")
    elif computerChose == "p" and humanChose == "r":
        print("Im win!! i was Rock")
    elif humanChose == "r" and computerChose == "p":
        print("Im win!! i was Paper")
    elif humanChose == "r" and computerChose == "s":
        print("You win! i was Scissors")
    elif humanChose == "s" and computerChose == "p":
        print("You win! i was Paper")
    elif humanChose == "s" and computerChose == "r":
        print("Im win!! i was Rock")
    elif humanChose == "p" and computerChose == "s":
        print("Im win!! i was Scissors")
    elif humanChose == "p" and computerChose == "r":
        print("You win! i was Rock")