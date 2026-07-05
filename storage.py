# storage.py
# Responsible for saving scan results to a CSV file

import csv
from datetime import datetime

def save_to_file(devices):
    # Generate a unique filename using the current timestamp
    filename = f"scan_results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    # Write device data to the CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["ip", "mac"])
        writer.writeheader()
        writer.writerows(devices)

    print(f"\n[+] Results saved to: {filename}")
    return filename