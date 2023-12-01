age = 23
height = 20.6
complex = 4+5j

# calculate an area of this triangle
base = float(input("Enter Base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# Calculate the perimeter of the triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

# Area and perimete of a rectangle
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"the area of the rectangle is {area}, and the perimeter is {perimeter} ")

# Area and perimeter of a rectangle
radius = float(input("Enter Radius: "))
pi = 3.14
area = pi * radius**2
circumference = 2 *pi * radius
print(f"the area of the circle is {area} a3nd the circumference is {circumference}")

#slope of x-intercept and y-intercept of y = 2x -2
y = lambda x: 2 * x - 2
slope1 = (y(1) - y(0)) / (1 - 0)
print("The slope is", slope1)

# slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope2 = (y2-y1)/(x2-x1)
print(f"the slope is {slope2}")
dst = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The Euclidian distance between (2, 2) and (6, 10) is {dst}")

# Comparing the slopes in First and the Second
if slope1 == slope2:
    print("the slopes are the same")
elif slope1 > slope2:
    print("the first slope is greater")
else:
    print("the second slope is greater")

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Define the function y = x^2 + 6x + 9
def y(x):
    return x**2 + 6*x + 9

# Try some x values and print the corresponding y values
print("y(0) =", y(0))
print("y(-1) =", y(-1))
print("y(-2) =", y(-2))
print("y(-3) =", y(-3))
print("y(-4) =", y(-4))
print("y(-5) =", y(-5))

print("You can see that y is 0 when x is -3. This means that -3 is the root of the equation y = x^2 + 6x + 9")

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
x_1,x_2 = len("python"), len("dragon")
print(x_1 != x_2 )

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "dragon")

# Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")

# There is no 'on' in both dragon and python
print("on" not in "python" and "dragon")

# Find the length of the text python and convert the value to float and convert it to string
n = len("python")
n = float(n)
n = str(n)
print(f"{n} and {type(n)}")

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
even = float(input("Enter no:"))
if even % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")
    
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') is equal to 10
print(int(9.8) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
weekly = hours * rate
print(f"Your weekly earning is {weekly}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
yrs = float(input("Enter number of years you have lived: "))
sec = yrs * 365 * 24 * 60 * 60
print(f"You have lived for {sec}seconds.")

print('''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125'''  
)