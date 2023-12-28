# Declare an empty list
list =  []

# Declare a list with more than 5 items
num = [' first', 'second', 'third','forth', 'fifth', 'sixth', 'seventh']

#Find the length of your list
print(len(num))

# Get the first item, the middle item and the last item of the list
first_num, a, b, middle_num, c, d, last_num, = num
print(first_num)     # banana
print(middle_num)    # berries
print(last_num)      # pawpaw

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Zidan", 23, 45, 'single', 'kaduna']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(mixed_data_types)
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
a,b,c,d,e,f,g = it_companies
print(a)
print(d)
print(g)

# Print the list after modifying one of the companies
it_companies[0] = "MICROTIK"
print(it_companies)

# Add an IT company to it_companies
it_companies.append('CISCO')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert( 3, 'NITDA')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = it_companies[4].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
result = '#; '.join(it_companies)
print(result)

# Check if a certain company exists in the it_companies list.
print(it_companies.index('Microsoft'))

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[:3])

# Slice out the last 3 companies from the list
print(it_companies[-1:-4:-1])

# Slice out the middle IT company or companies from the list
print(it_companies[4:5])

# Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# Remove the middle IT company or companies from the list
del it_companies[4]
print(it_companies)

# Remove the last IT company from the list
del it_companies[-1]
print(it_companies)

# Remove all IT companies from the list
del it_companies[0:]
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
code = front_end + back_end

# After joining the lists in question, Copy the joined list and assign it to a variable full_stack.
full_stack = code.copy()
print(full_stack)

# Then insert Python and SQL after Redux.
new=['Python','SQL']
full_stack.insert(5, new)
print(full_stack)

# Exercises: Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
print(max(ages))
print(min(ages))

# Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(len(ages)) # gives the odd number of 12
median = ages[5:7] # slice the two middle items
print(median)
a,b = median
median = (a+b)/2
print(f"median is {median}")

# Find the average age (sum of all items divided by their number )
mean = sum(ages) / len(ages)
print(f"mean of {ages} is {sum(ages)}/{len(ages)} \n mean = {mean}")

# Find the range of the ages (max minus min)
print(f"Range = {max(ages) - min(ages)}")

# Compare the value of (min - average) and (max - average), use abs() method

min_x = abs(mean - min(ages))
max_x = abs(mean - max(ages))

print(f"the difference between the min. and the average is {min_x}")
print(f"the difference between the max. and the average is {max_x}")

# Find the middle country(ies) in the countries list
country_list = countries = [
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

def find_middle(lst): #Function to find the middle country
    if not lst:
        return "The list is empty."
    length = len(lst)
    if length % 2 != 0: # if the length is odd
        middle_index = length // 2
        return lst[middle_index]
    first_middle_index = length // 2 - 1 # firsth value if the length is even
    second_middle_index = length // 2 # fsecond value if the length is even
    return (lst[first_middle_index], lst[second_middle_index])

middle_country = find_middle(country_list)
print(middle_country)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
def divide_lst(lst):
    if not lst:
        return "The list is empty."
    length = len(lst)
    if length % 2 != 0: # if the length is odd
        middle_index = length // 2
        list1 = lst[ : middle_index]
        list2 = lst[middle_index : ]
        print(list1)
        print(list2)
    else:
        first_middle_index = length // 2 - 1
        list1=lst[first_middle_index] 
        second_middle_index = length // 2 
        list2 =lst[second_middle_index]
        print(list1)
        print(list2)
print(divide_lst(country_list))

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

min_countries =['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic_countries = min_countries[0:3]
print(scandic_countries)