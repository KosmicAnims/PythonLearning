# Triangle Class

base = float( input ("Enter the base of the triangle: ") )
height =float( input ("Enter the height of the triangle: ") )
area = 0.5 * base * height

print('Area ', area)

print("\n===Time for the next CHALLENGE triangle===")
a = float(input('Enter a value for side A: '))
b = float(input('Enter a value for side B: '))
c = float(input('Enter a value for side C: '))
print('The perimeter of the triangle is: ', a + b + c)

print("\n===Time for the next CHALLENGE rectangle===")
width = float(input('Enter a value for width: '))
length = float(input('Enter a value for length: '))
print('The perimeter of the rectangle is: ', 2 * (width + length))

print("\n===Time for the next CHALLENGE circle===")
radius = float(input('Enter a value for radius: '))
print('The circumference of the circle is: ', 2 * 3.14 * radius)
print('The area of the circle is: ', 3.14 * radius * radius)

print("\n===Time for the next CHALLENGE slope===")
x1 = float(input('Enter a value for x1: '))
y1 = float(input('Enter a value for y1: '))
x2 = float(input('Enter a value for x2: '))
y2 = float(input('Enter a value for y2: '))

print('\nThe slope between (', x1, ',', y1, ') and (', x2, ',', y2, ') is: ', (y2 - y1) / (x2 - x1))
print('okay im just gonna get through the rest of the challenges now')
p = 'python'
d = 'dragon'
print('Are the lengths of "python" and "dragon" equal?', len(p) == len(d))
print('is "python" in "dragon"?', p in d)
