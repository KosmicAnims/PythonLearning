# Learning ppthon func and mods lol

#syntax

score = 500
multi = 3

def getScore(s,m):
    true_score = s*m
    return true_score # you have to return something always

print('Your score: ', getScore(score,multi))
#we know thwe other stuff  
true_score = getScore(500,3)
#default parameters
def greetings (name = 'Peter'): # if its empty we give it an automatic value
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh')) 

#abitrary value(if you dont know or dont care about how many parameters of the specific value)
def get_alltime_score(m,*ts):
    total = 0
    for a in ts:
        total += a*m
    return total
print('Your all-time score:', get_alltime_score(1.7,true_score,1000,3,400,9999))

 # Unpacking a dictionary in a func
def greet(name, location):
    print("Hi there", name, "how is the weather in", location)

greet(name="Alice", location="New York")  # Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)  # The ** operator unpacks the dictionary, passing its key-value pairs as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York


#exercise
def sum(*num):
    for a in num:
        sum_ += a
    return sum_
     
def check_season(month):
    month = string(month)
    if month.lower() == 'september' or 'november' or 'october':
        return 'Fall'
    elif  month.lower() == 'december' or 'january' or 'febuary':
        return 'Winter'
    else:
        return 'its just hot vru'

def reverse_list(lst):
    return list(reversed(lst))

# the other stuff is a bit more difficult but nothing i haven't done before onto Modules.
# they are basically classes that contain commonly used set of functions this file has even made some

import os
# Creating a directory aka a folder in YOUR os
#os.mkdir('directory_name')
# Changing the current directory
#os.chdir('path')
# Getting current working directory
#os.getcwd()
# Removing directory
#os.rmdir()

import sys
# This one gather infomtion passed thru the system while it runs
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
#print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
# to exit sys
#sys.exit()
# To know the largest integer variable it takes
#sys.maxsize
# To know environment path
#sys.path
# To know the version of python you are using
#sys.version
import math
from statistics import * # imports all (*) stat stuff idk
from math import pi, sqrt, pow, floor, ceil, log10 # you can import functions one by one
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2


# You can also rename the imported functions
from math import pi as PI_
import string
from random import random


#exercise
def random_user_ID():
    character = string.ascii_letters + string.digits
    out = ''
    for item in range(0,6):
       out += character[(int(random()*character.__len__()))]
    return out

print(random_user_ID())