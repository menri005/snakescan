import argparse
import csv
import ipaddress
import socket

from concurrent.futures import ThreadPoolExecutor

# Define variables for output report
output_rows = []

# Parse arguments
parser = argparse.ArgumentParser(description="Python TCP Port Scanner (host or subnet)")
parser.add_argument("-t", "--target", required=True, help="Target host or subnet (CIDR)")
parser.add_argument("-p", "--ports", default="1-1024",
                    help="Ports (comma-separated or ranges, e.g., 22,80,443,8000-8080)")
args = parser.parse_args()

# Parse ports (allow ranges and individual ports)
ports = set()
for part in args.ports.split(","):
    if "-" in part:
        start, end = part.split("-")
        ports.update(range(int(start), int(end) + 1))
    else:
        ports.add(int(part))
ports = sorted(ports)

# set the timeout to seconds
# could be set to less than 1 for faster scanning (but more false positives)
timeout = 1

# Determine if target is a single host or subnet
try:
    network = ipaddress.ip_network(args.target, strict=False)
except ValueError:
    print("Invalid target. Use an IP address or subnet (e.g., 192.168.1.0/24).")
    exit(1)

# Port scanning function
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((str(ip), port))
            if result == 0:
                print(f"[+] {ip} Port {port} is open")
                output_rows.append(
                    {
                        'IP Address': str(ip),
                        'Port': str(port)
                    }
                )
    except Exception:
        pass

# Scan function per host
# note you can raise the max workers to 500 but
# this may cause instability on the host running the scan
# or trip up network defenses as too many
# threads / connections would pop up
def scan_host(ip):
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda port: scan_port(ip, port), ports)

# Scan all hosts in network
for host in network.hosts():
    scan_host(host)

# write results out to CSV report
if output_rows:
    with open('results.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=output_rows[0].keys())
        writer.writeheader()
        writer.writerows(output_rows)
else:
    print('No open ports were found for the provided targets.')
