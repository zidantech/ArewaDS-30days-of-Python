
# # Day 19 - File Handling

# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

def count_lines_words(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            len_lines = len(lines)
            words = ' '.join(lines).split()
            len_words = len(words)
            
            print(f"File: {path}")
            print(f"Number of lines: {len_lines}")
            print(f"Number of words: {len_words}")
            print("-" * 40)
    except FileNotFoundError:
        print(f"File '{path}' not found.")

paths = [
    r'data\obama_speech.txt',
    r'data\michelle_obama_speech.txt',
    r'data\donald_speech.txt',
    r'data\melina_trump_speech.txt'
]

for path in paths:
    count_lines_words(path)


# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json

def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    languages_count = {}
    for country_info in data:
        languages = country_info.get('languages', [])
        for language in languages:
            languages_count[language] = languages_count.get(language, 0) + 1

    sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:top_n]

file_path = 'data\countries_data.json'

# Get the 10 most spoken languages
print(most_spoken_languages(filename=file_path, top_n=10)) 

# Get the 3 most spoken languages
print(most_spoken_languages(filename=file_path, top_n=3))

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

def most_populated_countries(filename, n):
    with open(filename, 'r') as file:
        data = json.load(file)
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    top_countries = sorted_countries[:n]

    for country in top_countries:
        print(f"Country: {country['name']}, Population: {country['population']}")
filename = 'data/countries_data.json'

most_populated_countries(filename, 10)
print()
most_populated_countries(filename, 3)


# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
with open('data\email_exchange_big.txt') as f:
    lines = f.readlines()
email_addresses = []
for line in lines:
    email_addresses.extend(re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line))
email_addresses[:]

# Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
import re
def find_most_common_words(file, n = 10):
    
    with open(file) as f:
        lines = f.readlines()
    words = []
    for line in lines:
        line = re.sub(r'[^\w\s]','',line)
        words.extend(line.split())
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word,0) + 1
    words_sorted = sorted(words_dict.items(),key=lambda x:x[1],reverse=True)
    result = [(word[1],word[0]) for word in words_sorted]
    return result[:n]



# Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
print(find_most_common_words('data\obama_speech.txt', 10))

# b) The ten most frequent words used in Michelle's speech 
print(find_most_common_words('data\michelle_obama_speech.txt', 10))

# c) The ten most frequent words used in Trump's speech 
print(find_most_common_words('data\donald_speech.txt', 10))

# d) The ten most frequent words used in Melina's speech
print(find_most_common_words('data\melina_trump_speech.txt', 10))


# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
def clean_text(file):
    with open(file) as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line = re.sub(r'[^\w\s]','',line)
            words.extend(line.split())
    return words


clean_text('data\michelle_obama_speech.txt')


from data.stop_words import stop_words
def remove_stop_words(list):
    return [word for word in list if word.lower() not in stop_words]
remove_stop_words(clean_text('data\michelle_obama_speech.txt')) 

def check_text_similarity(list_one,list_two):
    res = [x for x in (list_one + list_two) if x in list_one and x in list_two]
    similar_words_percent = (len(res)/(len(list_one) + len(list_two))) * 100
    return similar_words_percent
check_text_similarity(['apple','banana','mango','pawpaw'],['apple','mango','pear'])


def comparing_text_in_file_similarity(file_one,file_two):
    file_one_words = remove_stop_words(clean_text(file_one))
    file_two_words = remove_stop_words(clean_text(file_two))
    return check_text_similarity(file_one_words,file_two_words)

comparing_text_in_file_similarity('data\michelle_obama_speech.txt','data\melina_trump_speech.txt') 


# Find the 10 most repeated words in the romeo_and_juliet.txt

print(find_most_common_words('data\romeo_and_juliet.txt'))


'''Read the hacker news csv file and find out:
a) Count the number of lines containing python or Python 
b) Count the number lines containing JavaScript, javascript or Javascript
c) Count the number lines containing Java and not JavaScript'''

import csv
with open('data\hacker_news.csv',newline='') as f:
    csv_reader = csv.reader(f,delimiter=',')
    python_rows = 0
    javascript_rows = 0
    java_rows = 0
    for row in csv_reader:
        for i in range(len(row)):
            if re.findall(r'[Pp]ython',row[i]):
                python_rows += 1
            elif re.findall(r'[Jj]ava[Ss]cript',row[i]):
                javascript_rows +=1
            elif re.findall(r'Java$',row[i]):
                java_rows +=1
print(f'the number of lines containing a,b and c respectively are: {python_rows}, {javascript_rows} and {java_rows}')





