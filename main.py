from port_scan_fun import scan_port
from banner_fun import get_banner
from dns_lookup import get_ip
target = input("Enter the name of your target : ")
ip = get_ip(target)
if ip is not None:
    print(f"IP address of {target} is {ip}")
    port = int(input("Enter the port number to check : "))
    if scan_port(ip, port):
        banner = get_banner(ip, target,port)
        if banner:
            print(f"Banner for {target} ({ip}): {banner}")
        else:
            print(f"Port {port} is open but no banner was retrieved.")
    else:
        print(f"Port {port} is closed on {target} ({ip}).")