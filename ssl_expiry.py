import ssl
import socket
from datetime import datetime


def read_dns_file():
    with open("path/to/venv/dns.txt", "r") as file:
        for line in file:
            get_ssl_expiry(line.strip())
def get_ssl_expiry(domain, port=443):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        expiry_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
        days_left = (expiry_date - datetime.now()).days
        print(f"SSL certificate for {domain} expires on: {expiry_date}")
        if days_left <= 15:
            print(f"SSL certificate for {domain} to expire soon: {expiry_date}")
            # invoke alert fn
    except Exception as e:
        return f"Error: {e}"

read_dns_file()