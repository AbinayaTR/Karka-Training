day_num=int(input("Enter the weekday :" ))
def week_day(day):
    if day_num==1:
        return "Sunday"
    if day_num==2:
        return "Monday"
    if day_num==3:
        return "Tuesday"
    if day_num==4:
        return "Wednesday"
    if day_num==5:
        return "Thursday"
    if day_num==6:
        return "Friday"
    if day_num==7 or day_num==0:
        return "Saturday"
    else:
        return "error" 
result=week_day(day_num)
print(f"Today is a {result}")

