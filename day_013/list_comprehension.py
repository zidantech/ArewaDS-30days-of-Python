# Filter only negative and zero in the list using list comprehension
numbers = [-4,-3,-2,-1,0,2, 4, 6]
[number for number in numbers if number <=0]

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1,2,3]],[[4,5,6]],[[7,8,9]]]
# print(list_of_lists)

x = [number for row in list_of_lists for list in row for number in list]

print(x)

# Using list comprehension create the following list of tuples:
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

t_list = [(i**1,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)] 
print(t_list)

# Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# tupple -> row -> list
[[tpl[0].upper(),tpl[0][:3].upper(), tpl[1].upper()] for row in countries for tpl in row]

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
[{'country':tpl[0],'city':tpl[1]} for row in countries for tpl in row]

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
[(name[0] + " " + name[1]) for row in names for name in row]

# Write a lambda function which can solve a slope or y-intercept of linear functions.
# y = m * x + c
y = lambda m,c,x:c  # when x is zero, value of y
y(2,4,2)