import threading
import json
from functions import get_banner, get_ip
from cybertools.open_ports import port_scan
from detect_service import detect_service
from header_parser import head_parser
from https_banner import get_https_banner
from reverse_lookup import reverse_lookup

hostname = input("Enter the hostname to scan: ").strip()
ip = get_ip(hostname)
if ip is None:
    print("Unable to resolve hostname.")
    quit()
all_ports = []
CHUNK_SIZE = 50
dns_reverse = reverse_lookup(str(ip))
#threads

threads = []

for start in range(1, 501, CHUNK_SIZE):
    t = threading.Thread(
        target=port_scan,
        args=(ip, hostname, start, start + CHUNK_SIZE - 1, all_ports)
    )

    threads.append(t)

#threaing start 
for t in threads:
    t.start()

#threads waiting
for t in threads:
    t.join()

all_ports.sort()
print(f"Open ports on {hostname} ({ip}): {all_ports}")
print("Port scanning completed.")

results = {}

for port in all_ports:
    results[port] = {
        "service": detect_service(port),
        "headers": head_parser(get_banner(ip, hostname, port)) if port != 443 else head_parser(get_https_banner(ip, hostname, port))
        
    }
report = {"hostname": hostname, 
          "ip": ip, 
          "reverse_dns" : dns_reverse,
          "open_ports": results}
with open("scan_results.json", "w") as file :
    json.dump(report, file, indent = 4)
print("Detected services on open ports have been saved to scan_results.json")
# print(results)