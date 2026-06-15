# make the output 77
toys = {"robot": "$40.0", "car": "$25", "ironman": "$12"}

# get the values all put together
prices = int(eval(list(toys.values())[0][1:]) + eval(list(toys.values())[1][1:]) + eval(list(toys.values())[2][1:]))
print(prices)

# step by step breaking apart

# 1. get the values from the dictionary
toy_values = toys.values()

# 2 convert values to a list
toy_values = list(toy_values)

# 3. remove $
toy_values = list(toys.values())[0][1:]

# 4. Eval()
toy_values = eval(list(toys.values())[0][1:])

# 5. convert to int
toy_values = int(eval(list(toys.values())[0][1:]))

print(type(toy_values))
print(toy_values)