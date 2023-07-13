gender=input("What is your gender (f or m)?")
frst_name=input("First name : ")
lst_name=input("Last name : ")
age=int(input("Age : "))
if gender=="f" and age<20:
    print(f"Then I shall call you {frst_name + lst_name}")       
if gender=="f" and age>=20:
    mrd_status=input(f"Are you married, {frst_name} (y or n)?")
    if mrd_status=="y":
        print(f"Then I shall call you Mrs. {frst_name}")
    else:
        print(f"Then I shall call you Ms. {frst_name}")
if gender=="m" and age<20:
    print(f"Then I shall call you {frst_name + lst_name}")       
if gender=="m" and age>=20:
    # mrd_status=input(f"Are you married, {frst_name} (y or n)?")
    # if mrd_status=="y":
    print(f"Then I shall call you Mr. {frst_name}")