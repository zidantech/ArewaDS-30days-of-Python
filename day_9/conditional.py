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
    