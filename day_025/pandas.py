import pandas as pd

# Read the hacker_news.csv file
file_path = "data/hacker_news.csv"
df = pd.read_csv(file_path)

# Get the first five rows
first_five_rows = df.head()

# Get the last five rows
last_five_rows = df.tail()

# Get the title column as a pandas series
title_series = df['title']

# Count the number of rows and columns
num_rows, num_columns = df.shape

# Filter the titles which contain 'python'
python_titles = df[df['title'].str.contains('python', case=False)]

# Filter the titles which contain 'JavaScript'
javascript_titles = df[df['title'].str.contains('JavaScript', case=False)]

# Explore the data and make sense of it
data_summary = df.describe(include='all')

# Print results
print("First five rows:")
print(first_five_rows)
print("\nLast five rows:")
print(last_five_rows)
print("\nTitle column as pandas series:")
print(title_series)
print("\nNumber of rows and columns:")
print(f"Rows: {num_rows}, Columns: {num_columns}")
print("\nTitles containing 'python':")
print(python_titles)
print("\nTitles containing 'JavaScript':")
print(javascript_titles)
print("\nData Summary:")
print(data_summary)
