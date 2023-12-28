# Day 16: 30 days of Python programming

from datetime import datetime,date,time,timedelta
# Get the current day, month, year, hour, minute and timestamp from datetime module
current = datetime.now()
print(current) 
day = current.day
month = current.month
year = current.year
hour = current.hour
minute = current.minute
timestamp = current.timestamp()

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
t = current.strftime("%m/%d/%Y, %H:%M:%S")
print(t)


# Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


# Calculate the time difference between now and new year.
todays_day = current.date()
new_year = date(2024,1,1)
difference = new_year - todays_day
print(f'Time to new year is {difference} ')


# Calculate the time difference between 1 January 1970 and now.
# I have already assigned the current year,month and day from above
print(current.date() - date(1970,1,1)) #19702 days

# Think, what can you use the datetime module for? Examples:
#   - Working with timezones
#   - Calculating ages
#   - Arithemetic calculatons