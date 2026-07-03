# Exercise 1: Basic Dictionary Operations
# Problem Statement: Write a Python program to add a new key-value pair to a dictionary, modify an existing value, and access a specific key.
# Purpose: Learn and practice the most fundamental dictionary operations such as insertion, update, and lookup, which form the backbone of working with key-value data in Python.
# Given Input: student = {"name": "Alice", "age": 20, "grade": "B"}
# Expected Output: {"name": "Alice", "age": 21, "grade": "B", "city": "New York"} and Name: Alice

# Given dictionary Input
student = {
    "name": "Alice", 
    "age": 20, 
    "grade": "B"
    }

student["age"] = 21
student["city"] = "New York"

print("Exercise 1: Basic Dictionary Operations")
print(f"{student} and Name: {student["name"]}")

# Exercise 2: Dictionary Operations
# Problem Statement: Write a Python program to remove a specific key from a dictionary, retrieve all key-value pairs, and check whether a given key exists.
# Purpose: To builds familiarity with essential dictionary methods pop(), items(), and the in operator, which are routinely used when processing and validating structured data.
# Given Input: car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
# Expected Output:
# {'brand': 'Toyota', 'model': 'Camry', 'year': 2022}
# dict_items([('brand', 'Toyota'), ('model', 'Camry'), ('year', 2022)])
# 'brand' exists: True
# 'color' exists: False

car = {
    "brand": "Toyota", 
    "model": "Camry", 
    "year": 2022, 
    "color": "blue"
    }

car.pop("color")
print(f"\nExercise 2: Dictionary Operations")
print(car)
print(car.items())
print(f"'brand' exists:", 'brand' in car)
print(f"'color' exists:", 'color' in car)

# Exercise 3: Dictionary from Two Lists
# Problem Statement: Write a Python program to create a dictionary by mapping two equal-length lists, one containing keys and the other containing values.
# Purpose: Learn how to construct a dictionary dynamically from existing data, a common pattern when importing tabular data, pairing labels with values, or building lookup tables.
# Given Input: keys = ["name", "age", "city"] and values = ["Bob", 25, "London"]
# Expected Output: {'name': 'Bob', 'age': 25, 'city': 'London'}

keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]
users = zip(keys, values)

print(f"\nExercise 3: Dictionary from Two Lists")
print(dict(users))