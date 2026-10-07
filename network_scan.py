import socket
import sys

# Common ports used to detect a live device
COMMON_PORTS = [22, 80, 443, 445]

def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.2)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

if len(sys.argv) != 2:
    print("Usage: python network_scan.py <prefix, e.g. 192.168.1>")
    sys.exit(1)

prefix = sys.argv[1]
print(f"Scanning {prefix}.1 to {prefix}.254...")

# Try every address of the network, from .1 to .254
for last in range(1, 255):
    host = f"{prefix}.{last}"
    open_ports = []
    for port in COMMON_PORTS:
        if is_port_open(host, port):
            open_ports.append(port)
    if open_ports:
        print(f"{host} -> open ports: {open_ports}")
