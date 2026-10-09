import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python host_discovery.py <prefix, e.g. 192.168.1>")
    sys.exit(1)

prefix = sys.argv[1]
print(f"Waking up {prefix}.1 to {prefix}.254...")

for last in range(1, 255):
    host = f"{prefix}.{last}"
    subprocess.run(["ping", "-n", "1", "-w", "300", host],
                   stdout=subprocess.DEVNULL)

output = subprocess.run(["arp", "-a"], capture_output=True, text=True).stdout

devices = []
for line in output.splitlines():
    parts = line.split()
    # A valid ARP line looks like: IP  MAC  type
    if (len(parts) == 3
            and parts[0].startswith(prefix + ".")
            and parts[2].lower() in ("dynamic", "dynamique")):
        devices.append((parts[0], parts[1]))

print(f"{len(devices)} device(s) found:")
with open("results.txt", "w") as f:
    for ip, mac in devices:
        print(ip, mac)
        f.write(f"{ip} {mac}\n")
