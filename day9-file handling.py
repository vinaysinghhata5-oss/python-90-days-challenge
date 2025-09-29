'''
Print today’s date in YYYY-MM-DD format.'''
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d")
print("Current date:", now)

'''
Print current time only in HH:MM:SS format.'''
from datetime import datetime

now = datetime.now().strftime("%H:%M:%S")
print("Current time:", now)

'''
Parse "2025-12-31" into a datetime object.
'''
date_string = "2025-12-31"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed date:", parsed_date)

'''
Print the date 7 days from today.
'''
from datetime import datetime, timedelta

seven_days_later = datetime.now() + timedelta(days=7)
print("Date 7 days from today:", seven_days_later.strftime("%Y-%m-%d"))


'''
Search today’s date in system.log.
'''
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
with open("system.log", "r") as file:
    for line in file:
        if today in line:
            #print("Found today's date in log:", line.strip())
            print(line)
    

