import socket 
sock= socket.socket()
target = input("Enter your target : ")
ip = socket.gethostbyname(target)
print("The IP address of " + target + " is : " + ip)