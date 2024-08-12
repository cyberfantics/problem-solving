'''
For this problem we can approch two solutions
1) We use predefined numbers
2) Take it through user input
@mansoor
'''


# Solution 01
## First we initlize two numbers
num1 = 30
num2 = 50

## Take their sum in third 
num3 = num1 + num2

## Print 
print(f'{num1} + {num2} = {num3}')


'''
Solution 02
'''

## We take two values from user
num1 = input("Enter first number ")
num2 = input("Enter 2nd value ")
# We use input for taking input from user

# By default input take value in string, so explicitly we need to change data type to integer
num1 = int(num1)
num2 = int(num2)

# Take their sum in third 
num3 = num1 + num2

## Print 
print(f'{num1} + {num2} = {num3}')

