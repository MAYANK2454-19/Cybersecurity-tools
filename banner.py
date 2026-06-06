import socket
target = input("Enter the name of your target : ")
port = int(input("Enter the port number to check : "))
msg = f"HEAD / HTTP/1.1\r\nHost: {target}\r\n\r\n"
sock=socket.socket()
try :
    ip = socket.gethostbyname(target)
    sock.settimeout(1)
    result = sock.connect_ex((ip,port))
    if result == 0 :
        sock.send(msg.encode())
        banner = sock.recv(1024)
        print(f"Banner for {target} ({ip}): {banner.decode(errors='ignore')}")
except socket.gaierror :
    print(f"{target} is not a valid hostname.")
finally :
    sock.close()