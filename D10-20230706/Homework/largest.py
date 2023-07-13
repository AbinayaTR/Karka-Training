lst=[1,100,300,4,500,-200]
def largest(num):
    max=num[0]
    for x in num[1: ]:
        if x>max:
           max=x
    return max
result=largest(lst)
print(result)
