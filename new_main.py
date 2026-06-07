from new_fun import port_scan
from dns_lookup import get_ip
hostname = input("Enter the hostname to scan: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))
ip = get_ip(hostname)
if ip is not None:
    print(f"IP address of {hostname} is {ip}")
    open_ports = port_scan(ip, hostname, start_port, end_port)
    if open_ports:
        print(f"Open ports on {hostname} ({ip}): {open_ports}")
    else:
        print(f"No open ports found on {hostname} ({ip}) in the range {start_port}-{end_port}.")