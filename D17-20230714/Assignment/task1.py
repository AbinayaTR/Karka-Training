student_details=[{"name":"Abi","age":22,"place":"Nagercoil"},
    {"name":"Achu","age":20,"place":"Nagercoil"},
    {"name":"Alfee","age":22,"place":"Nagercoil"},
    {"name":"vajee","age":21,"place":"Nagercoil"},
    {"name":"Valli","age":22,"place":"Nagercoil"}]
# for i in range(5):
#     print(f"I am {student_details[i]['name']}.I'am {student_details[i]['age']} years old,and I'm from {student_details[i]['place']}")
#     i+=1

# i=0
# for std_detail in student_details:
#     print(f"I am {student_details[i]['name']}.I'am {student_details[i]['age']} years old,and I'm from {student_details[i]['place']}")
#     i+=1
def print_func():
    for std_detail in student_details:
        print(f"I am {std_detail['name']}.I'am {std_detail['age']} years old,and I'm from {std_detail['place']}")
print_func()

def check_age():
    for std_detail in student_details:
        if std_detail['age']>21:
            print(f"I am {std_detail['name']}.I'm from {std_detail['place']}")
check_age()