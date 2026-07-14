# 7-10: Dream Vacation. Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

responses = {}

# Set active status
polling_active = True

while polling_active:
    name = input(f"\nWhat's your name? ")
    location = input(f"If you could visit one place in the world, where would you go? ")

    responses[name] = location

    # Find out if anyone else is going to take the poll
    repeat_poll = input(f"Would you like to let anyone person respond? (yes / no) ")

    if repeat_poll == 'no':
        polling_active = False

# Polling Results
print("\n --- Polling Results ---")
for name, location in responses.items():
    print(f"- {name.title()} would like to go to {location.title()}")