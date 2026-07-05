# Network Scanner — CLI Tool

A Python command-line tool that scans a local network, detects connected devices, and displays their IP and MAC addresses. Results can be exported to a CSV file.

## Features
- Scan any local network range (e.g. 192.168.1.0/24)
- Detect all connected devices automatically
- Display IP Address and MAC Address for each device
- Export results to a timestamped CSV file

## Technologies Used
- Python 3
- Scapy library
- CSV module

## Installation

Install the required library using this command:

    pip install scapy

## Usage

Run the tool using this command:

    python main.py

Then enter your network range when prompted, for example: 192.168.1.0/24

## Project Structure

    network-scanner/
    ├── main.py          Main entry point
    ├── scanner.py       Network scanning logic
    ├── storage.py       CSV export logic
    └── requirements.txt Dependencies

## Author
Ali Belarrem — First Year Computer Science Student