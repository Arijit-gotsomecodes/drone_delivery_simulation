# drone.py
class Drone:
    def __init__(self, drone_id):
        self.id = drone_id
        self.status = "Idle"
        self.battery = 100.0
        self.location = [0, 0]
