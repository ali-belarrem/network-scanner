# scanner.py
# Responsible for scanning the local network and detecting connected devices

from scapy.all import ARP, Ether, srp

def scan(ip_range):
    # Create an ARP request to discover devices on the network
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send the packet and collect responses
    result = srp(packet, timeout=3, verbose=0)[0]

    # Store each discovered device's IP and MAC address
    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices