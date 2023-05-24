# Example dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Extract and delete a specific key
key = 'age'
value = my_dict[key]
del my_dict[key]
print("Extracted value:", value)
print("Updated dictionary:", my_dict)

# Extract and delete all keys
extracted_keys = list(my_dict.keys())
for key in extracted_keys:
    del my_dict[key]
print("Extracted keys:", extracted_keys)
print("Updated dictionary:", my_dict)

# Restore the original dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Extract and delete all values
extracted_values = list(my_dict.values())
my_dict.clear()
print("Extracted values:", extracted_values)
print("Updated dictionary:", my_dict)

# Restore the original dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Extract and delete all items
extracted_items = list(my_dict.items())
my_dict.clear()
print("Extracted items:", extracted_items)
print("Updated dictionary:", my_dict)
