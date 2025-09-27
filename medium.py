'''
Medium (5 Questions)

Extract IP addresses
From a log file nginx.log, extract and print all unique IP addresses that caused "404" errors.

Filter log by date
Write a script to print all log lines from application.log that occurred on the current date (assume the date format in log is YYYY-MM-DD).

Append data to a file safely
Append the line "Deployment completed successfully" to deployment.log, ensuring that if the file does not exist, it is created.

Read CSV file and summarize
Given a CSV file servers.csv with columns ServerName,CPU,Memory, print the name of the server with the highest CPU usage.

Count multiple error codes
Given a log file system.log, count how many lines contain any of the error codes ["403", "404", "500"]

'''
unique_ips=set()
with open("nginx.log", "r") as log:
    for line in log:
        if "404" in line:
            ip=line.split()[0]
            unique_ips.add(ip)
for ip in unique_ips:
    print(ip)


from datetime import datetime
c=datetime.now()
formate=c.strftime("%Y-%m-%d")
print(formate)



with open("app.log","r") as l:
    for line in l:
        if formate in line:
            print(line)


'''
Append the line "Deployment completed successfully" to deployment.log, ensuring that if the file does not exist, it is created.
'''
with open("deployment.log","w") as wr, open("deployment.log","a") as a:
    a.write("Deployment completed successfully")

m=70
import csv
with open("servers.csv","r") as r:
    reader=csv.DictReader(r)
    print(reader)
    for row in reader:
        if int(row["CPU"]) > m:
        
            print(f"{row['ServerName']} ----> {row['CPU']}")

erro=["403", "404", "500"]
count=0
try:
    with open("system.log","r") as u:
        for y in u:
           if any(code in y for code in ["403", "404", "500"]) :
                count+=1
                print(y.strip())

    print(f"Total error lines: {count}")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print("file is error")




