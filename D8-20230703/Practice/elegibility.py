passed_out_year=int(input("Enter the year :"))
cgpa=int(input("Enter the cgpa :"))
def is_elegible(passed_out_year,cgpa):
    return passed_out_year>2021 and cgpa>7
result=is_elegible(passed_out_year,cgpa)
print(result) 
