cur_weight=int(input("Please enter your current earth weight: "))
print("I have information for the following planets:\n\t 1. Venus\t 2. Mars\t 3. Jupiter\n \t 4. Saturn\t 5. Uranus\t 6. Neptune\n")
planet=int(input("Which planet are you visiting? "))
def space_box(cur_weight,planet):
    if planet==1:
        return 0.78
    if planet==2:
        return 0.39
    if planet==3:
        return 2.65
    if planet==4:
        return 1.17
    if planet==5:
        return 1.05
    if plnet==6:
        return 1.23
result=space_box(cur_weight,planet)
print(f"Your weight would be {result} pounds on that planet.")