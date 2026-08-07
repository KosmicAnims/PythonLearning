#We had a small gap but I'm back hope we make it to day 30!!!

#List compression is a way to write loops in one line basically, then turning that into a list

#syntax what to do wit I is expression
#lst = [expression for i in iterable if condition]


#examples
language = 'Python'
lst = list(language)
print(lst)
# or using list comp
lst = [ i for i in language]   
print(lst)

#example with instance and condition
numbers = [i for i in range(0,20)]
print (numbers)

evens = [i for i in range(0,20) if i%2==0]
print(evens)

even_expos = [i**2 for i in range(0,20) if i%2==0]
print (even_expos)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lamda time!
# they are kinda like a fixer upper for functions, they are a one liner function that can be used in place of a function

# syntax                         what to do with the parameters
#function = lambda param1, param2, param3: param1 + param2 + param3
#print(function(arg1, arg2, arg3))

#Example
add_two_nums = lambda a,b : a + b
print(add_two_nums(1,99))

reverse = lambda lst : lst[::-1]
lst = [1,2,3,4,5]
print (reverse(lst))
# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

#Function Expansion
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32

# Exercise Time !
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positve_filter = [num for num in numbers if num > 0 ]
print (positve_filter)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_lst = [num for row in list_of_lists for num in row]
print (flat_lst)
# lists of tuples
rows = 5
all_tup = [(x,x**1,x**2,x**3,x**4,x**5,x**6,x**7,x**8) for x in range(rows)]
print(all_tup)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
airport = []
for item in countries:
    country = item[0][0]
    code = country[:3].upper()
    item.insert(1, code)
    airport += item

print(airport)


country_city = {}
for item in countries:
    country = item[0][0]
    city = item[0][1]
    country_city[country] = city
print(country_city)