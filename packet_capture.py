from scapy.all import sniff

class PacketSniffer:
    def __init__(self, ids):
        self.ids = ids

    def start_sniffing(self, interface):
        sniff(iface=interface, prn=self.ids.packet_callback, store=0)
