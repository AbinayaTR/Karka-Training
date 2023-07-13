import prbm7
weight=int(input("Your weight in kg : "))
height=float(input("Your height in m : "))
bmi=prbm7.calc_bmi(weight,height)
print(type(bmi))
print(f"Your bmi is {bmi}")
if bmi<18.5:
    print("BMI Category : under weight")
if bmi>=18.5 and bmi<=24.9:
    print("BMI Category : normal weight")
if bmi>=25.0 and bmi<=29.9:
    print("BMI Category : normal weight")
if bmi>=30.0:
    print("BMI Category : obese")   
