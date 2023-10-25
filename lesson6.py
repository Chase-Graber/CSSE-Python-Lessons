'''
Name: Chase Graber

Date: 9/8/23
Class: CSSE, Guillaume, Tri 1 2023
Lesson 6: Return values

Description:
    Students will be able to use return values in fuctions to make them more effective
'''

import math

# Functions
def sum(a, b):
    return a + b

def sayHello(firstName, lastName):
    fullName = firstName + ' ' + lastName
    return 'Hello, ' + fullName + '.\nI am closing in on your current location and will be there in under 30 seconds.'

def pythagoranTheorem(a, b):
    cSquare = (a*a) + (b*b)
    return str(int(math.sqrt(cSquare)))

# Main
print('sum: ' + str(sum(4, 7)))
print(sayHello('Chase', 'Graber'))
c = pythagoranTheorem(3, 4)
print('Pythagorean Theorem: ' + c)
