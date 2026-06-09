# 5-2. More Conditional Tests: You don't have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:

fathers_age = 40
mothers_age = 42
grandparents = ['john','mary','william','gloria']
parents = ['jj','KAREN','paul','pam']
child_1 = 15
child_2 = 10
child_3 = 9

# Tests for equality and inequality with strings
print('Equality and inequality with strings test:')
print(f"Inequality string:\n\t - grandparents[0] == 'william' is {grandparents[0] == 'william'}.\n")
print("Equality  string:")
print(f"\t- parents[2] == 'paul' is {parents[2] == 'paul'}.")

# Tests using the lower () method
for parent in parents:
    if parent == 'KAREN':
        print(parent.lower())
    else:
        print(parent.title())

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to

# Numerical equality and inequality test
if fathers_age == mothers_age:
    print('Your parents are the same age.')
else:
    print('Your parents are different ages.')

# greater than and less than
if mothers_age > 50:
    print("Your mom's age is over 50.")
else:
    print(f"Your mom's age is {mothers_age}.")

# greater than or equal to
if child_1 >= child_2:
    print('You are the oldest.')

if child_2 <= child_3:
    print("you're' youger")
else:
    print("you're younger.")

# Tests using the 'and' keyword and the 'or' keyword
if ('jj' in parents) and ('KAREN' in parents):
    print("JJ is my father and Karen is my mother.")

# Test whether an item is in a list

# Test whether an item is 'not in' a list
stepdad = 'jackson'

if stepdad not in parents:
    print(f"{stepdad.title()} is not your parent.")