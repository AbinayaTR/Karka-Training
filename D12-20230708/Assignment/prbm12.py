
def quiz():
    start=input("Are you ready for a quiz? ")
    score=0
    if start=="yes":
        print("Okay, Here it comes!")
    print("Q1) What is the capital of Alaska?\n\t 1) Melbourne\n\t 2) Anchorage\n\t 3) Juneau\n")
    choice=int(input("Ans : "))
    if choice==1 or choice==2:
        print("Sorry, capital of alaska is Juneau\n")
    else:
        print("That's right!\n")
        score+=1
    print("Q2) Can you store the value \"cat\" in a variable of type int?\n\t 1) yes\n\t 2) no\n")
    choice=int(input("Ans : "))
    if choice==1:
        print("Sorry, \"cat\" is  string. ints can only store number\n")
    else:
        print("That's right!")
        score+=1
    print("Q3) What is the result of 9+6/3?\n\t 1) 5\n\t 2) 11\n\t 3) 15/3\n")
    choice=int(input("Ans : "))
    if choice==1 or choice==3:
        print("Sorry, the result is 11\n")
    else:
        print("That's right!\n")
        score+=1
    print("Overall, you got {} out of {} correct.\nThanks for playing!".format(score,3))

quiz()
 