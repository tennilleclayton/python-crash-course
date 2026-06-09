#3-10: Think of everything you can store in a list. For example, you can make a list of mountains, river, countries, cities, languages, or anything else you'd like. Make a program that creates a list containing these items and then use each function introducted in this chapter at least once.

# List of vegetables
vegetables=['spinach','kale','potatoes','carrots','broccoli','cauliflower','zucchini','pumpkin']

#Function in Chapter 3: sorted(), and len()

# print() function
print(vegetables)

# sorted() function
msg=sorted(vegetables)
print(msg)

msg=sorted(vegetables, reverse=True)
print(msg)

# len() function
num_vegetables=len(vegetables)
print(num_vegetables)