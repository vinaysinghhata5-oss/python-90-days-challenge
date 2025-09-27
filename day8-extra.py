'''
Q1. Search for "ERROR" in a Log File
'''
with open("system.log","r") as f:
    for line in f:
        if "ERROR" in line:
            print(line) 

'''
Q2. Count "404" Errors in a Log File
'''
c=0
with open("nginx.log","r") as n:
    for line in n:
        if "404" in line:
           c+=1
print(f"Total 404 errors:",c)


'''
Q3. Extract IP Addresses from a Log File
'''
with open("nginx.log","r") as t:
    for line in t:
        ip=line.split()[0]
        print(ip)

'''
Q4. Count Log Levels
👉 Count how many ERROR, INFO, and WARNING lines are there using a dictionary.
'''
e=0
i=0
w=0
with open("psql.log","r") as p:
    for line in p:
        if "ERROR" in line:
            e+=1
        elif "INFO" in line:
            i+=1
        elif "WARNING" in line:
            w+=1
        else:
            print(f"no other error")
print(f"erro count is",e)
print(f"info count is",i)
print(f"Warninf count is:",w)

'''
QA: 4 print the ip of 404 in log 
'''

with open("nginx.log","r") as c:
    for line in c:
        if "404" in line:
            t=line.split()
            ip=t[0]
            date=t[3].strip("[")
            print(ip,date)