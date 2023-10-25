"""
Lesson 1: Comments, printing, variables, sequencing

Name: Chase Graber
Date: 8/28/23
Cource Name: CSSE, Guillaume, Tri 2023

Description:
    Students will be able to print in python.
    Students will be able to use variables in python.
    Students will understand that sequencing means the specific order in which instructions are performed in a program.
"""

# PRINTING
print('Hello World!')
print('My name is Chase')
print('My name is Chase \n') # Use '\' and not '/'. There is a difference!

#VARIABLES
name = 'Chase'
print(name)
print('Hello, my name is ' + name) # Concatenate (concat): Combining strings
print('Hello,', name, "!")

number = 345.1
print(number)
print('My nuber is ' + (str)(number))

print(type(name))
print(type(number))

num1 = 2
num2 = -3
my_sum = num1 + num2
print('The sum of ' + (str)(num1) + ' and ' + (str)(num2) + ' is equal to ' + (str)(my_sum))

camelCase = 2
print(camelCase)
