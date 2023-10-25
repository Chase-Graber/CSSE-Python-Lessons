"""
Name: Chase Graber

Lesson 3: Booleans, User input, random library

Class: CSSE, Guillaume, Tri 1 2023
Date: 9/5/23
Period: 2

Description:
    Students will understand that boolean values are either true or false
    Students will be able to accept input from the user and use it in code
    Students will be able to generate random numbers
"""

# BOOLEANS
is_sleeping = True # is_sleeping is a boolean
print(is_sleeping)
print(type(is_sleeping))

if is_sleeping:
    print('Wake up little boy. It\'s breakfast time...')
    is_sleeping = False

print('Is the little boy still asleep? ' + str(is_sleeping))

# # USER INPUT
name = input('What\'s your name: ')
print(name)
print(type(name))

age = input('How old are you: ')
print('You are ' + age + ' years old!?')
print(type(age))

# RANDOM LIBRARY
import random

# Note: randrange(a, b) give random num between a and b-1

num = random.randrange(0, 5) # 0-4
print(num)
num2 = random.randrange(3,100)
print(num2)
