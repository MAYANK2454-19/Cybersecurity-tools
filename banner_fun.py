import socket
from dns_lookup import get_ip   
def get_banner(ip: str, hostname: str, port: int) -> str | None:
    try :
        msg = f"HEAD / HTTP/1.1\r\nHost: {hostname}\r\n\r\n"
        sock=socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip,port))
        if result == 0 :
            sock.send(msg.encode())
            banner = sock.recv(1024)
            sock.close()
            return banner.decode(errors='ignore')
        else:
            sock.close()
            return None
    except socket.gaierror :
        print(f"{hostname} is not a valid hostname.")
        return None