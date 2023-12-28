# Exercise: Level 1
# Create an empty tuple
empty = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Yasir', 'Tahir', 'Ridwan') 
sisters = ('Yasmin', 'Saudat')


# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Musa', 'Hadiza')
print(family_members)


# Exercise: Level 2
# Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print(siblings)
print( father, mother)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('mango', 'banana', 'orange', 'pawpaw', 'watermelon')
vegetables = ('carrot', 'cabbage', 'onions')
animal = ('dogs', 'cats', 'lizard', 'eagles')

food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(len(food_stuff_lt))
print(food_stuff_lt[5:7])

#Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3])

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)