import os
for file in os.listdir():
    if file.endswith('.log'):
        print(file)

    if 'backup_logs' not in os.listdir():
        os.mkdir('backup_logs')
        print('Directory created')
        break

    else:
        print('Directory already exists')
        break

with open("old_file.txt","w") as new:
    new.write("This is a new file")
    os.rename("old_file.txt","new_file.txt")
    print("File renamed successfully")


import sys
name=sys.argv[1]
print(f"hello {name}")

a=int(sys.argv[2])
b=int(sys.argv[3])
print(f"The sum is {a+b}")


status=sys.argv[4]
if status=="--stop":
    print("Script terminated")
else:
    print("Script running")

import subprocess
c=subprocess.run(["ls","-lrth"], capture_output=True, text=True)
print(c.stdout)

create=subprocess.run(["mkdir","test_dir"])
print("Directory created")

error=subprocess.run(["ls","-lart","non_existent_file"], capture_output=True, text=True)
print("Error message:", error.stderr)