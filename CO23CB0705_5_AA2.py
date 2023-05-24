student = {
    'Name': 'Conji',
    'Grade': 7,
    'Address': '123, Main Street, Avora',
    'Phone Number': '123-456-7890',
    'Favourite Subject': 'Potions'
}
# Display the student details
print("\nStudent Details:")
for key, value in student.items():
    print(f"{key}: {value}")
    
# Take user input for a new key-value pair
new_key = input("\nEnter a new key: ")
new_value = input("Enter the value for the new key: ")

# Add the new key-value pair using dictionary methods
student[new_key] = new_value

# Display the updated student details
print("\nUpdated Student Details:")
for key, value in student.items():
    print(f"{key}: {value}")
