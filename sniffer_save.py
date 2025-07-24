#!/usr/bin/env python3

from scapy.all import sniff, wrpcap

PACKET_COUNT = 100
INTERFACE = "eth0"
PCAP_FILENAME = "capture.pcap"

print(f"[+] Capturing {PACKET_COUNT} packets on {INTERFACE}...")
packets = sniff(count=PACKET_COUNT, iface=INTERFACE)

print(f"[+] Saving to {PCAP_FILENAME}...")
wrpcap(PCAP_FILENAME, packets)

print("[+] Done.")
