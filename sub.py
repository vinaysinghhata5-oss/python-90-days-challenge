import subprocess
disk=subprocess.check_output(["df","-h"]).decode()
print(disk)
for line in disk.splitlines():
    if line.endswith("/"):
        print(line)
        parts=line.split()
        print(parts)
        utilization=parts[4]
        print("Disk utilization is:",utilization)
