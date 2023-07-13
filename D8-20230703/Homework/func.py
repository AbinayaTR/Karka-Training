num1=int(input("Enter the first number = "))
opr=input("Enter the operator = ")
num2=int(input("Enter the third number = "))
def arithmetic_calc(num1,opr,num2):
    if opr=="+":
        return num1+num2
    elif opr=="-":
        return num1-num2
    elif opr=="*":
        return num1*num2
    elif opr=="/":
        return num1/num2
    elif opr=="%":
        return num1%num2
    elif opr=="**":
        return num1**num2
    else:
        print("wrong operator")
result=arithmetic_calc(num1,opr,num2)
print(result)