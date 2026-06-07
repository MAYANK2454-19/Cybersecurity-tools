import threading
from functions import get_ip
from new_fun import port_scan
hostname = input("Enter the hostname to scan: ")
ip = get_ip(hostname)
all_ports = []

#threads

t1=threading.Thread(target=port_scan, args=(ip, hostname, 1, 50,all_ports))
t2=threading.Thread(target=port_scan, args=(ip, hostname, 51, 100,all_ports))
t3=threading.Thread(target=port_scan, args=(ip, hostname, 101, 150,all_ports))
t4=threading.Thread(target=port_scan, args=(ip, hostname, 151, 200,all_ports))
t5=threading.Thread(target=port_scan, args=(ip, hostname, 201, 250,all_ports))

#threaing start 

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

#threads waiting

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
print(f"Open ports on {hostname} ({ip}): {all_ports}")
print("Port scanning completed.")