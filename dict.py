# Basic Questions:

# Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.
student = {
    "name" : "Ali",
    "age" : 21,
    "grade" : "A"
}

# print(student)

# Access the value of the key grade in the student dictionary.
acces_value = student["grade"]
# print(acces_value)

# Add a new key city to the student dictionary and set its value to "New York".
student["city"] = "New York"
# print(student)

# Update the value of the age key in the student dictionary to 20.
student["age"] = 20
# print(student)

# Remove the key city from the student dictionary.
del student["city"]
# print(student)


#                          _____________________________________________________________________

# Iterating through Dictionaries:

# Iterate through the dictionary student and print all keys.
for each_key in student.keys():
    print(each_key)
    
# Iterate through the dictionary student and print all values.
for each_value in student.values():
    print(each_value)
    
# Iterate through the dictionary student and print all key-value pairs in the format key: value.
for key, value in student.items():
    print(f"{key}: {value}")
    
# Check if the key grade exists in the student dictionary and print True or False.
for key in student:
    if key == "grade":
        print(True)
    
# Count the total number of keys in the student dictionary.
print(len(student))

#                           ________________________________________________________________________


# Merge the following two dictionaries and print the result:
dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4}  

dict1.update(dict2)
print(dict1)

# Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
dic = dict([('name', 'Alice'), ('age', 25), ('city', 'Paris')])
print(dic)

# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
sort_dic = sorted({'z': 1, 'a': 2, 'c': 3})
print(sort_dic)

# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.
original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {value: key for key, value in original_dict.items()}

print(reversed_dict)

# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).
def check_dic(dict1,dict2):
    if dict1 == dict2:
        return True
    else:
        return False
print(check_dic({"a":1,"b":2},{"a":1,"b":2}))

# Nested Dictionaries:

# Create a nested dictionary to represent the following data
# Person:  
#   Name: John  
#   Age: 30  
#   Address:  
#     Street: 123 Elm St  
#     City: Boston  

citizen = {"person":{"name":"John","age":30,"address":{"Street":"123 elm st","city":"Boston"}}}
print(citizen)

# Access the value of the City key in the nested dictionary from the previous question.
acce_val = citizen["person"]["address"]["city"]
print(acce_val)

# Add a new key Phone to the nested dictionary with the value "123-456-7890".
citizen["phone"] = "123-456-7890" 
print(citizen)

# Delete the Address key from the nested dictionary.
del citizen["person"]["address"]
print(citizen)

# Iterate through all the keys in the outermost level of the nested dictionary and print them.
for key in citizen.keys():
    print(key)
    
#                            _____________________________________________
