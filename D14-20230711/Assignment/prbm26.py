def add_keychains():
    return "ADD KEYCHAINS"
def remove_keychains():
    return "REMOVE KEYCHAINS"
def view_order():
    return "VIEW ORDER"
def checkout():
    return "CHECK OUT"
print("Ye Olde Keychain Shoppe\n\n1. Add Keychains to Order \n2. Remove Keychains from Order \n3. View Current Order \n4. Checkout")
for i in range(50):
    choice=int(input("Please enter your choice : "))
    if choice==4:
        result=checkout()
        print(result)
        break
    elif choice==3:
        result=view_order()
        print(result)
    elif choice==2:
        result=remove_keychains()
        print(result)
    elif choice==1:
        result=add_keychains()
        print(result)
    else:
        print("Wrong Choice")
        break
        
