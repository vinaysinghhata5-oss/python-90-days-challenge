'''
Q1. Logs from Last 2 Days
'''
from datetime import datetime, timedelta
date=(datetime.now()-timedelta(days=2)).strftime("%Y-%m-%d")
with open("system.log", "r") as file:
    for line in file:
        if date in line:
            print(line) 

from datetime import datetime, timedelta
count=0
date=datetime.now().strftime("%Y-%m-%d")
with open("system.log", "r") as file:
    for line in file:
        if date in line:
            count+=1
print("Number of log entries for today:", count)

'''
Q3. Earliest and Latest Log Entry'''
from datetime import datetime
log_dates = []
with open("system.log", "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) >= 2:
            log_date_str = parts[1]  # Assuming date is the second part
            try:
                log_date = datetime.strptime(log_date_str, "%Y-%m-%d")
                log_dates.append(log_date)
            except ValueError:
                continue
if log_dates:
    earliest_log = min(log_dates)
    latest_log = max(log_dates)
    print("Earliest log entry:", earliest_log)
    print("Latest log entry:", latest_log)
else:
    print("No valid log dates found.")

'''
Q5. Save Today’s Logs into New File
'''
from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")
with open("system.log", "r") as file:
    with open(f"logs_{today}.log", "w") as new_file:
        for line in file:
            if today in line:
                new_file.write(line)    