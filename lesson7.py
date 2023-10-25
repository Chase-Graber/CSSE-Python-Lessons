'''
Name: Chase Graber

Date: 9/8/23
Class: CSSE, Guillaume, Tri 1 2023
Lesson 7: Compound boolean expressions

Description:
    Students will be able to use AND and OR to evaluate compund boolean expressions
'''

# AND STATEMENTS: BOTH MUST BE TRUE
# OR STATEMENTS: ONE MUST BE TRUE

# AND STATEMENTS

# EX 1
x = 4
y = 5
if x>2 and y>4:
    print('Both are true.\n.\n.\n.\nOr so they want you to beleive.')

# EX 2
firstName = 'Hi i\'m Josh'
lastName = 'and welcome back to Let\'s Game it Out'

print('\n\n')
# The else is executed because only one of the parameters was true in the AND statement.
if firstName == 'Hi i\'m Josh' and lastName == 'and welcome back to Let\'s Fight it Out':
    print('What\'s up Josh')
else:
    print('Hi i\'m Josh, welcome back to Let\'s Game it Out. We\'re playing Satisfactory today.')

# OR STATEMENTS

# EX 1
a=4
b=5

print('\n\n')
# Only one of the statements needs to be true because it is an OR statement.
if a == 2 or b <= 10:
    print('You have passed the test. Welcome into the Brotherhood.')
else:
    print('You failed the test. You know too much. We need to [REDACTED] you.')

# EX 2
shirtColor = 'white'
pantsColor = 'blue'

print('\n\n')

if shirtColor == 'red' or pantsColor == 'gray':
    print('You look like Kevin Hart.')
else:
    print('You look like absolue [REDACTED] bro')

# VALIDATING USER INPUT WITH A COMPOUND EXPRESSION
playAgain = input('Do you want to play again: ')

while not(playAgain.lower() == 'yes' or playAgain.lower() == 'no'):
    playAgain = input('You absolute [REDACTED] bozo don\'t you dare [REDACTED] with me or i\'ll destroy all of your [REDACTED] [REDACTED]. YOU NEED TO SAY YES OR NO YOU [REDACTED] BUFFOON: ')
