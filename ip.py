import socket 
try :
    target = input("Enter the name of your target : ")
    ip = socket.gethostbyname(target)
    print("The IP address of " + target + " is : " + ip)
except socket.gaierror :
    print(f"{target} is not a valid hostname.")

