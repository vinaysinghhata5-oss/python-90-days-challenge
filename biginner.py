'''
Beginner (5 Questions)

Read a file line by line
Write a Python script to open a file called example.txt and print each line with its line number.

Count occurrences
Given a log file access.log, count how many times the string "ERROR" appears in the file.

Write to a file
Write a Python script that writes a list of server names ["server1", "server2", "server3"] into a file called servers.txt, one name per line.

Check if a file exists
Write a Python function that takes a file path as input and prints "File exists" if it exists, otherwise prints "File not found".

Copy contents from one file to another
Write a Python script that reads source.txt and writes its contents into destination.txt.


'''
with open("example.txt","r") as f:
    for i,line in enumerate(f, start=1):
        print(i,line)


c=0
with open("access.log","r") as r:
    for line in r:
        if "ERROR" in line:
            c+=1
print(f"ERROR COUNT is:{c}")


servers = ["server1", "server2", "server3"]
with open("servers.txt","w") as s:
    for i in servers:
        s.write(i + "\n")


with open("application.log","r") as src ,open("deployment.log","w") as des:
    for line in src:
        des.write(line)


'''
Check if a file exists
'''
try:
  with open("read.txt","r") as re:
    re.read()
    print("File found")
except FileNotFoundError:
    print("file not found")