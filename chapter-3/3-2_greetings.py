#3.2. Greeetings: Start with the list you used in Exercise 3.1, but instead of print each person's name, print a message to them. The text should be the same, but each message should be personalized with the person's name.

#Name of friends
names=['John','David','Sally','Reba','Karen']

#message
message="You're the best,"

#Print personalized message
print(f"{message} {names[0]}!") #formated this list
print(message,names[1])
print(message,names[2])
print(message,names[3])
print(message,names[4])