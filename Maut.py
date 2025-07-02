#!/usr/bin/env python3
import os
import json
import subprocess
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from time import sleep

console = Console()

# RIMZI Banner
def banner():
    os.system("clear")
    console.print(Panel.fit(f"""
[bold red]██╗██████╗ ███╗   ███╗███████╗██╗███████╗
██║██╔══██╗████╗ ████║██╔════╝██║██╔════╝
██║██████╔╝██╔████╔██║█████╗  ██║███████╗
██║██╔═══╝ ██║╚██╔╝██║██╔══╝  ██║╚════██║
██║██║     ██║ ╚═╝ ██║███████╗██║███████║
╚═╝╚═╝     ╚═╝     ╚═╝╚══════╝╚═╝╚══════╝

[bold yellow]Wi-Fi Scanner Tool - Termux (Non-Root)
[bold green]Coded By: RIMZI | For Educational Use Only!
""", border_style="orange1"))

# Scan Wi-Fi using termux-api
def scan_wifi():
    try:
        result = subprocess.check_output(['termux-wifi-scaninfo'], universal_newlines=True)
        networks = json.loads(result)
        return networks
    except Exception as e:
        console.print(f"[bold red]Error: {e}")
        return []

# Show scanned networks
def display_networks(networks):
    if not networks:
        console.print("[bold red]No Wi-Fi networks found or permission denied.")
        return

    table = Table(title="Nearby Wi-Fi Networks", header_style="bold magenta")
    table.add_column("SSID", style="bold cyan")
    table.add_column("BSSID", style="yellow")
    table.add_column("Signal (dBm)", justify="center", style="green")
    table.add_column("Frequency", style="white")
    table.add_column("Encryption", style="bold red")

    for net in networks:
        ssid = net.get("ssid", "Hidden")
        bssid = net.get("bssid", "Unknown")
        signal = str(net.get("level", "N/A"))
        freq = str(net.get("frequency", "N/A"))
        enc = "WPA/WPA2" if net.get("capabilities", "").find("WPA") != -1 else "Open"
        table.add_row(ssid, bssid, signal, freq, enc)

    console.print(table)

# Save to JSON (optional)
def save_to_file(networks):
    with open("wifi_results.json", "w") as f:
        json.dump(networks, f, indent=4)
    console.print("[bold green]✓ Wi-Fi results saved to [yellow]wifi_results.json")

# Main
def main():
    banner()
    console.print("[bold cyan]📶 Scanning for available Wi-Fi networks...\n")
    sleep(1.5)
    networks = scan_wifi()
    display_networks(networks)

    if networks:
        ask = console.input("\n[bold green]💾 Save to file? (y/n): ")
        if ask.lower() == 'y':
            save_to_file(networks)

if __name__ == "__main__":
    main()
