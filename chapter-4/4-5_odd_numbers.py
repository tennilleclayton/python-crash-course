#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

#List 1 to 20
odd_numbers = list(range(1,20,3))

# Print each odd number
for number in odd_numbers:
    print(number, end=' ')