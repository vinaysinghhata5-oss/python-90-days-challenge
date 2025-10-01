import subprocess

disk=subprocess.check_output(["df","-h"]).decode()
print(disk)

for line in disk.splitlines():
    if line.endswith("/"):
        print(line)
        parts = line.split()
        utilization = parts[4]
        print("Disk utilization is:", utilization)
        
        # Check if utilization is above 80%
        if utilization != '-':
            usage_percent = int(utilization.strip('%'))
            if usage_percent > 80:
                print(f"⚠️  Alert: Root filesystem utilization is above 80% ({utilization})")
            else:
                print(f"✅ Root filesystem utilization is within limits ({utilization})")


ping_output = subprocess.run(["ping", "-c", "4", "8.8.8.8"], capture_output=True, text=True)
print(ping_output.stdout)
print(ping_output.stderr)
if ping_output.returncode == 0:
    print("Ping was successful")
else:
    print("Ping failed")