# ERPNext Field Service Management (FSM) & SLA Dispatcher

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![FSM](https://img.shields.io/badge/Field%20Service-SLA%20Routing%20%26%20Van--Stock-orange.svg)](https://frappe.io)

Heavy equipment, elevator, and HVAC manufacturers face severe SLA penalties when emergency breakdown tickets are delayed. This engine integrates Haversine geolocation distance routing, technician skill matrix certification, and van-stock inventory reservations.

## Features
- **Haversine Geolocation Routing:** Computes true geodesic kilometers between live technician GPS locations and breakdown sites.
- **Skill Matrix Validation:** Ensures only certified technicians are dispatched to high-voltage or complex mechanical failures.
- **Van-Stock Inventory Consumption:** Real-time mobile truck warehouse inventory verification preventing double visits.

## Tests
```bash
python3 -m unittest discover tests
```
