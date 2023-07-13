name=input("Hey, what's our name? (Sorry, i keep forgetting.) ")
age=int(input(f"Ok, {name}. How old are you? "))
if age<16:
    print(f"You can't drive, {name}")
elif age==16 or age==17:
    print(f"You can drive but not vote, {name}")
# elif age>18 or age<=24:
#     print(f"You can vote but not rent a car, {name}")
elif 18<age<=24 :
    print(f"You can vote but not rent a car, {name}")
else:
    print(f"You  do pretty much anything, {name}")

