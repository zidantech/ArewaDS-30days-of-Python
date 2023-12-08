# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
user = input('Enter your age: ')
try:
    user = int(user)
    if user >= 18:
        print("You are old enough to drive")
    else:
        remains = 18 - user
        print(f"You need {remains} more years to learn to drive.")
    
except:
    print("Please enter a valid numeric age")
    exit()
    
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
your_age = input('Enter your age: ')
try:
    your_age = int(your_age)
    my_age = 23
    if your_age > my_age:
        remains = your_age - my_age
        if remains == 1 :
            print("You are a year older than me ")
        else:
            print(f"You are {remains} years older than me ")
    elif your_age < my_age:
        remains = my_age - your_age
        if remains == 1 :
            print("I am a year older than you ")
        else:
            print(f"I am {remains} years older than you ")
    
    else:
        print("We have the same age")
    
except:
    print("Please enter a valid numeric age")
    exit()
    
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = float(input("Enter Number one: "))
b = float(input("Enter Number two: "))
try:
    if a > b :
        print(f"{a} is greater than {b}")

    else:
        print(f"{b} is greater than {a}")
except:
    print("Enter a valid numeric value")
# Exercises: Level 2

# Write a code which gives grade to students according to theirs scores:
score = float(input("Enter Score: "))
if score >= 100:
    print("Score: A")
elif score >= 70 and score <= 89:
    print("Score: B")
elif score >= 60 and score <= 69:
    print("Score: C")
elif score >= 50 and score <= 59:
    print("Score: D")
else:
    print("Score: F")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

year = input("Enter Month: ")

year = year.lower()
Autumn = ["september", "october", "november"]
Winter = ["december", "january", "february"]
Spring = ['march', 'april', 'may']
Summer = ['june', 'july', 'august']

if year in Autumn:
    print("Autumn")
elif year in Winter:
    print("Winter")
elif year in Spring:
    print("Spring")
elif year in Summer:
    print("Summer")
else:
    print("Not a Season")

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new = input("Enter Fruit: ")
new = new.lower()
if new not in fruits:
    fruits.append(new)
    print('fruit added')
    print(fruits)
else:
    print('That fruit already exist in the list')
    print(fruits)
print()
# Exercises: Level 3

# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
Skills = "skills" in person
val = person['skills']
if Skills == True:
    print(val[2])
    # Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    if 'Python' in val:
        print(f"Has Python skills")
        print()

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if ('React' and 'Node' and 'MongoDB') in val:
    print('He is a fullstack developer') 
          
elif ('JavaScript' and 'React') in val:
    print('He is a front end developer')
    
elif ("Node" and 'Python' and 'MongoDB') in val:
    print('He is a backend developer')

else:
    print('unknown title')
print()
    
# If the person is married and if he lives in Finland, print the information in the following format:
if (person['is_marred'] == True) and  (person['country'] == "Finland"):
    print("Asabeneh Yetayeh lives in Finland. He is married.")   
    



