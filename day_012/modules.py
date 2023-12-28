
# # Day12 Assignment


# ## Excercise:Level1

#function which generates a six digit/character random_user_id
import random
import string

def generate_random_user_id():
    characters = string.ascii_lowercase + string.digits
    random_user_id = ''.join(random.choice(characters)
for i in range(6))
    return random_user_id
random_user_id = generate_random_user_id()
print(f"Random user ID: {random_user_id}")

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import random
import string

def user_id_gen_by_user():
    char_count = int(input("Enter the number of characters for each ID: "))
    id_count = int(input("Enter the number of IDs to be generated: "))

    user_ids = []
    for i in range(id_count):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=char_count))
        user_ids.append(user_id)
    return user_ids

generated_ids = user_id_gen_by_user()
print("Generated User IDs:", generated_ids)

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import random
import string

def user_id_gen_by_user():
    char_count = int(input("Enter the number of characters for each ID: "))
    id_count = int(input("Enter the number of IDs to be generated: "))

    user_ids = []
    for i in range(id_count):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=char_count))
        user_ids.append(user_id)
    return user_ids

generated_ids = user_id_gen_by_user()
print("Generated User IDs:", generated_ids)

#a function named rgb_color_gen that will generate rgb colors (3 values ranging from 0 to 255 each).
import random

def rgb_color_gen():
    red = random.randint(124, 125)
    green = random.randint(243, 244)
    blue = random.randint(255, 255)
    return (red, green, blue)
random_color = rgb_color_gen()
print(f"rgb: {random_color}")


# ## Excercise:Level2

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random

def list_of_hexa_colors(num_colors):
    colors = []
    for i in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        hex_color = f"#{red:02x}{green:02x}{blue:02x}"
        colors.append(hex_color)
    return colors
colors = list_of_hexa_colors(5)
print(f"Generated 5 random hexadecimal colors:")
for color in colors:
    print(f"\t- {color}")

# ## Excercise:Level2

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random

def list_of_hexa_colors(num_colors):
    colors = []
    for i in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        hex_color = f"#{red:02x}{green:02x}{blue:02x}"
        colors.append(hex_color)
    return colors
colors = list_of_hexa_colors(5)
print(f"Generated 5 random hexadecimal colors:")
for color in colors:
    print(f"\t- {color}")

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random

def list_of_rgb_colors(num_colors):
    colors = []
    for i in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colors.append([red, green, blue])
    return colors
colors = list_of_rgb_colors(5)
print(f"Generated 5 random RGB colors:")
for color in colors:
    print(f"\t- {color}")

#Write a function generate_colors which can generate any number of hexa or rgb colors.
import random

def generate_colors(num_colors, color_format="hexa"):
    colors = []
    for _ in range(num_colors):
        if color_format == "hexa":
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            hex_color = f"#{red:02x}{green:02x}{blue:02x}"
            colors.append(hex_color)
        elif color_format == "rgb":
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            colors.append((red, green, blue))
        else:
            raise ValueError(f"Invalid color format: {color_format}")
    return colors
colors = generate_colors(2, "hexa")
print(f"Generated 2 random hexadecimal colors:")
for color in colors:
    print(f"\t- {color}")

colors = generate_colors(2, "rgb")
print(f"Generated 2 random RGB colors:")
for color in colors:
    print(f"\t- {color}")

# ## Excercise: Level3

#Call function shuffle_list that takes and returns a shuffled list
import random

def shuffle_list(data):
    shuffled_data = data[:]
    for i in range(len(shuffled_data) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled_data[i], shuffled_data[j] = shuffled_data[j], shuffled_data[i]
    return shuffled_data
data = [2, 2, 1, 4, 5]
shuffled_data = shuffle_list(data)

print(f"Original data: {data}")
print(f"Shuffled data: {shuffled_data}")

#a function which returns an array of seven unique random numbers in a range of 0-9. 
import random

def generate_unique_random_numbers():
    unique_numbers = random.sample(range(10), 7)
    return unique_numbers

random_numbers = generate_unique_random_numbers()
print("Generated Random Numbers:", random_numbers)


