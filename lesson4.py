"""
Name: Chase Graber

Date: 9/6/23
Class: CSSE, Guillaume, Tri 1 2023
Lesson 4: Selection (conditionals)

Description:
    Students will be able to use condiational statements to program the computer to make decisions
"""

# Selection: a programming construct where a section of code is run only if a condition is met

# IF STATEMENT
x = 36
if x > 2:
    print("That number is greater than 2")

name = 'nico'
if name == 'nico':
    print("Your name is nico")

isGreen = False
if isGreen:
    print('It\'s green')

# IF/ELSE STATEMENTS
isBlue = False
if isBlue:
    print('It\'s blue')
else:
    print('It\'s not blue')

myNumber = 4092657123498
if myNumber > 25:
    print('That number is greater than 25')
else:
    print('That number is less than or equal to 25')

# IF/ELIF/ELSE STATEMENTS
num2 = 6
if num2 > 3:
    print('That number is greater than 3')
elif num2 == 3:
    print('That number is equal to 3')
else:
    print('That number is less than 3')

# NESTED IF/ELSE STATEMENTS
numCats = 2
if numCats < 3:
    if numCats == 3:
        print('You have 3 cats')
    else:
        print('Coward')
else:
    print('How many scars do you have')
