'''
Name: Chase Graber

Date: 9/21/23
Class: CSSE, Guillaume, Tri 1 2023
Modular Arithmetic

Description:
    Students will be able to use modular arithmetic to sind remainders of quotients
'''

a = 4 % 3
print('4 % 3 = ' + str(a))

b = 21 % 16
print('21 % 16 = ' + str(b))

c = 4 % 16
print('4 % 16 = ' + str(c))

d = 32 % 32
print('32 % 32 = ' + str(d))

# Check if a number is odd or even
userNum = int(input('Choose a number: '))
if userNum % 2 == 1:
    print('That number is odd.')
else:
    print('That number is even.')
