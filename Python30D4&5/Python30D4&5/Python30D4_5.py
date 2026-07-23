#1
from math import e


a,b,c,d = 'Thirty','Days','Of','Python'
str1 = a + ' ' + b + ' ' + c + ' ' + d
#2-13
a,b,c = 'Coding','For','All'
company = a + ' ' + b + ' ' + c
print(company,end=' ')
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize(),company.title(),company.swapcase(),company.casefold())

first_word = company.split()[2]
print(first_word)

print(company.__contains__('Coding'))
print(company.find('Coding') > -1)

company = company.replace('Coding','Python')
print(company)
x,y,z = company.split()
print(x,y,z)
#14 - 27
tech_companies ="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
tech_companies_list = tech_companies.split(', ')
print(tech_companies_list[1])

for company in tech_companies_list:
    print(company[0].upper(), end = '')

print('\n')
#28 - 36
str3 = 'You cannot end a sentence with because because because is a conjunction'
str3 = str3[str3.index('because'):str3.rindex('because') + len('because')]
print(str3)

str4 = '   Coding For All      ' 
str4_peeled = str4.split()[0] + ' ' + str4.split()[1] + ' ' + str4.split()[2]
print(str4_peeled)

str5_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(str5_list))