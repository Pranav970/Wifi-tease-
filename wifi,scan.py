import scapy.all as scapy

def get_mac(ip): arp_request = scapy.ARP(pdst=ip) broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") arp_request_broadcast = broadcast / arp_request answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

if answered_list:
    return answered_list[0][1].hwsrc
return None

def scan_network(network_range): arp_request = scapy.ARP(pdst=network_range) broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") arp_request_broadcast = broadcast / arp_request answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

devices = []
for sent, received in answered_list:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})
return devices

def main(): network_range = "192.168.1.1/24"  # Adjust according to your router print("Scanning network...") devices = scan_network(network_range)

if devices:
    print("Connected devices:")
    for device in devices:
        print(f"IP: {device['ip']} - MAC: {device['mac']}")
else:
    print("No devices found.")

if name == "main": main()

