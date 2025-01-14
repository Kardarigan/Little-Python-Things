def start_game():
    print("Welcome to the Martian story gameeee!")
    print("You are an alien from MARS.")
    print("The story start now.The MARS is being destroyed due to human research.")
    first_choice()

def first_choice():
    print("\nYou are the only one left on MARS, the rest of your friends have migrated to JUPITER.")
    print("You have only 2 ways: ")
    print("1. Go to JUPITER like your friends. ")
    print("2. Go to the Earth and taking revenge on humans. ")

    choice = input("Enter your choice (1/2): ")
     
    if choice == '1' :
        Go_to_JUPITER()
    if choice == '2':
        Go_to_EARTH()
    else:
        print("Enter a valid choice. ")
        first_choice()

def Go_to_JUPITER():
    print("\nYou go to JUPIYER to join your friends. ")
    print("You find out that your best friend has a bad disease and yhe only treatmet is a plant that grows on MARS.")
    print("what do you do even though you know that the plant grows in a very dengerous part of the MARS?")
    print("1. Tell to your friend that this is impossible and you don't go.")
    print("2. Return to MARS to find the plant for your friend.")

    choice = input("Enter your choice (1/2): ") 

    if choice == '1' :
        Do_not_go()
    if choice == '2':
        Return_to_MARS()
    else:
        print("Enter a valid choice. ")
        Go_to_JUPITER()

def Go_to_EARTH():
    print("\nYou go to the EARTH. ")
    print("And you realize that you can't do anything alone!")
    print("what do you want to do? ")
    print("1. You go to JUPITER and come back with your friends.")
    print("2. You stay on the EARTH")

    choice = input("Enter your choice (1/2): ") 

    if choice == '1' :
        go_back_with_friends()
    if choice == '2':
        stay_on_EARTH()
    else:
        print("Enter a valid choice. ")
        stay_on_EARTH()

def Do_not_go():
    print("\nYou don't go and your friend gets worse. ")
    print("But luckily, doctors discover a cure for this disease and your friend survive.")
    end_game()

def Return_to_MARS():
    print("You return to the MARS for your friend and after all the problems you managed to find the plant.")
    print("You go back to JUPITER and give the plant to your friend and she is savsd for you!")
    end_game()

def go_back_with_friends():
    print("You return to EARTH eith an army of Martians and take your revenge on humans.")
    print("We arredted a group of people! ")
    print("what do you want to do? ")
    print("1. Kill human")
    print("2. Take human to MARS to clean it.")
    
    choice = input("Enter your choice (1/2): ") 

    if choice == '1' :
        kill_human()
    if choice == '2':
        take_human_to_MARS()
    else:
        print("Enter a valid choice. ")
        take_human_to_MARS()

def stay_on_EARTH():
    print("\nYou stay on EARTH and seeing the behavior of humans with the EARTH.")
    print("You decide to leave human alone because they are destroying the EARTH by their own behavior.")
    end_game()

def kill_human():
    print("Now human want to take revenge on the Martians...")
    end_game()

def take_human_to_MARS():
    print("You take human to MARS to clean it up and they come back to EARTH after that.")
    end_game()

# end of the game 
def end_game():
    print("\nThe game is over.I hope you enjoyed this game!")
    print("Do you want to play again? ") 
    print("1.yes")
    print("2.no")
    
    command = input("Enter your choice (1/2): ")
    if command =='1':
       return False 
    if command == '2':
       return True


while True:
    start_game()
    if end_game():
        break
