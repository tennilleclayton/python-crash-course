# 4-12: More Loops. All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

# Favorite food lists
my_foods = ["pizza","falafel","carrot cake"]
friend_foods = my_foods[:]

# Add new to my favorite foods
my_foods.append("taco salad")

# Add to my friends favorite foods
friend_foods.append("Apples")

print("My Favorite foods are:")
for my_food in my_foods:
    print(f"- {my_food.title()}")

print("\nMy friends favorite foods:")
for friend_food in friend_foods:
    print(f"- {friend_food.title()}")
