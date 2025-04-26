# network.py
import time, random

def simulate_5g_delay():
    """
    Simulate 5G network latency by sleeping for a random short duration.
    We choose between 0.01 and 0.05 seconds to represent ~10-50ms delay.
    """
    delay = random.uniform(0.01, 0.05)
    time.sleep(delay)
