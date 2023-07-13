mixedlist=[1,2.0,"hai","@",5,6,"&",8,9]
real_count=0
for num in mixedlist:
    if type(num)==int:
        real_count+=1
print("Numbers in a mixed list : ",real_count)