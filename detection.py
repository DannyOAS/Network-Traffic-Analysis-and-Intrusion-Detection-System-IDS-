import matplotlib.pyplot as plt
from collections import Counter

class IDS:
    def __init__(self):
        self.suspicious_ips = []
        self.packet_count = Counter()
        self.suspicious_activity_log = []

    def packet_callback(self, packet):
        if packet.haslayer('IP'):
            src_ip = packet['IP'].src
            self.packet_count[src_ip] += 1

            # Detect SYN flood (an unusually high number of SYN packets from a single IP)
            if packet.haslayer('TCP') and packet['TCP'].flags == 'S':
                if self.packet_count[src_ip] > 10:  # Adjustable threshold
                    self.alert(src_ip)

    def alert(self, ip):
        print(f"[ALERT] Potential SYN flood attack detected from IP: {ip}")
        self.suspicious_activity_log.append(f"SYN flood detected from IP: {ip}")
        # Here we can also call the email alert function (in alert.py)

    def visualize_traffic(self):
        plt.bar(self.packet_count.keys(), self.packet_count.values())
        plt.xlabel('Source IP')
        plt.ylabel('Number of Packets')
        plt.title('Network Traffic Distribution')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig('../visualizations/traffic_plot.png')
        plt.show()

    def save_log(self):
        with open('../logs/suspicious_activity.log', 'w') as f:
            for log in self.suspicious_activity_log:
                f.write(log + "\n")
        print("[INFO] Suspicious activity log saved.")
