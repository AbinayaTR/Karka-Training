print("WELCOME TO MITCHELL'S TINY ADVENTURE!\n")
room=input("You are in a creepy house! Would you like to go \"upstairs\" or int the \"kitchen\"?\n")
if room=="kitchen":
    r1=input("\nThere is a long countertop with dirty dishes everywhere. off to one side there is, as you'd expect a refrigerator. You may open the \"refrigerator\" or look in a \"cabinet\".\n")
    if r1=="refrigerator":
        choice=input("\nInside the refrigertor you see food and stuff. It looks prety nasty. Would you like to eat some of the food? (\"yes\" or \"no\")")
        if choice=="yes":
            print("\nDon't eat this")
        else:
            print("\nYou die of starvation... eventualy")
    if r2=="cabinet":
        choice=input("\n Inside the cabinet there is a snacks. Do you need to eat this?")
        if choice=="yes":
            print("\nEnjoy the snacks")
        else:
            print("\nOkay, come when you are hungry")
if room=="upstairs":
    r3=input("\nOne side there is a bedroom and other side there is balcony. You may choose bedroom or balcony?\n")
    if r3=="bedroom":
        choice=input("\nInside the bedroom there is a bed would you like to take rest?\n")
        if choice=="yes":
            print("\nTake rest")
        else:
            print("\nokay do your work")
    if r3=="balcony":
        choice=input("\nWould like to take a cup of coffee?")
        if choice=="yes":
            print("\nEnjoy your coffee")
        else:
            print("\nTake a nap")