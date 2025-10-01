import subprocess
c=subprocess.run(["pwd"],capture_output=True).stdout.decode().strip()
print(c)


user=subprocess.run(["whoami"],capture_output=True).stdout.decode().strip()
print(f"You are logged in as: {user}")



list=subprocess.run(["ls","-l"],capture_output=True).stdout.decode().strip()
print(list)
count=subprocess.run(["ls","-l"],capture_output=True).stdout.decode().strip().count("\n")
print(f"Total files and directories: {count}")


disk=subprocess.check_output(["df","-h"]).decode()
for line in disk.splitlines():
    if line.endswith("/"):
        print(line)

#Run a wrong command (like abcd) and handle the error gracefully.
error=subprocess.run(["abcd"],capture_output=True,text=True)
if error.returncode !=0:
    print("Command failed to execute")
    print("Error message:",error.stderr)
else:
    print("Command executed successfully")
    print(error.stdout)