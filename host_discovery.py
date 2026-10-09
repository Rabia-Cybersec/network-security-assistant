import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python host_discovery.py <prefix, e.g. 192.168.1>")
    sys.exit(1)

prefix = sys.argv[1]
print(f"Waking up {prefix}.1 to {prefix}.254...")

# Send one ping to every address so devices answer the ARP request
# (-n 1: one ping, -w 300: wait 300 ms; Windows syntax)
for last in range(1, 255):
    host = f"{prefix}.{last}"
    subprocess.run(["ping", "-n", "1", "-w", "300", host],
                   stdout=subprocess.DEVNULL)

# Read the ARP cache
output = subprocess.run(["arp", "-a"], capture_output=True, text=True).stdout

print("Devices seen on the network:")
for line in output.splitlines():
    if line.strip().startswith(prefix + "."):
        print(line.strip())
