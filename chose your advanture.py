print("You are on a deserted island in a 2D world.")
print("Try to survive until rescue arrives!")
print("Available commands are in CAPITAL letters.")           
print("Any other command exits the program")                  
print("First LOOK around...")
print("You are stuck in a sand ditch.")
print("Crawl out LEFT or RIGHT.")

do = input(":: ").upper()
if do == "LEFT": 
    print("You see a STARFISH and a CRAB on the sand.")
    print("And you're hungry! Which one do you want to eat?")

    do = input(" >>> ").upper()
    
    if do == "STARFISH":
        
        print("Oh no! You immediately don't feel well.")
        print("You do not survive :(")

    elif do == "CRAB":  
        
        print("Raw crab should be fine, right? YES or NO.")

        do = input(">>> ").upper()
        if do == "YES": 
            print("Ok, You eat it raw. Fingers crossed.")
            print("Food in your belly helps you see a TREE. (YES/NO)")
       
            
            do = input(">> ").upper()
            if do == "YES":  
                print("It's a coconut tree! And you're thirsty!")
                print("Do you drink the coconut water? YES OR NO.")

                do = input(">> ").upper()
                if do == "YES":
                    print("Oh boy. Coconut water and raw crab don't mix.")
                    print("You do not survive :(")
                    quit

                elif do == "NO":  
            
                    print("Good choice.")
                    print("Look! It's a rescue plane! You made it! \o/")
                    quit
            elif do == "NO":
                print("Your last food and crab caused your eye to lost its vision")
                print("You lost your way forever and you dont survive!")
                quit
        
        elif do == "NO": 
            
            print("Well, there's nothing else left to eat.")
            print("You do not survive :(")
        
        else:
            print("Your answer not identified . Retry again !")
            quit
    else:
        print("Your answer not identified . Retry again !")
        quit

elif do == "RIGHT":  
    
    print("No can do. That side is very slippery.")
    print("You fall very far into some weird cavern.")
    print("You do not survive :(")
