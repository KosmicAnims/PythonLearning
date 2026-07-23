from ast import Compare
from math import sqrt
import pprint
import weakref


print("HIIII!!!")

first_name = "Azear"
last_name = "n/a"
full_name = first_name + " " + last_name
country = "Sot"
age = 12
year_in_adventure = 0
is_married = False
is_true = True
is_Azear = True
height,weight,weapon_choice,is_clan = '5,6', 120, 'dagger', False

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year_in_adventure))
print(type(is_married))
print(type(is_true))
print(type(is_Azear))

print(len(first_name))
Compare(len(first_name), len(last_name))

num1,num2 = 3,24
total = num1 + num2
diff = num2 - num1
product = num1 * num2
quotent = num2 / num1
mod = num2 % num1   
second_powwer = num1**2
floor_div = num2 // num1
pprint.pprint(f"Total: {total}, Difference: {diff}, Product: {product}, Quotient: {quotent}, Modulus: {mod}, Second Power: {second_powwer}, Floor: {floor_div}")

def circle_find_area(radius):
    area =float(radius)*3.14 ** 2
    return area

def circle_find_circumference(area):
    circumference = sqrt(area/3.14) * 2 * 3.14
    return circumference

print('lets do some calculation with Circles')
radius_ = input("what is the radius of the circle? ")
print(f"The area of the circle is: {circle_find_area(radius_)}")
print(f"The circumference of the circle is: {circle_find_circumference(circle_find_area(radius_))}")
help('keywords')