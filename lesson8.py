'''
Name: Chase Graber

Date: 9/8/23
Class: CSSE, Guillaume, Tri 1 2023
Lesson 8: Lists

Description:
    Students will be able to use lsits to store and access data
'''
import random

# use [] to create a list
colorsList = ['red', 'green', 'blue', 'yellow']
numbersList = [62, 42, 12, 3, 6]
namesList = ['harry', 'ronald', 'hermione']
statesList = [] # Empty list

# ACESSING DATA
print(namesList[1])

# DETERMINE THE LENGTH OF THE LIST
print(len(colorsList))

# CHANGE THE DATA IN THE LIST
namesList[1] = 'ginny'
print(namesList)

# RANDOMLY CHOOSE FROM A LIST
ranColor = random.choice(colorsList)
print(ranColor)

# APPEND TO LIST
print(numbersList)
numbersList.append(17)
print(numbersList)

print(namesList)
namesList.append('NICHOLASSSSS')
print(namesList)

# REMOVE FROM LIST
namesList.remove('NICHOLASSSSS')
namesList.remove('hermione')
print(namesList)

# INSERT INTO A LIST
namesList.insert(0, 'Voldemort')
print(namesList)
numbersList.insert(1, 900)
print(numbersList)

# SORT
numbersList.sort()
print(numbersList)

# ITERATING THROGH A LIST
for index in range(len(colorsList)):
    print(colorsList[index])

for i in range(len(numbersList)):
    numbersList[i] = numbersList[i] + 3
    print(numbersList[i])
