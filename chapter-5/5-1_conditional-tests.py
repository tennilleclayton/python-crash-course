# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.
# Look closely at your results, and make sure you understand why each line evaluates to True or False.
# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

car = 'subaru'

# Variable
print(car)

# print true statements
print("\nThese are 5 True statements:")
print("1. car == 'subaru' is,", car == 'subaru')
print("2.", car.title() == 'Subaru')
print("3.", car.capitalize() == 'Subaru')
print("4.", (car == 'SUBARU') or (car == 'subaru'))
print("5. (car != 'bike') and (car == 'subaru') is,", (car != 'bike') and (car == 'subaru'))

# print false statement
print("\nThese are 5 False statements:")
print("1.", car.capitalize() == 'subaru')
print("2.", car == 'toyota')
print("3.", car == ' truck')
print("4.", car.title() == 'subaru')
print("5.", car.upper() == 'subaru')

# print (car == ' subaru')
# print ("\nIs car == 'audi'? I predict False.")
# print (car == 'audi')


