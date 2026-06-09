# 5-4: Alien Colors #2. Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain. 
# 1. If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
# 2. If the alien's color isn't green, print a statement that the player just earned 10 points.
# 3. Write one version of this program that runs the if block and another that runs the else block.

alien_color = 'green'

# 1. Earn 5 point for shooting green alien
if alien_color == 'green':
    print('You just earned 5 points for shooting the alien.')

# 2. if alien color not green earn 10 points.
alien_color = 'red'
if alien_color != 'green':
    print("\nYou've earned 10 points.")

# 3. If else block
if alien_color == 'red':
    points = 10
elif alien_color == 'green':
    points = 5

print(f'\nYou just earned {points} points for shooting the alien.')