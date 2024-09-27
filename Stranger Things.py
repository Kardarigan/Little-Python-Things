S = True

def start_game():
    print("welcme to the Stranger Things game! ")
    print("You are in the town of Hawkins, Indiana.")
    print("It\'s a dard night, strange thins are happening. ")
    first_choice()

def first_choice():
    print("\n You are sitting at home when you hear a strange noise from outside.")
    print("what do you want to do?")
    print("1. Go outside and see what\'s going on. ")
    print("2. Stay inside and watch TV. ")

    choice = input("Enter your choice (1/2): ")
     
    if choice == '1' :
        go_outside()
    if choice == '2':
        stay_inside()
    else:
        print("Enter a valid choice. ")
        first_choice()

def go_outside():
    print("\nYou go outside notice a strange light in the sky. ")
    print("suddenly, a bizarre creature emerges from the woods! ")
    print("what do you want to do?")
    print("1. Run away.")
    print("2. Talk to the creature.")

    choice = input("Enter your choice (1/2): ") 

    if choice == '1' :
        run_away()
    if choice == '2':
        talk_to_creature()
    else:
        print("Enter a valid choice. ")
        go_outside()

def stay_inside():
    print("\nYou stay inside and watch TV")
    print("But suddenly, the power goes out and everything goes dark.")
    print("what do you want to do? ")
    print("1. Go to the bedroom.")
    print("2. Find a flash light.")

    choice = input("Enter your choice (1/2): ") 

    if choice == '1' :
        go_to_bedroom()
    if choice == '2':
        find_flashlight()
    else:
        print("Enter a valid choice. ")
        stay_inside()

def run_away():
    print("\nyou run back home, but the creature gets closer! ")
    print("you take a side street and notice a group of your friends.")
    print("what do you want to do? ")
    print("1. Join your friends.")
    print("2. Escape alone.")
    
    choice = input("Enter your choice (1/2): ") 

    if choice == '1' :
        join_friends()
    if choice == '2':
        alone_escape()
    else:
        print("Enter a valid choice. ")
        run_away()

def talk_to_creature():
    print("you talk to the creature and realize it\'s just an innocent being.")
    print("it tells you it needs help.")
    print("what do you want to do? ")
    print("1. Help it.")
    print("2. Walk anyway from it.")
    
    choice = input("Enter your choice (1/2): ") 

    if choice == '1' :
        help_creature()
    if choice == '2':
        run_away()
    else:
        print("Enter a valid choice. ")
        talk_to_creature()

def go_to_bedroom():
    print("you go to the bedroom and find it dark as well.")
    print("Suddenly, you hear a noise coming from the closet! ")
    print("what do you want to do? ")
    print("1. open the closet.")
    print("2. Run away.")
    
    choice = input("Enter your choice (1/2): ") 

    if choice == '1' :
        open_closet()
    if choice == '2':
        run_away()
    else:
        print("Enter a valid choice. ")
        go_to_bedroom()

def find_flashlight():
    print("\nyou find a flash light and turn it on.")
    print("with the light, you see a creature standing next to you!")
    print("what do you want to do? ")
    print("1. attack it with the flashlight.")
    print("2. Stay calm and see what happens.")
    choice = input("Enter your choice (1/2): ") 

    if choice == '1' :
        attack_creature()
    if choice == '2':
        calm_down()
    else:
        print("Enter a valid choice. ")
        find_flashlight()

def join_friends():
    print("\nyou join your friends and decide to head into the woods together.")
    print("in the woods, you find a strange portal to another world!")
    print("what do you want to do? ")
    print("1. go through the portal.")
    print("2. turn back and stay away.")

    choice = input("Enter your choice (1/2): ") 

    if choice == '1' :
        go_to_portal()
    if choice == '2':
        run_away()
    else:
        print("Enter a valid choice. ")
        join_friends()

def alone_escape():
    print("\nYou escape alone and eventually return home.")
    print("but thr creature is still around, and you can\'t find peace.")
    end_game()

def open_closet():
    print("You open the closet and find no one there, but you discover a note: ")
    print("i\'m still here ...")
    end_game()

def attack_creature():
    print("you attack the creature with the flashlight, but it simply runs away.")
    end_game()

def calm_down():
    print("\nYou stay calm, and the creature gets closer, It\'s just a lost child")
    end_game()

def go_to_portal():
    print("\nYou step through the portal and enter upside down!")
    end_game()

def help_creature():
    print("\nYou help the creature and it guides you to another world!")
    print("threr, you find new friends and embark on new adventures!")
    end_game()

# end of the game 
def end_game():
    print("\nthe game has ended. I hope you enjoyed the experience!")
    print("Do you want o play again? ") 
    print("1.yes")
    print("2.no")
    
    command = input("Enter your choice (1/2): ")
    if command =='1':
       return False 
    if command == '2':
       return True


while S:
    start_game()
    if end_game():
        S = False
    