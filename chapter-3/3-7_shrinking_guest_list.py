#3-7. Shrinking guests List: You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests. 
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they're still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

#list of guests
guests=['donald trump','marco polo','jane doe']

#invitation message
message=", you are invited to dinner. You're welcome!"

#Each person invite message
print(f'{guests[0].title()}{message}')
print(f'{guests[1].title()}{message}')
print(f'{guests[2].title()}{message}')

#Inform guestss we have a bigger table
print(f'\nGreat new! We have a bigger dinner table. YAY!\n')

#insert new guests at the beginning
guests.insert(0,'clark howard')

#insert new guests in the middle
guests.insert(2,'carol williams')

#append guests to end of list
guests.append('chicken little')

name=guests[0].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

name=guests[1].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

name=guests[2].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

name=guests[3].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

name=guests[4].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

name=guests[5].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

#Shrinking guests list starts here
# Print message about guests list update
msg=f'\nI can only invite two people to dinner.\n'
print(msg)

#inform guests who is out
name=guests.pop()
msg=f"{name.title()}, sorry I can't invite you to dinner."
print(msg)

name=guests.pop()
msg=f"{name.title()}, sorry I can't invite you to dinner."
print(msg)

name=guests.pop()
msg=f"{name.title()}, sorry I can't invite you to dinner."
print(msg)

name=guests.pop()
msg=f"{name.title()}, sorry I can't invite you to dinner."
print(msg)

#Still invited guests
name=guests[0].title()
msg=f"{name}, you're still invited."
print(msg)

name=guests[1].title()
msg=f"{name}, you're still invited."
print(msg)

#delete the guests list
del guests[0]
del guests[0]

#Prove the list is empty
print(guests)