name=input("Hey, what's our name? ")
age=int(input(f"Ok, {name}. How old are you? "))
if age<16:
    print(f"You can't drive, {name}")
if age<18:
    print(f"You can't vote, {name}")
if age<25:
    print(f"You can't rent a car, {name}")
if age>=25:
    print(f"You can do anthing that's legal, {name}")


