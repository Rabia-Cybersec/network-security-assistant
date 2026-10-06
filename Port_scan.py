import socket

def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

host = "127.0.0.1"

# Test every port from 1 to 9000
for port in range(1, 9001):
    if is_port_open(host, port):
        print(f"Port {port} is open")
