"""
Name: Chase Graber

Date: 9/7/23
Class: CSSE, Guillaume, Tri 1 2023
Lesson 5: Functions and parameters

Description:
    Students will be able to create functions and abstraction to reduce & reuse code,
"""

# Abstraction: Breaking down complex programs into smaller, more managable parts

def sayHello1():
    print('Hello')

def sayHello2(name):
    print('Hello, ' + name)
    print('The council has been waiting for your arrival.')

def calculate_sum(a, b):
    print('a = ' + str(a))
    print('b = ' + str(b))
    print('a + b = ' + str(a + b))

# Main
sayHello1()
sayHello2('Chase Graber')
print()
sayHello2('Vincint Pennick')

print()
calculate_sum(1,2)
print()
calculate_sum(4,-5)
