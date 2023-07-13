marks=[67,89,87,90,80]
tot_marks=0
# for mark in marks:
    # print("Before iteration",tot_marks)
    # tot_marks+=mark
    # print("After iteration",tot_marks)

enum_marks=enumerate(marks)
print(type(enum_marks))
for i,mark in enum_marks:
    print("Entering the iteration process at index "+str(i))
    print("Before iteration ",tot_marks)
    tot_marks+=mark
    print("After iteration ",tot_marks)
    print("Exiting the iteration process at index "+str(i))
    print("\n")
print(tot_marks)
