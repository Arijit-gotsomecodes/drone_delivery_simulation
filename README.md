<!-- README.md -->
# Drone Delivery Simulation with Mock Blockchain and 5G

## Description
This project simulates a drone delivery system with:
- Multiple drone missions (Idle, Pre-Flight, In-Flight, Delivered)
- A mock Hyperledger Fabric–style blockchain to log transactions immutably
- A simulated 5G network by adding random latency delays
- A Flask web dashboard displaying live drone status and delivery logs

## Setup Instructions
1. Ensure **Python 3** is installed.
2. Install dependencies:


3. Start the application:

4. Open your web browser to `http://localhost:5000` to view the dashboard.

## Usage
- The dashboard shows each drone’s ID, location, battery, and status.
- Click **Request New Delivery** to assign a random delivery to an idle drone.
- Delivery events (start and completion) are recorded in the blockchain log table.

## Notes
- Drone flights and blockchain writes include random delays (~10–50ms) to mimic 5G latency&#8203;:contentReference[oaicite:16]{index=16}&#8203;:contentReference[oaicite:17]{index=17}.
- The blockchain log is append-only and immutable, reflecting real blockchain properties&#8203;:contentReference[oaicite:18]{index=18}&#8203;:contentReference[oaicite:19]{index=19}.
- Flask (a lightweight Python web framework&#8203;:contentReference[oaicite:20]{index=20}) serves the dashboard and provides JSON endpoints for live updates.
