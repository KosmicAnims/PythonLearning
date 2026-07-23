# Set is a collection of unordered and un-indexed distinct elements.sooo kinda like list but without everything cool

#making sets




setA = {}
setB = set()
setC = {'item1', 'item2', 'item3'}

#important functions
setC.add('item4') 
setC.remove('item1') 
setC.pop() #removes a random item from the set
removed_item = setC.pop() 
setC.clear() #removes all items from the set

setC = {'item1', 'item2', 'item3'}
setD = {'item4', 'item5', 'item6'}
union_set = setC.union(setD) #combines two sets into one via | (.update() does the same lol but modifies the original set) 
inboth_set = setC.intersection(setD) #returns a set of items that are in both sets via & or : (.intersection_update() does the same but modifies the original set) is returns nothing btw

setC = {1,2,3,4,5,5,6,7,8,9,10}
setD = {2,4,6,8,10}

setD.issubset(setC) #returns True think d is a subset of c
setC.issubset(setD) #returns false c is not a subset of d(C has more items than D)

#issuperset is the opposite of subset, it checks if the set is a superset of another set

setC.difference(setD) #returns a set of items that are in setC but not in setD via -. {3,5,7,9}
setC.symmetric_difference(setD) #returns a set of items that are in either setC or setD but not in both via ^. {1,3,5,7,9})

setC.isdisjoint(setD) #returns True if the two sets have no items in common.(false btw they have 2,4,6,8,10 in common)
print(setA,setB, setC, setD, union_set, inboth_set)

# sets exercises
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

a = len(it_companies)
it_companies.add('twitter')
it_companies.update(['OpenAI','Claude'])
it_companies.remove('Google')
#discard dosen't care if its there or not

C = A.union(B)
C = A.intersection(B)
disjointed = A.isdisjoint(B)
A.update(B)
B.update(A)
C = A.symmetric_difference(B)
del A
del B
del C
del it_companies

age_lst = list(age)
lst_isbigger = len(age_lst) > len(age)

#big problem! count the number of unique words in a sentence and print them out
sentence = 'I am a teacher and I love to inspire and teach people'
setA = sentence.split()
setA = set(setA)
#sets are all about distinct elements so it will automatically remove duplicates
print(setA)


#Enough about sets! really quick lets do dictionaries!

#dictionaries are a collection of unordered, changeable and indexed key-value pairs! They are written with curly brackets, and have keys and values.
person = {
    'first_name': 'John', # this is a Item1(key) and value1 pair
    'last_name': 'Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'SQL']
}

# accessing items in a dictionary

print(person['first_name']) #accessing the value of a key)
print(person['last_name']) #accessing the value of a key)
print(person['age']) #accessing the value of a key)
print(person['skills'][2]) #accessing the value of a key)

#bettter way is .get() method
# u cant access via value btw

print(person.get('first_name'))  #accessing the value connected to the key
print(person.get('skills')[1]) #accessing the value connected to the key

#adding items to a dictionary

person['country'] = 'USA' #adding a new key-value pair to the dictionary)
person['skills'].append('CSS') #adding a new value to the list connected to the key 'skills'

#converting a dictionary to a list
person_lst = list(person.items()) #returns a list of tuples containing the key-value pairs in the dictionary
#etc
'skills' in person 
person.pop('age')
person.popitem() #removes the last inserted key-value pair
# remove and return the first skill
first_skill = person['skills'].pop(0)

#Exercises
dog = {'name': 'davonte brownly jr',
      'age': 3, 
      'breed': 'chinu',
     'color': 'brown', 
      'is_friendly': False
}

student = {'first_name': 'alex', 
           'last_name': 'johnson', 
           'age': 16, 
           'skills': ['Python', 'JavaScript', 'SQL'],
           'Gpa': 4.1
}

print (len(student)) # 5
print (type(student['skills'])) # <list>
student['skills'].append('HTML') # add 'HTML' to skills
print (list(dog.keys()))
print (list(dog.values()))  
# bye im done now

