# main.py
# Main entry point of the Network Scanner CLI tool

from scanner import scan
from storage import save_to_file

def main():
    print("=" * 40)
    print("   Network Scanner - CLI Tool")
    print("=" * 40)

    # Ask the user to enter the IP range to scan
    ip_range = input("\n[?] Enter IP range to scan (e.g. 192.168.1.0/24): ")

    print("\n[*] Scanning the network, please wait...")

    # Run the scan
    devices = scan(ip_range)

    # Display results
    if not devices:
        print("\n[-] No devices found.")
    else:
        print(f"\n[+] Found {len(devices)} device(s):\n")
        print(f"{'IP Address':<20} {'MAC Address'}")
        print("-" * 40)
        for device in devices:
            print(f"{device['ip']:<20} {device['mac']}")

        # Ask if user wants to save results
        save = input("\n[?] Save results to file? (y/n): ")
        if save.lower() == "y":
            save_to_file(devices)

    print("\n[*] Scan complete. Goodbye!")

if __name__ == "__main__":
    main()