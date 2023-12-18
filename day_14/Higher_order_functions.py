# Day 14: 30 days of Python programming

# Exercises: Level 1

# Explain the difference between map, filter, and reduce.
    # The difference between map, filter, and reduce in python is that they are three functions that allow you to apply a function to an iterable or a sequence of elements in a concise and elegant way.
    # map(function, iterable) applies the function to each element in the iterable and returns a new iterable with the results. For example, map(str.upper, [“hello”, “world”]) returns [“HELLO”, “WORLD”].
    # filter(function, iterable) keeps only the elements in the iterable that satisfy the function as a condition and returns a new iterable with the filtered elements. For example, filter(lambda x: x > 0, [-1, 2, -3, 4]) returns [2, 4].
    # reduce(function, iterable) applies the function cumulatively to the elements in the iterable, from left to right, and reduces the iterable to a single value. For example, reduce(lambda x, y: x + y, [1, 2, 3, 4]) returns 10.

# Explain the difference between higher order function, closure and decorator
    # A higher order function is a function that takes another function as an argument or returns a function as a result. For example, the built-in function map is a higher order function that takes a function and an iterable and returns a new iterable with the function applied to each element.
    # A closure is a function that can access and modify variables from the outer scope, even after the outer scope has ended. A closure is created when a nested function is returned by the outer function    
    # A decorator is a special kind of higher order function that wraps another function and modifies its behavior or adds some functionality. A decorator can be defined using the @ syntax before the function definition

# Define a call function before map, filter or reduce, see examples.
# Example with map
def square(y):
    return y ** 3

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use the function with map
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# Example with filter
def is_even(x):
    return x % 2 == 0

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use the function with filter
even_numbers = list(filter(is_even, numbers))
print(even_numbers)


# Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# Use for to print each name in the names list.
for name in names:
    print(name)

# Use for to print each number in the numbers list.
for number in numbers:
    print(number)

# Exercise level 2
# countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# Use map to create a new list by changing each country to uppercase in the countries list
upper_case_countries = list(map(lambda x:x.upper(),countries))
print(f'countries in upper case: {upper_case_countries} ')

# Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = list(map(lambda x:x**2,numbers))
print(f'The square of the numbers: {squared_numbers} ')

# Use map to change each name to uppercase in the names list
upper_case_names = list(map(lambda x:x.upper(),names))
print(f'Uppercase of the names: {upper_case_names} ')

# Use filter to filter out countries containing 'land'.
contains_land = list(filter(lambda x:'land' in x,countries))
print(f' The countries with land in their name: {contains_land}')

# Use filter to filter out countries having exactly six characters.
six_chars = list(filter(lambda x:len(x)==6,countries))
print(f'The countries with six characters: {six_chars} ')

# Use filter to filter out countries containing six letters and more in the country list.
six_or_more_chars = list(filter(lambda x:len(x) >= 6,countries))
print(f'Countries with six or more characters in their names: {six_or_more_chars} ')

# Use filter to filter out countries starting with an 'E'
starting_with_e = list(filter(lambda x:x.startswith('E'),countries))
print(f' Countries starting with E in the list are: {starting_with_e}')

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

numbers = [3, 5, 8, 2, 14]
squared_even_numbers_sum = reduce(lambda x, y: x + y, 
                                   list(filter(lambda x: x % 2 == 0, 
                                                map(lambda x: x**2, numbers))))
print(squared_even_numbers_sum)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(input_list):
    return [item for item in input_list if isinstance(item, str)]

# Test the function
input_list = [1, 'apple', 'banana', 3, 'orange', 'kiwi']
result = get_string_lists(input_list)
print(result)

# Use reduce to sum all the numbers in the numbers list.
from functools import reduce
def add(x,y):
    return x + y
sum_all = reduce(add,numbers)
print(f'The sum of {numbers} is {sum_all}')

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
concat = reduce(lambda x,y:x + ',' + ' '+ y,countries[:-1])
print(f'{concat} and {countries[-1]} are North European countries ')

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(pattern):
    list_countries = []
    for country in countries:
        if pattern.lower() in country:
            list_countries.append(country)
    return list_countries

print(f'Countries with "pattern": ',categorize_countries('stan'))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def countries_dict():
    dict_countries = {}
    for country in countries:
        dict_countries[country[0]] = dict_countries.get(country[0],0) + 1
    return dict_countries
print(f' Dictionary of number of countries per letter: {countries_dict()}')

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
    return countries[:10]

print(f' First ten countries in the countries list: {get_first_ten_countries()}')

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return countries[-10:]

print(f'The last ten countries in the countries list: {get_last_ten_countries()}')

# Exercises: Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# Sort countries by name, by capital, by population
# Sort out the ten most spoken languages by location.
# Sort out the ten most populated countries.