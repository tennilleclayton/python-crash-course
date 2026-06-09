#3.5. Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite. 
#Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can't make it. 
#Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting. 
#Print a second set of invitation messages, one for each person who is still in your list.

#list of guest
guest_list=['donald trump','marco polo','jane doe']

#invitation message
message=", you are invited to dinner. You're welcome!"

#Each person invite message
print(f'{guest_list[0].title()}{message}')
print(f'{guest_list[1].title()}{message}')
print(f'{guest_list[2].title()}{message}')

#The guest that can't make it
cant_make_dinner=guest_list[2]

print(f'\nSorry everyone, plans have changed. Unfortunately, {cant_make_dinner.title()} is no longer able to make the dinner.\n')

#replacing a guest
guest_list[2]='will trent'

#Each person invite message
print(f'{guest_list[0].title()}{message}')
print(f'{guest_list[1].title()}{message}')
print(f'{guest_list[2].title()}{message}')