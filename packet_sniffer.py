from scapy.all import sniff, IP
import threading

# Store captured packets
captured_packets = []

def process_packet(packet):
    if IP in packet:

        # Convert protocol numbers to names
        protocol_map = {
            1: "ICMP",
            6: "TCP",
            17: "UDP"
        }

        protocol = protocol_map.get(
            packet[IP].proto,
            str(packet[IP].proto)
        )

        packet_info = {
            "source": packet[IP].src,
            "destination": packet[IP].dst,
            "protocol": protocol
        }

        captured_packets.append(packet_info)

        # Keep only the latest 50 packets
        if len(captured_packets) > 50:
            captured_packets.pop(0)

def get_packets():
    return captured_packets

def start_sniffing():
    sniff(prn=process_packet, store=False)

# Run packet capture in background
sniffer_thread = threading.Thread(
    target=start_sniffing,
    daemon=True
)

sniffer_thread.start()