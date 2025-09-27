'''
📝 Day 6 Practice Tasks

Given nums = [2,4,6,8,10,12], print:

First 3 elements

Last 2 elements

Reverse the list

Given msg = "DevOps with Python",

Print "DevOps"

Print "Python"

Convert to lowercase

Given csv_line = "error,warning,critical,info",

Split into a list

Print only "critical"

Join the list back with " | "
'''

def first_element(n):
    print(n[0:3])

n=[2,4,6,8,10,12]
first_element(n)


first_element(n[0:2])
print(n[::-1])
msg="DevOps with Python"
print(msg[0:6])
print(msg.lower())
csv_line="error,warning,critical,info"
print(csv_line.split())
parts=csv_line.split(",")
join="-".join(parts)
print(parts[2])
print(join)


'''
🎯 Bonus Challenge (Day 6)

Write a script that:

Takes a log line:
"ERROR 2025-09-25 Connection failed at server01"

Extracts only:

Log level (ERROR)

Date (2025-09-25)

Server name (server01)

👉 Use .split() and slicing.
'''
log="ERROR 2025-09-25 Connection failed at server01"
parts=log.split()
print(parts)
print(parts[0],parts[2])