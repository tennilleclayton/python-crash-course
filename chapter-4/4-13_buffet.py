# 4-13: Buffet. A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure that Python rejects the change.
# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

# Tuple list of buffet foods
buffet_menu = ("Baked Chicken", "Salisbury Steak", 
               "Pork Tenderloin", "Beef Tips", "Fried Chicken Livers"
               )

# Print Monday's menu items
print("Monday Buffet:")
for menu_item in buffet_menu:
    print(f"- {menu_item}")

# Update buffet foods to Tuesday's menu
buffet_menu = ("Meatloaf", "Pot Roast", "Chicken and Dumplings", 
               "Corned Beef/BBQ Brisket", "Fried Chicken"
               )

# Print Tuesday's buffet menu items
print("\nTuesday Buffet:")
for menu_item in buffet_menu:
    print(f"- {menu_item}")