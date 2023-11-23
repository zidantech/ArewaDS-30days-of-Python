import math

def cal_sqrt(num):
    sqrt = math.sqrt(num)
    return sqrt

num = float(input("Enter a number: "))

try:
    result = cal_sqrt(num)
    print(f"The Squareroot of the {num} is {result}")
except:
    print("Please enter a positive numeric number")
    quit()