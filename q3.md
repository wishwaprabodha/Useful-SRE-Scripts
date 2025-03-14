# SSL Cer­ti­fi­ca­te Ex­pi­ry Mo­ni­tor

This Python script reads a list of domain names from a file and checks the expiration date of their SSL certificates. If any certificate is due to expire within 15 days, the script prints a warning message.

## Features

- **Domain List Input:**
  Reads domain names from a specified file (one domain per line).

- **SSL Certificate Checking:**
  Establishes an SSL connection on port 443 for each domain to retrieve its certificate.

- **Expiry Date Extraction:**
  Parses the certificate to extract the expiry date.

- **Alert Notification:**
  Notifies if a certificate is expiring soon (within 15 days).

- **Error Handling:**
  Catches and reports errors during connection or certificate retrieval.

## Prerequisites

- **Python Version:**
  Python 3.x is required.

- **Dependencies:**
  The script uses built-in Python libraries:
  - `ssl`
  - `socket`
  - `datetime`

No additional packages need to be installed.

## Usage

1. **Configure the DNS File Path:**
   Edit the `read_dns_file()` function to specify the correct path to your DNS file (e.g., `{venv_path}/dns.txt`).

2. **Prepare the DNS File:**
   Create a text file containing domain names, one per line. For example:
   ```txt
   example.com
   google.com
