my_dict = {
    'first_name': 'Paul',
    'last_name': 'Parker',
    'age': 30, 
    'city': 'New York',
    'occupation':'teacher'
}

# extract all the keys and print them
extracted_keys = list(my_dict.keys())
print("Extracted keys:", extracted_keys)

# extract all the values and print them
extracted_values = list(my_dict.values())
print("Extracted values:", extracted_values)

# remove a specific key
removed_element = my_dict.pop('age')
print("\nRemoved element:", removed_element)
print("Updated dictionary:", my_dict)

# remove last key
my_dict.popitem()
print("\nDictionary after removing last key:", my_dict)

# delete all items
my_dict.clear()
print("\nFinal Dictionary:", my_dict)

