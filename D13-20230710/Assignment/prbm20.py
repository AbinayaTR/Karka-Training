# sum=0
# for i in range(100):
#     num=int(input("Number:"))
#     if num==0:
#         break
#     else:
#         sum+=num
#         print(f"The total so far is {sum}")
# print(f"The total is {sum}")

sum=0
checkOut = True
while checkOut:
    num=int(input("Number : "))
    if num != 0 :
        sum+=num     
        # print(f"The total so far is {sum}")
    else : 
        checkOut=False
print(f"The total is {sum}")

    
    
