# RIMZI Wi-Fi Scanner (Termux - Non Root)

A simple Wi-Fi scanner tool built in Python for Termux (non-rooted Android).  
Displays nearby SSID, BSSID, signal strength, frequency & encryption type.

## 🔧 Requirements

- Termux App
- Termux:API App (from Play Store)
- Python 3
- `termux-api` package

## 🛠 Installation

```bash
pkg update && pkg install python termux-api -y
pip install rich
