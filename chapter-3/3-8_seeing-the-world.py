#3-8. Seeing the World: Think of at least five places in the world you'd like to visit. 
# 1. Store the locations in a list. Make sure the list is not in alphabetical order.
# 2. Print your list in its original order. Don't worry about printing the list neatly, just print it as a raw Python list.
# 3. Use sorted() to print your list in alphabetical order without modifying the actual list.
# 4. Show that your list is still in its original order by printing it.
# 5. Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# 6. Show that your list is still in its original order by printing it again.
# 7. Use reverse() to change the order of your list. Print the list to show that its order has changed.
# 8. Use reverse() to change the order of your list again. Print the list to show it's back to its original order. 
# 9. Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.
# 10. Use sort() to change your list so it's stored in reverse alphabetical order. Print the list to show that its order has changed.

#1. Places to visit
places=['london','new york city','washington dc','japan','china']

#2. Print original list
print(f'Original')
print(places)

#3. Sorted list alphabetical order
print(f'\nAlphabetical')
print(sorted(places))

#4. Verify original order
print(f'\nOriginal')
print(places)

#5.Sorted list in reversed alphabetical order
print(f'\nSorted Reverse order')
#print(sorted(places,reverse=True))
msg=sorted(places, reverse=True)
print(msg)

#6. Verify list order
print(f'\nOriginal')
print(places)

# 7. Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print(f'\nReverse order')
print(places)

# 8. Use reverse() to change the order of your list again. Print the list to show it's back to its original order. 
places.sort(reverse=False)
print(f'\nOriginal order')
print(places)

# 9. Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()
print(f'\nAlphabetical')
print(places)

# 10. Use sort() to change your list so it's stored in reverse alphabetical order. Print the list to show that its order has changed.
places.sort(reverse=True)
print(f'\nReverse alphabetical')
print(places)