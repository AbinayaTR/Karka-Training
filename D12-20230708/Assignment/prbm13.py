print("TWO QUESTION!\nThink of an object, and I'll try to guess it.\n")
objects=input("Question 1) Is it animal, vegetable, or mineral?\n")
a="moose"
b="squirrel"
c="watermelon"
d="carrot"
e="camera"
f="paper clip"
if objects=="animal":
    size=input("Question 2) Is it bigger than a breadbox?\n")
    if size=="yes":
        print("moose")
        print(f"My guess is that you are thinking of a {a} \nI would ask you if I'm right. but I don't actually care ")
    else:
        print("squirrel")
        print(f"My guess is that you are thinking of a {b}\nI would ask you if I'm right. but I don't actually care ")
if objects=="vegetable":
    size=input("Question 2) Is it bigger than a breadbox?\n")
    if size=="yes":
        print("watermelon")
        print(f"My guess is that you are thinking of a {c}\nI would ask you if I'm right. but I don't actually care ")
    else:
        print("carrot")
        print(f"My guess is that you are thinking of a {d}\nI would ask you if I'm right. but I don't actually care ")
if objects=="mineral":
    size=input("Question 2) Is it bigger than a breadbox?\n")
    if size=="yes":
        print("Camera")
        print(f"My guess is that you are thinking of a {e}\nI would ask you if I'm right. but I don't actually care ")

    else:
        print("Paper clip")
        print(f"My guess is that you are thinking of a {f}\nI would ask you if I'm right. but I don't actually care ")
