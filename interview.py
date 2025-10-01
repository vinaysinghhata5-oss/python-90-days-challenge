with open('app.log', 'r') as file:
    for line in file:
        if 'ERROR' in line:
            print(line.strip())


import subprocess

# Run df -h
output = subprocess.check_output(["df", "-h"]).decode()

for line in output.splitlines()[1:]:  # skip header
    parts = line.split()
    
    if len(parts) < 6:
        continue  # skip malformed lines
    
    filesystem = " ".join(parts[:-5])
    size, used, avail, use_percent, mount = parts[-5:]
    
    # Skip volumes with '-' in Use% (unavailable)
    if use_percent == '-':
        print(f"Skipping {mount} ({filesystem}) -> utilization not available")
        continue
    
    utilization = int(use_percent.strip('%'))
    
    print(f"Checking {mount} ({filesystem}) -> {utilization}% used")
    
    if utilization > 80:
        print(f"⚠️  Alert: {mount} utilization is above 80%")
    else:
        print(f"✅ {mount} utilization is within limits")


