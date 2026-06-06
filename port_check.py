import socket 
sock= socket.socket()
try :
    target = input("Enter the name of your target : ")
    port = int(input("Enter the port you want to check : "))
    ip = socket.gethostbyname(target)
    result = sock.connect_ex((ip,port))
    print(result)
    
except socket.gaierror :
    print(f"{target} is not a valid hostname.")
sock.close()