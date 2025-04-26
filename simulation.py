# simulation.py
import time, random
from network import simulate_5g_delay

def simulate_delivery(drone, dest, blockchain):
    # 1. Record delivery initiation (with 5G delay)
    simulate_5g_delay()
    message = f"Delivery initiated by drone {drone.id} to {dest}"
    blockchain.add_block(message)

    # 2. Pre-flight check (battery must be sufficient)
    if drone.battery < 20:
        message = f"Drone {drone.id} pre-flight check failed (low battery)"
        blockchain.add_block(message)
        return

    # 3. Begin flight
    drone.status = "Pre-Flight"
    time.sleep(1)  # simulate pre-flight time
    drone.status = "In-Flight"

    # 4. Simulate movement step-by-step towards dest
    curr_x, curr_y = drone.location
    dest_x, dest_y = dest
    while [curr_x, curr_y] != [dest_x, dest_y]:
        # Move 1 unit in x, then 1 unit in y (simple pathfinding)
        if curr_x < dest_x: curr_x += 1
        elif curr_x > dest_x: curr_x -= 1
        if curr_y < dest_y: curr_y += 1
        elif curr_y > dest_y: curr_y -= 1
        drone.location = [curr_x, curr_y]

        # Drain some battery each step
        drain = random.uniform(0.5, 2.0)
        drone.battery = max(drone.battery - drain, 0)

        simulate_5g_delay()      # simulate delay in communication
        time.sleep(0.5)         # simulate travel time per step

    # 5. Arrive and complete delivery
    drone.status = "Delivered"
    message = f"Delivery completed by drone {drone.id} at {dest}"
    blockchain.add_block(message)
    simulate_5g_delay()

    # 6. Return to idle after short pause
    time.sleep(1)
    drone.status = "Idle"
