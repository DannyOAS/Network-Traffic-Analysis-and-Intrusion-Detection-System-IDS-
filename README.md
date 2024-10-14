# Network Traffic Intrusion Detection System (IDS)

## Overview
This project is a Python-based Intrusion Detection System (IDS) designed to monitor network traffic, detect suspicious activity such as SYN flood attacks, and alert the user. It also provides visualizations of the traffic distribution for better insight.

## Features
- **Real-time Traffic Monitoring**: Capture and analyze network packets.
- **Intrusion Detection**: Detects SYN floods and suspicious activity.
- **Email Alerts**: Sends email alerts when suspicious activity is detected.
- **Traffic Visualization**: Visualize network traffic using matplotlib.
- **Logging**: Logs suspicious activity in a log file.

## Requirements
- Python 3.x
- Scapy
- Matplotlib

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/yourusername/Network-Traffic-IDS.git
    ```
2. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

## Usage
1. Run the IDS:
    ```
    sudo python3 src/main.py
    ```
2. Interrupt the program using `Ctrl+C` to stop the IDS and generate the traffic visualization.

## Configuration
- Change the network interface in `main.py` as per your system's interface name (e.g., `eth0`, `wlan0`).
- If you want to enable email alerts, provide your SMTP details in `alert.py`.

## Logs
Suspicious activity will be logged in `logs/suspicious_activity.log`.

## Visualizations
Traffic visualization will be saved in the `visualizations/` directory.

## Future Improvements
- Add support for more attack signatures.
- Implement machine learning for anomaly detection.
