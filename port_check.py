import socket 
sock= socket.socket()
target = input("Enter the name of your target : ")
port = int(input("Enter the port you want to check : "))
result = sock.connect_ex((target,port))
print(result)