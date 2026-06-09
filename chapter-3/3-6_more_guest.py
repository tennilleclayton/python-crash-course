#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program, informing people that you found a bigger dinner table. 
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list. Print a new set of invitation messages, one for each person in your list.

#list of guest
guest_list=['donald trump','marco polo','jane doe']

#invitation message
message=", you are invited to dinner. You're welcome!"

#Each person invite message
print(f'{guest_list[0].title()}{message}')
print(f'{guest_list[1].title()}{message}')
print(f'{guest_list[2].title()}{message}')

#Inform guest we have a bigger table
print(f'\nGreat new! We have a bigger dinner table. YAY!\n')

#insert new guest at the beginning
guest_list.insert(0,'clark howard')

#insert new guest in the middle
guest_list.insert(2,'carol williams')

#append guest to end of list
guest_list.append('chicken little')

name=guest_list[0].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

name=guest_list[1].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

name=guest_list[2].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

name=guest_list[3].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

name=guest_list[4].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)

name=guest_list[5].title()
msg=f"{name}, you're invited to dinner tonight."
print(msg)