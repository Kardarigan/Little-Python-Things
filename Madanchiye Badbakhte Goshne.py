money = 50
energy = 8
crystals = 0
tools = 0
tool_kharab = 3 
print ("hey there! these are the things you've got : \n money: 50 \n energy: 8 \n crystals: 0 \n tools:0 \n choose your first action: \n buy tools (spend 10 ) \n mining (you lose some energy(you cant do it without having tools)) \n eat (spend 7, gain one energy) \n sell crystals(you should mine first)\n you'll win if you get 15 crystals and you'll lose if your money gets negative:)")
while True:
    choice = input("Enter your action: ")
    if choice == "buy tools":
        money -= 10
        tools += 1
        print("congrats! you have a tool! you can start mining.")
        
    elif choice == "mining":
        if tools > 0 and energy > 2: 
            energy -= 2
            crystals += 1
            tool_kharab -= 1
            print("you found a crystal!")
            if tool_kharab < 1:
                tools -= 1
                tool_kharab = 5
                print("Oh no! your tool broke! you must buy a new one.")
                print("tools:", tools)

        else:
            print("you cant mine right now...buy some tools first...")
        
    elif choice == "eat":
        money -= 7
        energy += 1
        print("now youre energetic again!but youve lost some money/")

    elif choice == "sell a crystal":
        if crystals > 0 :
            crystals -= 1
            money += 10
            print("done! what now?")
    
    else:
        print("ummm... we dont have anything like that...")
    if crystals >= 5:
        print("🎉 YOU WIN! you collected 15 crystals! 🎉")
        break

    if money < 0:
        print("💀 You lost... your money went negative.")
        break
    if energy < 0:
        print("💀 You lost... your energy finished and you died...")
        break
    

    print("----------------")
    print("money:", money)
    print("energy:", energy)
    print("crystals:", crystals)
    print("tools:", tools)
    print("----------------")