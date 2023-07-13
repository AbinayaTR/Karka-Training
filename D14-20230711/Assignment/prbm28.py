cur_keychain=0
tax=8.25/100
base_shipping=5
per_keychain_shipping=1
def add_keychains(keychain):
    add=int(input(f"You have {keychain} keychains. How many to add? "))
    return cur_keychain+add
    print(f"You now have {keychain} keychains")
def remove_keychains(keychain):
    # global cur_keychain
    remove=int(input(f"You have {keychain} keychains. How many to remove? "))
    if remove>cur_keychain:
        print(f"Error:You have only {keychain} keychains.\nBut you entered {remove} keychains")
    elif remove<=0:
        print(f"Enter a valid number of keychains")
    else:
        return keychain-remove
        print(f"You now have {cur_keychain} keychains")
    return keychain
def view_order():
    return f"You have {cur_keychain} keychains.\nKeychains cost $10 per each.\nShipping charges on the order {base_shipping}.\n"
def checkout():
    global cur_keychain
    name=input("What is your name? ")
    return f"You have {cur_keychain} keychains.\nKeychains cost $10 per each.\nTotal cost is {cur_keychain*price}\nThanks for your order, {name}"
print("Ye Olde Keychain Shoppe\n\n1. Add Keychains to Order \n2. Remove Keychains from Order \n3. View Current Order \n4. Checkout")
while True:
    choice=int(input("Please enter your choice : "))
    if choice==4:
        result=checkout()
        print(result)
        break
    elif choice==3:
        result=view_order()
        print(result)
    elif choice==2:
        cur_keychain=remove_keychains(cur_keychain)
        print(cur_keychain)
    elif choice==1:
        cur_keychain=add_keychains(cur_keychain)
        print(cur_keychain)
    else:
        print("Wrong Choice")
        break