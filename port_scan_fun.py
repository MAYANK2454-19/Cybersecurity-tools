import socket

def scan_port(ip: str, port: int) -> bool:
    sock = socket.socket()
    sock.settimeout(1)

    result = sock.connect_ex((ip, port))

    sock.close()

    return result == 0