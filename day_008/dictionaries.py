# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'jackie', 'color':'black', 'breed':'bulldog', 'legs':'brown', 'age': 2}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Zidan', 'last_name':'Musa', 'gender':'Male', 'age':23, 'marital_status':'single', 'skills':['JavaScript', 'Node', 'MongoDB', 'Python'], 'country':'Nigeria', 'city':'Abuja', 'address':'Wuse'}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
skills = student['skills']
print(skills)

# Modify the skills values by adding one or two skills
student['skills'].append('React')
print(student)

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.pop('skills')
print(student)

# Delete one of the dictionaries
del student