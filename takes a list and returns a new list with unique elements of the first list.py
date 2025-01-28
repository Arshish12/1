# Original list
original_list = [1, 2, 3, 4, 4, 5, 5, 6]

# Create a new list with unique elements
unique_list = list(set(original_list))

# Print the result
print("Original List:", original_list)
print("Unique List:", unique_list)
# Original list
original_list = [1, 2, 3, 4, 4, 5, 5, 6]

# Create a new list with unique elements while maintaining order
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

# Print the result
print("Original List:", original_list)
print("Unique List:", unique_list)
