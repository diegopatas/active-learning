# Program to list several types of list of numbers
## Printing 1 to 20
for i in range(1,21):
    print(i)
## Printing odd numbers
for i in range(1, 21, 2):
    print(i)
## Printing multiples of 3
for i in range(1, 11):
    print(i*3)
## Printing cubes
for i in range(1,11):
    print(i**3)
## Printing cubes in a list comprehension
cubes = [i**3 for i in range(1,11)]
print(cubes)