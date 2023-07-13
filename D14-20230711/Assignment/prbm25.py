months=["January","February","March","April","May","June","July","August","September","October","November","December"]
def month_name(i):
    # i-=1   
    return months[i-1]
result=month_name(7)
print(result)