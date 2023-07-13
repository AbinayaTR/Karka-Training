passed_out_year=input("Enter the passed out year :")
cgpa=input("Enter the cgpa :")
passed_out_year=int(passed_out_year)
cgpa=int(cgpa)
# type_of_passed_out_year=type(passed_out_year)
# print(type_of_passed_out_year)
is_elegible=passed_out_year>2021 and cgpa>7
# is_elegible=passed_out_year>2021 or cgpa>7
# is_elegible=not cgpa<6
if is_elegible:
    print("The student is elegible")
else:
    print("The student is not elegible")
