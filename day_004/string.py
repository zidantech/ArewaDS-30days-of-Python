# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
print( 'Thirty '+ 'Days ' + 'Of ' + 'Python' )

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
print( 'Coding', 'For' , 'All')

# Declare a variable named company and assign it to an initial value "Coding For All"
company =  "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
g = "Coding For All"
print(g.capitalize())
print(g.title())
print(g.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(g[0:6])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(g.find("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.
print(g.replace("Coding", "Python"))

# Change Python for Everyone to Python for All using the replace method or other methods.
p = "Python for Everyone"
print(p.replace("Everyone", "All"))

# Split the string 'Coding For All' using space as the separator (split()) 
ch = 'Coding For All'
print(ch.split()) 

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
ch = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(ch.split(','))

# What is the character at index 0 in the string Coding For All.
r = "Coding For All" 
print(r[0]) #C

# What is the last index of the string Coding For All.
print(r[-1]) #l

# What character is at index 10 in "Coding For All" string.
print(r[10]) #" "

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
acc = 'Python For Everyone'
print(".".join(word[0] for word in acc.split()))

# Create an acronym or an abbreviation for the name 'Coding For All'.
acc = 'Coding For All'
print(".".join(word[0] for word in acc.split()))

# Use index to determine the position of the first occurrence of C in Coding For All.
text = "Coding For All"
print(text.index("C"))

# Use index to determine the position of the first occurrence of F in Coding For All.
text = "Coding For All"
print(text.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
text = "Coding For All People"
position = text.rfind("l")
print(position)

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
position = sentence.index("because")
print(position)

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
position = sentence.rindex("because")
print(position)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
phrase = sentence[31:54]
print(phrase)

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
position = sentence.index("because")
print(position)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase = sentence[31:54]
print(phrase)

# Does 'Coding For All' start with a substring Coding?
text = 'Coding For All' 
print(text.startswith('Coding')) #true

# Does 'Coding For All' end with a substring coding?
text = 'Coding For All' 
print(text.startswith('coding')) #False

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
challenge = '   Coding For All      '
print(challenge.strip(' '))

# Which one of the following variables return True when we use the method isidentifier():
ch = '30DaysOfPython'
print(ch.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(ch.isidentifier()) # True

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)
print(result)

#Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
print("Name\t        Age  \tCountry \tCity")
print("Asabeneh\t250\tFinland \tHelsinki")

# Use the string formatting method to display the following
print('{} = {}'.format('radius', 10))
radius = 10
print('{} = {} * {} ** {}'.format('area', 3.14,  'radius', 2))
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Make the following using string formatting methods:
a=8
b=6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))