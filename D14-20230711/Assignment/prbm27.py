cur_keychain=0
price=10
def add_keychains():
    global cur_keychain
    add=int(input(f"You have {cur_keychain} keychains. How many to add? "))
    cur_keychain+=add
    return f"You now have {cur_keychain} keychains"
def remove_keychains(cur_keychain):
    remove=int(input(f"You have {cur_keychain} keychains. How many to remove? "))
    cur_keychain-=remove
    return f"You now have {cur_keychain} keychains"
def view_order(cur_keychain,price):
    return f"You have {cur_keychain} keychains.\nKeychains cost $10 per each.\nTotal cost is {cur_keychain*price}"
def checkout(cur_keychain,price):
    name=input("What is your name? ")
    return f"You have {cur_keychain} keychains.\nKeychains cost $10 per each.\nTotal cost is {cur_keychain*price}\nThanks for your order, {name}"
for i in range(50):
    print("Ye Olde Keychain Shoppe\n\n1. Add Keychains to Order \n2. Remove Keychains from Order \n3. View Current Order \n4. Checkout")
    choice=int(input("Please enter your choice : "))
    if choice==4:
        result=checkout(cur_keychain,price)
        print(result)
        break
    elif choice==3:
        result=view_order(cur_keychain,price)
        print(result)
    elif choice==2:
        result=remove_keychains(cur_keychain)
        print(result)
    elif choice==1:
        result=add_keychains()
        print(result)
    else:
        print("Wrong Choice")
        break