"""
Lesson 2: Iteration (While Loops & For Loops)

Name: Chase Graber
Date: 8/30/23
Course: CSSE, Guillaume, Tri 1 2023

Description:
    Students will be able to write while loops in python to repeat code
    Students will be able to write for loops in python to repeat code
    Students will be able to analyze the output of nested loops
"""

# ITERATION: a sequence of instructions or code being repeated until a specific end result is acheived

# WHILE LOOPS: repeat while a condition is true

print('while loop counting down')
x = 3
while x > 0:
    print(x)
    x -= 1

print('\nwhile loop counting up')
y = 10
while y <= 100:
    print(y)
    y += 10

# FOR LOOPS: repeat a set amount of times
print('\nfor loop counting up by 1s from 0 to 5 non-inclusive')
for i in range(5):
    print(i)

print('\nfor loop counting up by 1s from 5 to 10 non-inclusive')
for i in range(5,10):
    print(i)

print('\nfor loop counting by 1000s from -1000 to 1000 non-inclusive')
for example_variable in range(-10000, 10000, 1000):
    print(example_variable)

# NESTED FOR LOOPS
for g in range(2):
    for c in range(4):
        print('hello world')
    print()

# NESTED WHILE LOOPS
z = 2
while z >= 0:
    g = 4
    while g > 0:
        print('Go Titans')
        g -= 1
    print()
    z -= 1
