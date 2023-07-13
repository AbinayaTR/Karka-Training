# print("+------------------------------------+")
# print("| 1 |        Tamil   |       Mr. Ram |")
# print("| 2 |      English   |     Mr. James |")
# print("| 3 |        Maths   |      Ms. Jeba |")
# print("| 4 |      Science   |     Mr. Radha |")
# print("| 5 |       Social   |      Ms. Ravi |")
# print("+------------------------------------+")

# sub1="Tamil"
# sub2="English"
# sub3="Maths"
# sub4="Science"
# sub5="Social"
# name1="Mr. Ram"
# name2="Mr. James"
# name3="Ms. Jeba"
# name4="Mr. Radha"
# name5="Ms. Suji"
# print("+"+('-'*48)+"+")
# print("| 1 |{:>25} | {:>15} |".format(sub1,name1))
# print("| 2 |{:>25} | {:>15} |".format(sub2,name2))
# print("| 3 |{:>25} | {:>15} |".format(sub3,name3))
# print("| 4 |{:>25} | {:>15} |".format(sub4,name4))
# print("| 5 |{:>25} | {:>15} |".format(sub5,name5))
# print("+"+('-'*48)+"+")

subjects=("Tamil","English","Maths","Science","Social")
names=("Ram","Ravi","James","Suji","Jeba")
border="+"+('-'*51)+"+"
print(border)
print("| {} |{:>25} | {:>15} |".format("S.No","Subjects","Teachers"))
print(border)
for i in range(len(names)):
    print("| {:=4} | {:>24} | {:>15} |".format(i+1,subjects[i],names[i]))
print(border)