
#Hellooo were doing ifs and loops tdy(they behave mostly like c# but cooler)
cond = True

# syntax
if cond:
    print(':) the condition is true') #true
else:
    print(':( the conditon is false') # false

#else-if syntax
a = 5
if a > 0:
    print(f'{a} is positive')

elif a < 0:
    print(f'{a} is negative')

else:
    print(f'{a} is 0')

#shorthand
print("I'm positive a is positive") if a > 0 else print('a is negative mb')

#im not re-explaining nested if 

# Operaters
if a > 0 and cond: # &&
    print('Both are true')
elif a > 0 or cond: # ||
    print('One is true')

if (a>0 and cond) or a > 50:
        print('sometihing was meant ig')

# Exercises
age = int(input('Enter your age: '))

if age >= 16:
    print('You can get a permit. Practice then take the test!')
else:
    print(f'You will have to wait {16-age} years to drive.')


person= {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print(f"{person['first_name']} has some skills")

    if 'Python' in person['skills']:
        print('They can even code in Python!!!')

    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('I predict they are a front-end dev, maybe.')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} has a partner and lives in Finland.")



#Loops Time!!!

#Syntax(while)
cond = True
count = 0;
while cond:
    break

#or

while count < 10:
 print(count) 
 count = count + 1
 #output will be 1 -> 9
else:
    print(count) # 10

#continue skips the current loop
    count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
    #The above while loop only prints 0, 1, 2 and 4 (skips 3).



#Syntax(for) there no more i++, its basically foreach... forever!
lst = [1,2,4,8,16,32,64]
str1 = 'python'
for item in lst:
    print(item)

# how to get letters from a string :o
for letter in str1:
    print(letter)

for index in range(len(str1)): #range is a set of numbers btw
    print(str1[index])

for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

for i in str1:
    pass # does literaly nothing

r1 = range(0,10,2) # strat, end (index so - 1) ,increment!!!
print(r1)

#exercises
r1 = range(11)
#ramp
for out1 in r1:
    for in1 in range(out1):
        print('#', end='')
    if out1 != 0:
     print()


rows = range(10)
cols = range(11)
#box
for row in rows:
    for col in cols:
          print ('#', end= '') if col != len(cols)-1 else print('#')

m = range(11)
for num in m:
    print(f'{num} x {num} = {num*num}')

#I understand it now.
       