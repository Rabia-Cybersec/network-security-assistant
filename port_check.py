import socket

def is_port_open(host, port):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    # connect_ex returns 0 if the connection succeeds
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

print(is_port_open("127.0.0.1", 8000))
