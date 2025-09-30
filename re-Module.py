import re
line="ERROR 2025-09-29 server01"
log=r"ERROR"
if re.search(log,line):
    print("Error found in the log line",re.search(log,line).group())
else:
    print("No error found")

#Extracting log level (ERROR, INFO, WARNING)
log_level=r"(ERROR|INFO|WARNING)"
with open("re_logs.txt","r") as f:
    for line in f:
        if re.search(log_level,line):
            print("Log level found in the log line",re.search(log_level,line).group())
        else:
            print("No log level found")

server=r"server\d+"
with open("re_logs.txt","r") as f:
    for line in f:
        if re.search(server,line):
            print("Server found in the log line",re.search(server,line).group())
        else:
            print("No server found")

#Extracting all numbers in each line (CPU, Memory, Disk) CPU=80 Memory=70 Disk=50
import re

with open("re_logs.txt", "r") as f:
    for line in f:
        # Find CPU/Memory/Disk with their values
        matches = re.findall(r"(CPU=\d+|Memory=\d+|Disk=\d+)", line, re.IGNORECASE)
        for match in matches:
            print(match)



