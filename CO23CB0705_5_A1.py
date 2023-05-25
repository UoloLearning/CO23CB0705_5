emp_data = {
    'first_name': 'Paul',
    'last_name': 'Parker',
    'age': 30, 
    'city': 'New York',
    'occupation':'teacher'
}

# extract all the keys and print them
extracted_keys = list(emp_data.keys())
print("Extracted keys:", extracted_keys)

# extract all the values and print them
extracted_values = list(emp_data.values())
print("Extracted values:", extracted_values)

# remove a specific key
removed_element = emp_data.pop('age')
print("\nRemoved element:", removed_element)
print("Updated dictionary:", emp_data)

# remove last key
emp_data.popitem()
print("\nDictionary after removing last key:", emp_data)

# delete all items
emp_data.clear()
print("\nFinal Dictionary:", emp_data)

