user = input('Enter your age: ')
user = int(user)
if user >= 18:
    print("You are old enough to drive")
else:
    remains = 18 - user
    print(f"You need {remains} more years to learn to drive.")


your_age = input('Enter your age: ')
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
score = float(input("Enter Score: "))
if score >= 100:
    print("A")
elif score >= 70 and score <= 89:
    print("B")
elif score >= 60 and score <= 69:
    print("C")
elif score >= 50 and score <= 59:
    print("D")
else:
    print("F")


year = input("Enter Month: ")
if year in ["september", "october", "november"]:
    print("Autumn")
elif year in ["december", "january", "february"]:
    print("Winter")
elif year in ['march', 'april', 'may']:
    print("Spring")
elif year in ['june', 'july', 'august']:
    print("Summer")
else:
    print("Not a Season")


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

Skills = "skills" in person
val = person['skills']
if Skills == True:
    print(val[2])
    if 'Python' in val:
        print(f"Has Python skills")
        print()
if ('React' and 'Node' and 'MongoDB') in val:
    print('He is a fullstack developer') 
          
elif ('JavaScript' and 'React') in val:
    print('He is a front end developer')
    
elif ("Node" and 'Python' and 'MongoDB') in val:
    print('He is a backend developer')

else:
    print('unknown title')
print()
    
if (person['is_marred'] == True) and  (person['country'] == "Finland"):
    print("Asabeneh Yetayeh lives in Finland. He is married.")   
    



