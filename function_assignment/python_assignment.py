# %% [markdown]
# # Funtion assignments

# %% [markdown]
# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly

# %%
def display_message():
    print("I am learning funtions")
    
display_message()

# %% [markdown]
# Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

# %%
def favorite_book(title):
    print(f"One of my favorite books is {title}")
    
favorite_book("Alice in Wonderland")
favorite_book("The thirty-nine step")

# %% [markdown]
# Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt. The function should print a 
# sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the 
# function a second time using keyword arguments.

# %%
def make_shirt(size, message):
    print(f"Shirt size: {size.upper()}, Message: '{message}'")

# Call the function using positional arguments
make_shirt("medium", "Hello World!")

# Call the function using keyword arguments
make_shirt(size="large", message="Python Rocks!")


# %% [markdown]
# Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message

# %%
def make_shirt(size="large", message="I love Python"):
    print(f"Shirt size: {size.capitalize()}, Message: '{message}'")

# Make a large shirt with default message
make_shirt()

# Make a medium shirt with default message
make_shirt(size="medium")

# Make a custom-sized shirt with a different message
make_shirt(size="small", message="Python is fun!")


# %% [markdown]
# Write a function called describe_city() that accepts the name of 
# a city and its country. The function should print a simple sentence, such as 
# Reykjavik is in Iceland. Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the 
# default country.

# %%
def describe_city(city, country="default country"):
    print(f"{city.capitalize()} is in {country.capitalize()}.")

# Call the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("New York")


# %% [markdown]
# Write a function called city_country() that takes in the name 
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values 
# that are returned.

# %%
def city_country(city, country):
    return f"{city.capitalize()}, {country.capitalize()}"

# Call the function with three city-country pairs
result1 = city_country("santiago", "chile")
result2 = city_country("tokyo", "japan")
result3 = city_country("new york", "united states")

# Print the returned values
print(result1)
print(result2)
print(result3)


# %% [markdown]
# Write a function called make_album() that builds a dictionary 
# describing a music album. The function should take in an artist name and an 
# album title, and it should return a dictionary containing these two pieces of 
# information. Use the function to make three dictionaries representing different 
# albums. Print each return value to show that the dictionaries are storing the 
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to 
# store the number of songs on an album. If the calling line includes a value for 
# the number of songs, add that value to the album’s dictionary. Make at least 
# one new function call that includes the number of songs on an album.

# %%
def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

# Make three dictionaries representing different albums
album1 = make_album("Ed Sheeran", "Divide")
album2 = make_album("Beyoncé", "Lemonade")
album3 = make_album("Coldplay", "A Head Full of Dreams", songs=12)

# Print each return value
print(album1)
print(album2)
print(album3)


# %% [markdown]
# Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created. Be sure to include a quit value in the while loop.

# %%
def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

while True:
    artist_input = input("Enter the artist's name (or 'quit' to exit): ")
    if artist_input.lower() == 'quit':
        break

    title_input = input("Enter the album title: ")

    # Call make_album with user input and print the dictionary
    album_info = make_album(artist_input, title_input)
    print(album_info)


# %% [markdown]
# Make a list containing a series of short text messages. Pass the 
# list to a function called show_messages(), which prints each text message.
# 
# 

# %%
def show_messages(messages):
    for message in messages:
        print(message)

# List of short text messages
text_messages = [
    "Hello, how are you?",
    "Don't forget to pick up groceries!",
    "Happy birthday! 🎉",
    "Learning Python is fun!",
]

# Call the function to print each text message
show_messages(text_messages)


# %% [markdown]
# Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and 
# moves each message to a new list called sent_messages as it’s printed. After 
# calling the function, print both of your lists to make sure the messages were 
# moved correctly.

# %%
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# List of short text messages
text_messages = [
    "Hello, how are you?",
    "Don't forget to pick up groceries!",
    "Happy birthday! 🎉",
    "Learning Python is fun!",
]

# Empty list to store sent messages
sent_messages = []

# Call the function to send and print messages
send_messages(text_messages, sent_messages)

# Print both lists to verify
print("Original messages:")
show_messages(text_messages)

print("\nSent messages:")
show_messages(sent_messages)


# %% [markdown]
# Archived Messages: Start with your work from Exercise 8-10. Call the func-
# tion send_messages() with a copy of the list of messages. After calling the func-
# tion, print both of your lists to show that the original list has retained its messages.

# %%
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# List of short text messages
text_messages = [
    "Hello, how are you?",
    "Don't forget to pick up groceries!",
    "Happy birthday! 🎉",
    "Learning Python is fun!",
]

# Create a copy of the list to pass to send_messages
messages_copy = text_messages.copy()

# Empty list to store sent messages
sent_messages = []

# Call the function to send and print messages using the copy
send_messages(messages_copy, sent_messages)

# Print both lists to verify
print("Original messages:")
show_messages(text_messages)

print("\nSent messages:")
show_messages(sent_messages)


# %% [markdown]
# Sandwiches: Write a function that accepts a list of items a person wants 
# on a sandwich. The function should have one parameter that collects as many 
# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.

# %%
def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item.capitalize()}")

# Call the function three times with different numbers of arguments
make_sandwich("turkey", "cheese", "lettuce")
make_sandwich("ham", "swiss")
make_sandwich("peanut butter", "jelly", "bread")


# %% [markdown]
# User Profile: Start with a copy of user_profile.py from page 148. Build a 
# profile of yourself by calling build_profile(), using your first and last names 
# and three other key-value pairs that describe you.

# %%
def build_profile(first_name, last_name, **additional_info):
    profile = {'first_name': first_name, 'last_name': last_name}
    profile.update(additional_info)
    return profile

# Create a profile for yourself
my_profile = build_profile(
    first_name="YourFirstName",
    last_name="YourLastName",
    age=25,
    occupation="Developer",
    location="City, Country"
)

print(my_profile)


# %% [markdown]
# Cars: Write a function that stores information about a car in a diction-
# ary. The function should always receive a manufacturer and a model name. It 
# should then accept an arbitrary number of keyword arguments. Call the func-
# tion with the required information and two other name-value pairs, such as a 
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was 
# stored correctly.

# %%
def make_car(manufacturer, model, **car_info):
    car = {'manufacturer': manufacturer, 'model': model}
    car.update(car_info)
    return car

# Call the function with required and additional information
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary to verify the stored information
print(car)


# %% [markdown]
# Printing Models: Put the functions for the example printing_models.py in a 
# separate file called printing_functions.py. Write an import statement at the top 
# of printing_models.py, and modify the file to use the imported functions.

# %%
from printing_functions import print_models, show_completed_models

# Sample data
unprinted_designs = ['phone case', 'pendant', 'keychain']
completed_models = []

# Using imported functions
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


'''In this example, the functions print_models and show_completed_models are defined in printing_functions.py, and they are imported into printing_models.py using the import statement. '''

# %% [markdown]
# Imports: Using a program you wrote that has one function in it, store that 
# function in a separate file. Import the function into your main program file, and 
# call the function using each of these approaches:
# - import module_name
# - from module_name import function_name
# - from module_name import function_name as fn
# - import module_name as mn
# - from module_name import *

# %%
import module

module.my_function()


# %%
from module import my_function

my_function()


# %%
from module import my_function as fn

fn()


# %%
import module as mn

mn.my_function()


# %%
from module import *

my_function()


# %% [markdown]
# Styling Functions: Choose any three programs you wrote for this chapter, 
# and make sure they follow the styling guidelines described in this section.

# %%
def describe_city(city, country='default country'):
    """Prints a simple sentence describing the city and country."""
    print(f"{city.capitalize()} is in {country.capitalize()}.")

# Example usage
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("New York")



