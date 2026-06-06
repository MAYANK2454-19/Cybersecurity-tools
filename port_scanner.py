import socket 

target = input("Enter the name of your target : ")
port = int(input("Enter the port you want to check : "))
try :
    ip = socket.gethostbyname(target)
    for port in range (1,port+1):
        sock=socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip,port))
        if result == 0 :
            print(f"Port {port} is open on {target} ({ip}).")
        
except socket.gaierror :
    print(f"{target} is not a valid hostname.")
finally :
    sock.close()