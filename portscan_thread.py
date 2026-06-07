import threading
from functions import get_banner, get_ip
from new_fun import port_scan
from detect_service import detect_service
hostname = input("Enter the hostname to scan: ")
ip = get_ip(hostname)
all_ports = []
CHUNK_SIZE = 50

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
        "banner": get_banner(ip, hostname, port)
    }
print("Detected services on open ports:")
print(results)