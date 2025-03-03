# RFID Blocking Application

This project detects unauthorized RFID scans and alerts users about potential skimming attacks. It helps protect personal and financial data from RFID-based threats.

## Features
- Detects RFID/NFC scans in real-time.
- Alerts the user when an unauthorized scan is detected.
- Provides Tag ID information to track potential threats.

## Prerequisites
1. **Hardware Requirements:**
   - An NFC reader/writer (e.g., ACR122U or PN532)

2. **Software Requirements:**
   - Python 3.x installed ([Download Python](https://www.python.org/downloads/))
   - `nfcpy` library for handling RFID/NFC communication

## Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/rfid-blocking-app.git
   cd rfid-blocking-app
   ```
2. **Install Dependencies:**
   ```sh
   pip install nfcpy
   ```

## Running the Application
1. Connect the NFC reader to your computer.
2. Run the following command:
   ```sh
   python rfid_blocking_app.py
   ```
3. The application will start detecting RFID scans and alert the user when an unauthorized scan is found.

## Usage Example
- If an unauthorized RFID scan occurs, the console will display:
  ```
  ⚠ Unauthorized RFID Scan Detected! ⚠
  Tag ID: <Detected Tag ID>
  Take necessary precautions!
  ```
