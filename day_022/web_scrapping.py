
# # Day 22 - Web Scrapping

# Scrape the following website and store the data as json file
# (url = 'http://www.bu.edu/president/boston-university-facts-stats/').

import requests
from bs4 import BeautifulSoup
import json

# Specify the URL
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the data you want to scrape using BeautifulSoup methods
    # For example, let's extract all the paragraphs in this case
    paragraphs = soup.find_all('p')

    # Create a list to store the extracted data
    data_list = []

    # Iterate through the paragraphs and extract text content
    for paragraph in paragraphs:
        data_list.append(paragraph.get_text())

    # Create a dictionary to store the data
    data_dict = {'paragraphs': data_list}

    # Convert the dictionary to JSON format
    json_data = json.dumps(data_dict, indent=4)

    # Save the JSON data to a file
    with open('scraped_data.json', 'w') as json_file:
        json_file.write(json_data)

    print('Data has been successfully scraped and stored as "scraped_data.json".')

else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')


# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# Specify the URL
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table on the page using BeautifulSoup methods
    table = soup.find('table')

    # Use pandas to read the HTML table into a DataFrame
    df = pd.read_html(str(table))[0]

    # Convert the DataFrame to a JSON object
    json_data = df.to_json(orient='records', indent=4)

    # Save the JSON data to a file
    with open('table_data.json', 'w') as json_file:
        json_file.write(json_data)

    print('Table data has been successfully extracted and stored as "table_data.json".')

else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')


# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
import requests
from bs4 import BeautifulSoup
import json

# Specify the URL
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with the class 'wikitable' on the page
    table = soup.find('table', {'class': 'wikitable'})

    # Extract the table rows
    rows = table.find_all('tr')

    # Create a list to store the data
    data_list = []

    # Iterate through the rows and extract the data
    for row in rows[1:]:  # Skip the header row
        columns = row.find_all(['th', 'td'])
        president_data = [column.get_text(strip=True) for column in columns]
        data_list.append(president_data)

    # Create a list of dictionaries representing each president's data
    presidents_data = []
    for president_data in data_list:
        president_dict = {
            "Number": president_data[0],
            "President": president_data[1],
            "Took office": president_data[2],
            "Left office": president_data[3],
            "Party": president_data[4],
            "Home state": president_data[5]
        }
        presidents_data.append(president_dict)

    # Convert the list of dictionaries to JSON format
    json_data = json.dumps(presidents_data, indent=4)

    # Save the JSON data to a file
    with open('presidents_data.json', 'w') as json_file:
        json_file.write(json_data)

    print('Presidents data has been successfully scraped and stored as "presidents_data.json".')

else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')



