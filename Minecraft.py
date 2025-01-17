#Code to see how a world creation menu might work

print("\nHello Steve! Welcome to World1")

def SurvivalCase(survival_choice):
    if survival_choice == "1":
            print("You chose Easy")
    elif survival_choice == "2":
        print("You chose Normal")
    elif survival_choice == "3":
        print("You chose Hard")
    elif survival_choice == "4":
        print("You chose to Go Back")
        Choice()
    else:
        print("Enter a valid choice!\n\t1 for Easy\n\t2 for Normal\n\t3 for Hard\n\t4 to Go Back")
        survival_choice = input()
        SurvivalCase(survival_choice)
def CreativeCase(creative_choice):
    if creative_choice == "1":
            print("You chose to continue")
    elif creative_choice == "2":
        print("You chose to Go Back")
        Choice()
    else:
        print("Enter a valid choice!\n\t1 to Continue\n\t2 to Go Back")
        creative_choice = input()
        CreativeCase(creative_choice)           
def QuitCase(quit_choice):
        if quit_choice == "1":
            print("Thanks for playing")
        elif quit_choice == "2":
            print("Ok")
            Choice()
        else:
            print("Enter a valid choice!\n\t1 for Yes\n\t2 for No")
            quit_choice = input()
            QuitCase(quit_choice)

def Choice():
    print("\nChoose world type:\n\t1 for Survival\n\t2 for Creative\n\t3 to Quit game")
    world_type = input()
    
    if world_type == "1":
        print("\nYou chose Survival. Select difficulty:\n\t1 for Easy\n\t2 for Normal\n\t3 for Hard\n\t4 to Go Back")
        survival_choice = input()
        SurvivalCase(survival_choice)
        
    elif world_type == "2":
        print("\nYou chose Creative.\nSelect:\n\t1 to Continue\n\t2 to Go Back")
        creative_choice = input()
        CreativeCase(creative_choice)

    elif world_type == "3":
        print("\nAre you sure?\n\t1 for Yes\n\t2 for No")
        quit_choice = input()
        QuitCase(quit_choice)

    else:
        print("Enter a valid choice!")
        Choice()

Choice()
