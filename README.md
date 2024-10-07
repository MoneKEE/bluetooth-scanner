### Bluetooth Scanner

This script is designed to scan for Bluetooth peripherals using the CoreBluetooth API in Python. It discovers peripherals, connects to them, and retrieves services and characteristics offered by these peripherals. Here’s a detailed breakdown of the script:

#### Features
- **Peripheral Discovery**: Scans for nearby Bluetooth peripherals and lists them.
- **Connection Management**: Manages connections to discovered peripherals.
- **Service Discovery**: Discovers services offered by connected peripherals.
- **Characteristic Discovery**: Retrieves characteristics of the discovered services.

#### How to Use
1. **Installation**: Ensure you have the required libraries installed. You can install them using:
   ```bash
   pip install pyobjc-framework-CoreBluetooth
   ```
2. **Running the Script**: Execute the script using Python:
   ```bash
   python blue_tooth_scan_v1.py
   ```
3. **Scanning**: The script will start scanning for peripherals automatically.

#### Key Components
- **MyCentralManagerDelegate**: A class that handles various Bluetooth events such as discovering peripherals, connecting to peripherals, discovering services, and characteristics.
- **Peripheral List**: Maintains a list of discovered peripherals and their details.
- **Connection Handling**: Manages connecting and disconnecting from peripherals.
- **Service and Characteristic Discovery**: Retrieves and prints the services and characteristics offered by the connected peripherals.

For detailed information, refer to the [source code](https://github.com/MoneKEE/Python-Code-Samples/blob/4a81b167d8f700aaf35595053b846be0b052c730/blue_tooth_scan_v1.py).
