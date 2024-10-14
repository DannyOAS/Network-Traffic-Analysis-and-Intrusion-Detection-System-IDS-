from packet_capture import PacketSniffer
from detection import IDS

if __name__ == "__main__":
    ids = IDS()
    sniffer = PacketSniffer(ids)
    
    try:
        print("[INFO] Starting Network Traffic Sniffer...")
        sniffer.start_sniffing(interface="eth0")  # Change interface based on your system
    except KeyboardInterrupt:
        print("\n[INFO] Stopping IDS and generating traffic report...")
        ids.visualize_traffic()
        ids.save_log()
