import socket
import sys

def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# The target must be given on the command line
if len(sys.argv) != 2:
    print("Usage: python port_scan.py <host>")
    sys.exit(1)

host = sys.argv[1]
print(f"Scanning {host}...")

# Scan the well-known ports (1 to 1024)
for port in range(1, 1025):
    if is_port_open(host, port):
        print(f"Port {port} is open")
