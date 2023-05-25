# Example dictionary
student_data = {
    'name': 'Conji', 
    'age': 13, 
    'city': 'New Avora City'
}

# Update the value of an existing key
student_data['age'] = 12

# Update multiple keys and values using the update() method
updates = {'name': 'Eva', 'city': 'Old Avora City'}
student_data.update(updates)

# Show the modified dictionary
print("Modified dictionary:", student_data)
