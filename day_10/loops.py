
# Exercise Level 1

# Iterate 0 to 10 using for loop, do the same using while loop.
for num in range(11): # for loop
    print(num)

print()

x = 0
while x <= 10: # while loop 
    print(x)
    x+=1

# Iterate 10 to 0 using for loop, do the same using while loop.
for num in range(11): # for loop
    print(10-num)

print()

x = 10
while x >= 0 : # while loop 
    print(x)
    x -= 1


# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
X = ""
for t in range(7):
    X = X + "#"
    print(X)

# Use nested loops to create the following:
rows = 7
columns = 15

for x in range(rows):
    for y in range(columns):
        print("#", end=" ")
    print()

for n in range(11):
    result = n * n
    print(f"{n} x {n} = {result}")


# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lists = ['Python', 'Numpy','Pandas','Django', 'Flask']
for list in lists:
    print(list)

# Use for loop to iterate from 0 to 100 and print only even numbers
for n in range(101):
    if n%2 == 0:
        print(n)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for n in range(101):
    if n%2 != 0:
        print(n)

# Exercises: Level 2
sum = 0
for num in range(101): # for loop
    print(num)
    sum = sum + num

print(f"The sum of all numbers is {sum}.")

sum_e = 0
sum_o = 0
for num in range(101): # for loop
    print(num)
    if num%2 == 0:
        sum_e = sum_e + num
    else:
        sum_o = sum_o + num

print(f"The sum of all evens is {sum_e}. And the sum of all odds is {sum_o}.")


