a=int(input("Enter the value a "))
b=int(input("Enter the value b "))
c=int(input("Enter the value c "))
s=(a+b+c)/2
def area_triangle(a,b,c,s):
    return (s*(s-a)*(s-b)*(s-c))**0.5
result=area_triangle(a,b,c,s)
print(f"Area of triangle is {result}")

side=int(input("\nEnter the side "))
def area_square(side):
    return side*side
result=area_square(side)
print(f"Area of square is {result}")

length=int(input("\nEnter the length "))
bredth=int(input("Enter the bredtth "))
def area_rectangle(l,b):
    return length*bredth
result=area_rectangle(length,bredth)
print(f"Area of rectangle is {result}")

radius=int(input("\nEnter the radius "))
def area_circle(r):
    return 3.14*r*r
result=area_circle(radius)
print(f"Area of cicle is {result}")

base1=int(input("\nEnter the base1 "))
base2=int(input("Enter the base2 "))
height=int(input("Enter the height "))
def area_trapezium(base1,base2,height):
    return 1/2*(a+b)*height
result=area_trapezium(base1,base2,height)
print(f"Area of trapezium is {result}")