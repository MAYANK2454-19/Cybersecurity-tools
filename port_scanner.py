import socket 

target = input("Enter the name of your target : ")
max_ports = int(input("Enter the maximum port number to check : "))
open_ports = 0
ports_list = []
try :
    ip = socket.gethostbyname(target)
    print(f"Scanning {target} ({ip})...")
    for port in range (1,max_ports+1):
        sock=socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip,port))
        print(f"Scanning port {port}")
        if result == 0 :
            print(f"Port {port} is open on {target} ({ip}).")
            open_ports += 1
            ports_list.append(port)
        sock.close()
except socket.gaierror :
    print(f"{target} is not a valid hostname.")
finally :
    print(f"Scan completed. {open_ports} open ports found.")
    if open_ports > 0 :
        print(f"Open ports: {ports_list}")
